import { Injectable, OnModuleInit } from '@nestjs/common';
import { Client, LocalAuth } from 'whatsapp-web.js';
import * as qrcode from 'qrcode-terminal';

@Injectable()
export class WhatsappService implements OnModuleInit {
  private client: Client;

  constructor() {
    this.client = new Client({
      authStrategy: new LocalAuth({
        clientId: 'bhsafezone-service',
      }),
      puppeteer: {
        headless: true, // O Puppeteer usará o Chromium baixado automaticamente
      },
    });

    this.client.on('qr', (qr) => {
      qrcode.generate(qr, { small: true });
    });

    this.client.on('ready', () => {
      console.log('WhatsApp client is ready!');
    });

    this.client.on('message', (message) => {
      console.log(`Mensagem de ${message.from}: ${message.body}`);
    });

    this.client.on('error', (error) => {
      console.error('Erro no cliente:', error);
    });
  }

  onModuleInit() {
    this.client.initialize();
  }

  async fetchMessage(): Promise<any> {
    this.client.on('ready', () => {
      console.log('okay');
    });

    const groupName = 'BHAZap #25'; // Substitua pelo nome do grupo

    const chats = await this.client.getChats();

    const groupChat = chats.find((c) => c.name === groupName);

    if (!groupChat) {
      console.log('Grupo não encontrado!');
      return;
    }

    const groupChat2 = await this.client.getChatById(groupChat.id._serialized);

    const messages = await groupChat2.fetchMessages({ limit: 50 });

    console.log({ messages });
    console.log({ tamanho: messages.length });

    return groupChat;
  }
}

// name: 'BHAZap #19',
// id: {
//   server: 'g.us',
//   user: '120363285740319093',
//   _serialized: '120363285740319093@g.us'
// }
