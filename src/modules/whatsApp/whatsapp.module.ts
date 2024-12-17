import { Module } from '@nestjs/common';
import { BhazapService } from './services/bhazap/bhazap.service';
import { BhazapController } from './services/bhazap/bhazap.controller';
import { WhatsappService } from '../../system/whatsapp/whatsapp.service';
import { MongooseModule } from '@nestjs/mongoose';
import { WhatsAppSchema } from './schema/whatsapp.schema';
import { WhatsAppRepository } from './repository/whatsapp.repository';
import { WhatsApp } from './classes/WhatsApp.class';
import { PorDentroDeMinasService } from './services/porDentroDeMinas/por-dentro-de-minas.service';
import { PorDentroDeMinasController } from './services/porDentroDeMinas/por-dentro-de-minas.controller';

@Module({
  imports: [
    MongooseModule.forFeature([
      { name: WhatsApp.name, schema: WhatsAppSchema },
    ]),
  ],
  providers: [
    BhazapService,
    PorDentroDeMinasService,
    WhatsappService,
    WhatsAppRepository,
  ],
  controllers: [BhazapController, PorDentroDeMinasController],
})
export class WhatsAppModule {}
