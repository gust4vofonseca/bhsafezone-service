import { Controller, Post } from '@nestjs/common';
import { JCOService } from './jco.service';
import { Cron } from '@nestjs/schedule';
import { CronEnum } from '../../../../common/enums/cron.enum';

@Controller('jco')
export class JCOController {
  constructor(private readonly jCOService: JCOService) {}

  @Cron(CronEnum.EVERY_6_HOURS)
  @Post()
  async sendMessage(): Promise<void> {
    await this.jCOService.execute();
  }
}
