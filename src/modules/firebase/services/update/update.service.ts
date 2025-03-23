import { Inject, Injectable } from '@nestjs/common';
import { WhatsAppRepository } from '../../../whatsApp/repository/whatsapp.repository';
import { FirebaseService } from '../conection/firebase.service';
import { RegionEnum } from '../../enum/Region.enum';

@Injectable()
export class IntegratedInFireStoreService {
  constructor(
    @Inject(WhatsAppRepository)
    private whatsAppRepository: WhatsAppRepository,

    @Inject(FirebaseService)
    private firebaseService: FirebaseService,
  ) {}

  async execute(): Promise<any> {
    const data = await this.whatsAppRepository.getByIntegratedFalse();

    for (const item of data) {
      await this.firebaseService.upsertCrimeRegion(
        RegionEnum[item.region.toLocaleUpperCase()],
        item.crime,
        1,
      );

      await this.firebaseService.upsertCrimePorBairro(
        RegionEnum[item.region.toLocaleUpperCase()],
        item.bairro,
        item.crime,
        1,
      );

      await this.firebaseService.upsertCrimePorTimeSeries(
        RegionEnum[item.region.toLocaleUpperCase()],
        'time_series',
        formatarMesAnoNumerico(item.created_at),
        item.crime,
        1,
      );

      await this.firebaseService.upsertCrimeRegion(
        'Geral',
        RegionEnum[item.region.toLocaleUpperCase()],
        1,
      );

      await this.firebaseService.upsertCrimePorTimeSeries(
        'Geral',
        'time_series',
        formatarMesAnoNumerico(item.created_at),
        item.crime,
        1,
      );

      await this.whatsAppRepository.update(item._id, {
        integrated: 1,
      });
    }
  }
}

function formatarMesAnoNumerico(data: Date): string {
  const mes = String(data.getMonth() + 1).padStart(2, '0');
  const ano = data.getFullYear();

  return `${mes}-${ano}`;
}
