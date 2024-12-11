import { Module } from '@nestjs/common';
import { BhazapService } from './services/fetch/bhazap.service';
import { BhazapController } from './services/fetch/bhazap.controller';
import { WhatsappService } from '../../system/whatsapp/whatsapp.service';

@Module({
  providers: [BhazapService, WhatsappService],
  controllers: [BhazapController],
})
export class BhazapModule {}
