import { Controller, Post } from '@nestjs/common';
import { PorDentroDeMinasService } from './por-dentro-de-minas.service';
import { Cron } from '@nestjs/schedule';
import { CronEnum } from '../../../../common/enums/cron.enum';

@Controller('por-dentro-de-minas')
export class PorDentroDeMinasController {
  constructor(
    private readonly porDentroDeMinasService: PorDentroDeMinasService,
  ) {}

  @Cron(CronEnum.EVERY_6_HOURS)
  @Post()
  async sendMessage(): Promise<void> {
    await this.porDentroDeMinasService.execute();
  }
}
