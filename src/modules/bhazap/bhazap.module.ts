import { Module } from '@nestjs/common';
import { BhazapService } from './services/fetch/bhazap.service';
import { BhazapController } from './services/fetch/bhazap.controller';
import { WhatsappService } from '../../system/whatsapp/whatsapp.service';
import { MongooseModule } from '@nestjs/mongoose';
import { WhatsAppSchema } from './schema/whatsapp.schema';
import { WhatsAppRepository } from './repository/whatsapp.repository';

@Module({
  imports: [
    MongooseModule.forFeature([{ name: 'WhatsApp', schema: WhatsAppSchema }]),
  ],
  providers: [BhazapService, WhatsappService, WhatsAppRepository],
  controllers: [BhazapController],
})
export class BhazapModule {}
