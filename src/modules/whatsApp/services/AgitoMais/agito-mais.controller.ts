import { Controller, Post } from '@nestjs/common';
import { AgitoMaisService } from './agito-mais.service';
import { Cron } from '@nestjs/schedule';
import { CronEnum } from '../../../../common/enums/cron.enum';

@Controller('agito-mais')
export class AgitoMaisController {
  constructor(private readonly agitoMaisService: AgitoMaisService) {}

  @Cron(CronEnum.EVERY_DAY_AT_10AM)
  @Post()
  async sendMessage(): Promise<void> {
    await this.agitoMaisService.execute();
  }
}
