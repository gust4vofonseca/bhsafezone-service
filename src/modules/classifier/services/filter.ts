import { Injectable } from '@nestjs/common';

@Injectable()
export class FilterService {
  private crimeDictionary: Record<string, string> = {
    roubo: 'Roubo',
    roubado: 'Roubo',
    roubada: 'Roubo',
    furto: 'Furto',
    furtado: 'Furto',
    furtada: 'Furto',
    'batedor de carteira': 'Furto',
    trombadinha: 'Furto',
    assalto: 'Assalto',
    assaltada: 'Assalto',
    assaltado: 'Assalto',
    arrastão: 'Assalto',
    feminicídio: 'Feminicídio',
    estupro: 'Estupro',
    estuprado: 'Estupro',
    estuprada: 'Estupro',
    violentado: 'Estupro',
    violentada: 'Estupro',
    'violência sexual': 'Estupro',
    'abuso sexual': 'Estupro',
    abusada: 'Estupro',
    abusado: 'Estupro',
    'importunação sexual': 'Estupro',
    extorsão: 'Extorsão',
    coagido: 'Extorsão',
    coagir: 'Extorsão',
    'lesão corporal': 'Lesão Corporal',
    briga: 'Lesão Corporal',
    confronto: 'Lesão Corporal',
    agressão: 'Lesão Corporal',
    agredida: 'Lesão Corporal',
    agredido: 'Lesão Corporal',
    confusão: 'Lesão Corporal',
    'violência doméstica': 'Lesão Corporal',
    sequestro: 'Sequestro',
    perseguição: 'Sequestro',
    homicídio: 'Homicídio',
    assassinado: 'Homicídio',
    assassinada: 'Homicídio',
    'tráfico de drogas': 'Tráfico de Drogas',
    tráfico: 'Tráfico de Drogas',
    drogas: 'Tráfico de Drogas',
    maconha: 'Tráfico de Drogas',
    entorpecente: 'Tráfico de Drogas',
    cocaína: 'Tráfico de Drogas',
    lsd: 'Tráfico de Drogas',
    ecstasy: 'Tráfico de Drogas',
    heroína: 'Tráfico de Drogas',
    'tentativa de homicídio': 'Tentativa de Homicídio',
    baleado: 'Tentativa de Homicídio',
    baleada: 'Tentativa de Homicídio',
    depredação: 'Depredação',
    pichações: 'Depredação',
    pichação: 'Depredação',
    vandalismo: 'Depredação',
    vandalização: 'Depredação',
    incêndio: 'Incêndio',
    incendiar: 'Incêndio',
    incendiou: 'Incêndio',
    incendiaram: 'Incêndio',
  };

  containsCrime(text: string): string | undefined {
    const lowerText = text.toLowerCase();
    for (const [term, crime] of Object.entries(this.crimeDictionary)) {
      if (lowerText.includes(term)) {
        return crime;
      }
    }
    return undefined;
  }
}
