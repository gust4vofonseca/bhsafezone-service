import { Module } from '@nestjs/common';
import { CrimeClassificationController } from './services/classifier.controller';
import { ClassifierService } from './services/classifier.service';
import { WhatsAppRepository } from '../whatsApp/repository/whatsapp.repository';
import { MongooseModule } from '@nestjs/mongoose';
import { WhatsApp } from '../whatsApp/classes/WhatsApp.class';
import { WhatsAppSchema } from '../whatsApp/schema/whatsapp.schema';
import { FilterService } from './services/filter';
import { FirebaseService } from '../firebase/services/conection/firebase.service';

@Module({
  imports: [
    MongooseModule.forFeature([
      { name: WhatsApp.name, schema: WhatsAppSchema },
    ]),
  ],
  providers: [
    WhatsAppRepository,
    ClassifierService,
    FilterService,
    FirebaseService,
  ],
  controllers: [CrimeClassificationController],
})
export class ClassifierModule {}
