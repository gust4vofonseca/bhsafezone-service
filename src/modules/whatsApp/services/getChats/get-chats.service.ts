import { Inject, Injectable } from '@nestjs/common';
import { WhatsappService } from '../../../../system/whatsapp/whatsapp.service';

@Injectable()
export class GetChatsService {
  constructor(
    @Inject(WhatsappService)
    private whatsappService: WhatsappService,
  ) {}

  async execute(): Promise<any> {
    const data = await this.whatsappService.getChats();

    return data;
  }
}
