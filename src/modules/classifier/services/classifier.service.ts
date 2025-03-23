import { Inject, Injectable } from '@nestjs/common';
import { spawn } from 'child_process';
import { WhatsAppRepository } from '../../whatsApp/repository/whatsapp.repository';
import { FilterService } from './filter';

@Injectable()
export class ClassifierService {
  constructor(
    @Inject(WhatsAppRepository)
    private whatsAppRepository: WhatsAppRepository,

    @Inject(FilterService)
    private filterService: FilterService,
  ) {}

  async execute(): Promise<any> {
    let index = 0;
    const data = await this.whatsAppRepository.getByClassifiedFalse();

    for (const item of data) {
      const text = `${item.body} ${item.title} ${item.description}`;
      const filter = this.filterService.containsCrime(text);

      if (filter) {
        index++;
        await this.whatsAppRepository.update(item._id, {
          classified: 0,
          crime: filter,
        });
      } else {
        await this.whatsAppRepository.update(item._id, {
          classified: 1,
          is_crime: 0,
        });
      }
    }

    console.log({ index });

    new Promise((resolve, reject) => {
      const pythonProcess = spawn('python3', [
        'src/modules/classifier/services/classifier.py',
      ]);

      let output = '';

      pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        const errorMessage = data.toString();
        console.error(`Erro: ${errorMessage}`);

        // Ignorar mensagens do NLTK que não são erros críticos
        if (!errorMessage.includes('[nltk_data]')) {
          reject(new Error(errorMessage));
        }
      });

      pythonProcess.on('close', (code) => {
        if (code === 0) {
          resolve(output);
        } else {
          reject(new Error(`Processo encerrado com código ${code}`));
        }
      });
    }).catch((err) => {
      console.error('Erro no processamento do classificador:', err);
      throw err;
    });
  }
}
