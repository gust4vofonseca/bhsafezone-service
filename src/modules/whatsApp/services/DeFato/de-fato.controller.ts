import { Controller, Post } from '@nestjs/common';
import { DeFatoService } from './de-fato.service';

@Controller('de-fato')
export class DeFatoController {
  constructor(private readonly deFatoService: DeFatoService) {}

  @Post()
  async sendMessage(): Promise<void> {
    await this.deFatoService.execute();
  }
}
