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
import { GetChatsControllers } from './services/getChats/get-chats.controller';
import { GetChatsService } from './services/getChats/get-chats.service';
import { JCOController } from './services/JCO/jco.controller';
import { JCAController } from './services/JCA/jca.controller';
import { DeFatoController } from './services/DeFato/de-fato.controller';
import { AgitoMaisService } from './services/AgitoMais/agito-mais.service';
import { JCOService } from './services/JCO/jco.service';
import { JCAService } from './services/JCA/jca.service';
import { DeFatoService } from './services/DeFato/de-fato.service';
import { AgitoMaisController } from './services/AgitoMais/agito-mais.controller';

@Module({
  imports: [
    MongooseModule.forFeature([
      { name: WhatsApp.name, schema: WhatsAppSchema },
    ]),
  ],
  providers: [
    GetChatsService,
    BhazapService,
    PorDentroDeMinasService,
    WhatsappService,
    WhatsAppRepository,
    JCOService,
    JCAService,
    DeFatoService,
    AgitoMaisService,
  ],
  controllers: [
    GetChatsControllers,
    BhazapController,
    PorDentroDeMinasController,
    JCOController,
    JCAController,
    DeFatoController,
    AgitoMaisController,
  ],
})
export class WhatsAppModule {}
