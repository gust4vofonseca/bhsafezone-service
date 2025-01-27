import { Inject, Injectable } from '@nestjs/common';
import { WhatsAppRepository } from '../../whatsApp/repository/whatsapp.repository';
import { NeuralNetwork } from 'brain.js';
import { FilterService } from './filter';
import { locateARegion } from './location';

@Injectable()
export class ClassifierService {
  private classifier: NeuralNetwork<Record<string, number>, { crime: number }>;

  constructor(
    @Inject(WhatsAppRepository)
    private whatsAppRepository: WhatsAppRepository,

    @Inject(FilterService)
    private filterService: FilterService,
  ) {
    this.classifier = new NeuralNetwork();
  }

  async execute(): Promise<void> {
    if (!(await this.train())) return;

    const data = await this.whatsAppRepository.getByClassifiedFalse();

    for (const item of data) {
      const text = `${item.body} ${item.title} ${item.description}`;
      const filter = this.filterService.containsCrime(text);

      if (filter) {
        const features = textToFeatures(text);
        const prediction = this.classifier.run(features);
        const isCrime = prediction.crime > 0.5;
        const region = locateARegion(text);

        await this.whatsAppRepository.update(item._id, {
          classified: true,
          crimeType: filter,
          isCrime: isCrime,
          region,
        });
      } else {
        await this.whatsAppRepository.update(item._id, {
          classified: true,
          isCrime: false,
        });
      }
    }

    console.log('Fim da classificação');
  }

  async train(): Promise<boolean> {
    const trainingData = [];

    const crimesWithType =
      await this.whatsAppRepository.getByIsCrimeTrueWithType();
    crimesWithType.forEach((message) => {
      trainingData.push({
        input: textToFeatures(`${message.body}`),
        output: { crime: 1 },
      });
    });

    const nonCrimesWithType =
      await this.whatsAppRepository.getByIsCrimeFalseWithType();
    nonCrimesWithType.forEach((message) => {
      trainingData.push({
        input: textToFeatures(`${message.body}`),
        output: { crime: 0 },
      });
    });

    const nonCrimesWithoutType =
      await this.whatsAppRepository.getByIsCrimeFalseWithoutType();
    nonCrimesWithoutType.forEach((message) => {
      trainingData.push({
        input: textToFeatures(`${message.body}`),
        output: { crime: 0 },
      });
    });

    [
      {
        input: textToFeatures('assaltaram na esquina'),
        output: { crime: 1 },
      },
      {
        input: textToFeatures(
          'Furtaram uma moto no estacionamento de um mercado',
        ),
        output: { crime: 1 },
      },
      { input: textToFeatures('bom dia, amigos'), output: { crime: 0 } },
      {
        input: textToFeatures(
          'Uma menina foi abusada hoje por um homem no metro',
        ),
        output: { crime: 1 },
      },
      {
        input: textToFeatures('alguém foi furtado ontem'),
        output: { crime: 1 },
      },
      { input: textToFeatures('tem promoção na loja'), output: { crime: 0 } },
      {
        input: textToFeatures('Os preços no supermercado esta um roubo'),
        output: { crime: 0 },
      },
    ].map((item) => trainingData.push(item));

    try {
      this.classifier.train(trainingData);

      return true;
    } catch (error) {
      return false;
    }
  }
}

function textToFeatures(text: string): Record<string, number> {
  const words = text.toLowerCase().split(/\s+/);
  const features: Record<string, number> = {};

  for (const word of words) {
    features[word] = (features[word] || 0) + 1;
  }

  return features;
}
