import { Controller, Post } from '@nestjs/common';
import { DeFatoService } from './de-fato.service';
import { Cron } from '@nestjs/schedule';
import { CronEnum } from '../../../../common/enums/cron.enum';

@Controller('de-fato')
export class DeFatoController {
  constructor(private readonly deFatoService: DeFatoService) {}

  @Cron(CronEnum.EVERY_6_HOURS)
  @Post()
  async sendMessage(): Promise<void> {
    await this.deFatoService.execute();
  }
}
