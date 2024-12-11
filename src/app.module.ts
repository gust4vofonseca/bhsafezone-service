import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { WhatsappModule } from './system/whatsapp/whatsapp.module';
import { BhazapModule } from './modules/bhazap/bhazap.module';
@Module({
  imports: [WhatsappModule, BhazapModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
