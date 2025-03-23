import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { WhatsAppModule } from './modules/whatsApp/whatsapp.module';
import { WhatsappModule } from './system/whatsapp/whatsapp.module';
import { ClassifierModule } from './modules/classifier/classifier.module';
import { LocationModule } from './modules/location/location.module';
import { FirebaseModule } from './modules/firebase/firebase.module';
@Module({
  imports: [
    MongooseModule.forRoot('mongodb://localhost:27017/bh-safezone'),
    WhatsappModule,
    WhatsAppModule,
    ClassifierModule,
    LocationModule,
    FirebaseModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
