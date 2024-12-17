import { Controller, Post } from '@nestjs/common';
import { BhazapService } from './bhazap.service';

@Controller('bhazap')
export class BhazapController {
  constructor(private readonly bhazapService: BhazapService) {}

  @Post()
  async sendMessage(): Promise<void> {
    await this.bhazapService.execute();
  }
}
