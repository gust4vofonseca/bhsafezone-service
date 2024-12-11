import { Inject, Injectable } from '@nestjs/common';
import { WhatsappService } from '../../../../system/whatsapp/whatsapp.service';

@Injectable()
export class BhazapService {
  constructor(
    @Inject(WhatsappService)
    private whatsappService: WhatsappService,
  ) {}

  async execute(): Promise<void> {
    console.log('Chegou aqui');

    const teste = await this.whatsappService.fetchMessage();

    console.log({ teste });
  }
}
