import { Controller, Post } from '@nestjs/common';
import { PorDentroDeMinasService } from './por-dentro-de-minas.service';

@Controller('por-dentro-de-minas')
export class PorDentroDeMinasController {
  constructor(
    private readonly porDentroDeMinasService: PorDentroDeMinasService,
  ) {}

  @Post()
  async sendMessage(): Promise<void> {
    await this.porDentroDeMinasService.execute();
  }
}
