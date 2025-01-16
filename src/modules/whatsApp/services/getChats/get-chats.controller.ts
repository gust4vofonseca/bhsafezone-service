import { Controller, Post } from '@nestjs/common';
import { GetChatsService } from './get-chats.service';

@Controller('get-chats')
export class GetChatsControllers {
  constructor(private readonly getChats: GetChatsService) {}

  @Post()
  async sendMessage(): Promise<any> {
    return this.getChats.execute();
  }
}
