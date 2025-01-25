import { Controller, Post } from '@nestjs/common';
import { JCAService } from './jca.service';
import { Cron } from '@nestjs/schedule';
import { CronEnum } from '../../../../common/enums/cron.enum';

@Controller('jca')
export class JCAController {
  constructor(private readonly jCAService: JCAService) {}

  @Cron(CronEnum.EVERY_6_HOURS)
  @Post()
  async sendMessage(): Promise<void> {
    await this.jCAService.execute();
  }
}
