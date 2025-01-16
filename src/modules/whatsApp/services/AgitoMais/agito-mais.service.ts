import { Inject, Injectable } from '@nestjs/common';
import { WhatsappService } from '../../../../system/whatsapp/whatsapp.service';
import { WhatsAppRepository } from '../../repository/whatsapp.repository';

@Injectable()
export class AgitoMaisService {
  constructor(
    @Inject(WhatsappService)
    private whatsappService: WhatsappService,

    @Inject(WhatsAppRepository)
    private whatsAppRepository: WhatsAppRepository,
  ) {}

  async execute(): Promise<void> {
    // 120363091079412102@g.us
    const data = await this.whatsappService.fetchMessage(
      '120363091079412102@g.us',
    );

    for (const item of data) {
      if (item.body !== '') {
        try {
          await this.whatsAppRepository.create({
            ...item,
            origin: 'Agito Mais',
            classified: false,
          });
        } catch (error) {
          console.log({ error });
        }
      }
    }
  }
}

// {
//   id: {
//     server: 'g.us',
//     user: '120363040839837629',
//     _serialized: '120363040839837629@g.us'
//   },
//   name: 'Notícias - Por Dentro de Minas (1)'
// }
