import { Controller, Post } from '@nestjs/common';
import { BhazapService } from './bhazap.service';
import { Cron } from '@nestjs/schedule';
import { CronEnum } from '../../../../common/enums/cron.enum';

@Controller('bhazap')
export class BhazapController {
  constructor(private readonly bhazapService: BhazapService) {}

  @Cron(CronEnum.EVERY_6_HOURS)
  @Post()
  async sendMessage(): Promise<void> {
    await this.bhazapService.execute();
  }
}
