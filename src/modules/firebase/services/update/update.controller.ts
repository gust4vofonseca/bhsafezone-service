import { Controller, Post } from '@nestjs/common';
import { Cron } from '@nestjs/schedule';
import { IntegratedInFireStoreService } from './update.service';
import { CronEnum } from '../../../../common/enums/cron.enum';

@Controller('firebase')
export class IntegratedInFireStoreController {
  constructor(
    private integratedInFireStoreService: IntegratedInFireStoreService,
  ) {}

  @Cron(CronEnum.EVERY_6_HOURS)
  @Post()
  handle() {
    this.integratedInFireStoreService.execute();
  }
}
