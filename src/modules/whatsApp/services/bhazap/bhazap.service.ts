import { Inject, Injectable } from '@nestjs/common';
import { WhatsappService } from '../../../../system/whatsapp/whatsapp.service';
import { WhatsAppRepository } from '../../repository/whatsapp.repository';

@Injectable()
export class BhazapService {
  constructor(
    @Inject(WhatsappService)
    private whatsappService: WhatsappService,

    @Inject(WhatsAppRepository)
    private whatsAppRepository: WhatsAppRepository,
  ) {}

  async execute(): Promise<void> {
    //120363372671317259@g.us
    const data = await this.whatsappService.fetchMessage(
      '120363372671317259@g.us',
    );

    for (const item of data) {
      if (item.body !== '') {
        try {
          await this.whatsAppRepository.create({
            ...item,
            origin: 'bhazap',
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
//     user: '120363372671317259',
//     _serialized: '120363372671317259@g.us'
//   },
//   name: 'BHAZap #25'
// }
