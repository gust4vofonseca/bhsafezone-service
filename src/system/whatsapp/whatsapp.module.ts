import { Module } from '@nestjs/common';
import { WhatsappService } from './whatsapp.service';

@Module({
  providers: [WhatsappService],
  controllers: [],
})
export class WhatsappModule {}
