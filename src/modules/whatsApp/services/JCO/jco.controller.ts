import { Controller, Post } from '@nestjs/common';
import { JCOService } from './jco.service';

@Controller('jco')
export class JCOController {
  constructor(private readonly jCOService: JCOService) {}

  @Post()
  async sendMessage(): Promise<void> {
    await this.jCOService.execute();
  }
}
