import { Cron } from '@nestjs/schedule';
import { CronEnum } from '../../../../common/enums/cron.enum';
import { BhazapService } from './bhazap.service';

export class BhazapController {
  constructor(private readonly bhazapService: BhazapService) {}

  @Cron(CronEnum.EVERY_DAY_AT_10AM)
  async sendMessage(): Promise<void> {
    await this.bhazapService.execute();
  }
}
