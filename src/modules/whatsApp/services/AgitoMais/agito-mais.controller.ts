import { Controller, Post } from '@nestjs/common';
import { AgitoMaisService } from './agito-mais.service';

@Controller('agito-mais')
export class AgitoMaisController {
  constructor(private readonly agitoMaisService: AgitoMaisService) {}

  @Post()
  async sendMessage(): Promise<void> {
    await this.agitoMaisService.execute();
  }
}
