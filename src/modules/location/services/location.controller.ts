import { Controller, Post } from '@nestjs/common';
import { Cron } from '@nestjs/schedule';
import { CronEnum } from '../../../common/enums/cron.enum';
import { LocationService } from './location.service';

@Controller('location')
export class LocationController {
  constructor(private locationService: LocationService) {}

  @Cron(CronEnum.EVERY_6_HOURS)
  @Post()
  handle() {
    this.locationService.execute();
  }
}
