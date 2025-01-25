import { Controller, Post } from '@nestjs/common';
import { ClassifierService } from './classifier.service';
import { Cron } from '@nestjs/schedule';
import { CronEnum } from '../../../common/enums/cron.enum';

@Controller('crime-classification')
export class CrimeClassificationController {
  constructor(private readonly classificationService: ClassifierService) {}

  @Cron(CronEnum.EVERY_6_HOURS)
  @Post('analyze')
  analyzeText() {
    this.classificationService.execute();
  }
}
