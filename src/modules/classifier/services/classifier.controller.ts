import { Controller, Post } from '@nestjs/common';
import { ClassifierService } from './classifier.service';

@Controller('crime-classification')
export class CrimeClassificationController {
  constructor(private readonly classificationService: ClassifierService) {}

  @Post('analyze')
  analyzeText() {
    this.classificationService.execute();
  }
}
