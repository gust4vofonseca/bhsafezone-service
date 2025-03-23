import { Module } from '@nestjs/common';
import { IntegratedInFireStoreController } from './services/update/update.controller';
import { IntegratedInFireStoreService } from './services/update/update.service';
import { WhatsAppRepository } from '../whatsApp/repository/whatsapp.repository';
import { FirebaseService } from './services/conection/firebase.service';
import { MongooseModule } from '@nestjs/mongoose';
import { WhatsApp } from '../whatsApp/classes/WhatsApp.class';
import { WhatsAppSchema } from '../whatsApp/schema/whatsapp.schema';

@Module({
  imports: [
    MongooseModule.forFeature([
      { name: WhatsApp.name, schema: WhatsAppSchema },
    ]),
  ],
  providers: [
    IntegratedInFireStoreService,
    WhatsAppRepository,
    FirebaseService,
  ],
  controllers: [IntegratedInFireStoreController],
})
export class FirebaseModule {}
