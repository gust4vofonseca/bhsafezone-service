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
        headless: true,
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

  async fetchMessage(id: string): Promise<any> {
    const groupChat2 = await this.client.getChatById(id);

    const messages = await groupChat2.fetchMessages({});

    return messages;
  }
}
