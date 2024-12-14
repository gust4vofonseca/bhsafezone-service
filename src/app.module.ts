import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { BhazapModule } from './modules/bhazap/bhazap.module';
import { WhatsappModule } from './system/whatsapp/whatsapp.module';
@Module({
  imports: [
    MongooseModule.forRoot('mongodb://localhost:27017/bh-safezone'),
    WhatsappModule,
    BhazapModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
