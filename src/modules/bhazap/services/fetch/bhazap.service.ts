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
    console.log('Chegou aqui');

    //120363372671317259@g.us
    const data = await this.whatsappService.fetchMessage(
      '120363372671317259@g.us',
    );

    for (const item of data) {
      if (item.body !== '') {
        console.log(item);
        try {
          await this.whatsAppRepository.create(item);
        } catch (error) {
          console.log({ error });
        }
      }
    }
  }
}
