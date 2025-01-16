import { Controller, Post } from '@nestjs/common';
import { JCAService } from './jca.service';

@Controller('jca')
export class JCAController {
  constructor(private readonly jCAService: JCAService) {}

  @Post()
  async sendMessage(): Promise<void> {
    await this.jCAService.execute();
  }
}
