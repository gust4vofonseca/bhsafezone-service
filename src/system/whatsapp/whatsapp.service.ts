import { Injectable, OnModuleInit } from '@nestjs/common';
import { Client, LocalAuth } from 'whatsapp-web.js';
import * as qrcode from 'qrcode-terminal';
import * as fs from 'fs';
import * as path from 'path';

@Injectable()
export class WhatsappService implements OnModuleInit {
  private client: Client;

  constructor() {
    deleteFolders();

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
    try {
      const getChatById = await this.client.getChatById(id);

      const messages = await getChatById.fetchMessages({
        limit: 1000,
        fromMe: false,
      });

      return messages;
    } catch (error) {
      console.log({ error });
      return [];
    }
  }

  // async getChats(): Promise<any> {
  //   try {
  //     const getChatById = await this.client.getChats();

  //     console.log({ getChatById });

  //     return getChatById;
  //   } catch (error) {
  //     console.log({ error });
  //     return [];
  //   }
  // }
}

async function deleteFolders() {
  const foldersToDelete = [
    path.join(__dirname, '../../../.wwebjs_auth'),
    path.join(__dirname, '../../../.wwebjs_cache'),
  ];

  for (const folder of foldersToDelete) {
    try {
      if (fs.existsSync(folder)) {
        await fs.promises.rm(folder, { recursive: true, force: true });
        console.log(`Deleted: ${folder}`);
      } else {
        console.log(`Folder not found: ${folder}`);
      }
    } catch (err) {
      console.error(`Error deleting folder ${folder}:`, err);
    }
  }
}
