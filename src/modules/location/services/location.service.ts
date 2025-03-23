import { Injectable } from '@nestjs/common';
import { spawn } from 'child_process';

@Injectable()
export class LocationService {
  async execute(): Promise<any> {
    new Promise((resolve, reject) => {
      const pythonProcess = spawn('python3', [
        'src/modules/location/services/location.py',
      ]);

      let output = '';

      pythonProcess.stdout.on('data', (data) => {
        output += data.toString();
      });

      pythonProcess.stderr.on('data', (data) => {
        const errorMessage = data.toString();
        console.error(`Erro: ${errorMessage}`);
      });

      pythonProcess.on('close', (code) => {
        if (code === 0) {
          resolve(output);
        } else {
          reject(new Error(`Processo encerrado com código ${code}`));
        }
      });
    }).catch((err) => {
      console.error('Erro no processamento do classificador:', err);
      throw err;
    });
  }
}
