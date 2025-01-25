import { BaseEntity } from '../../../common/entity/base.entity';

export class WhatsApp extends BaseEntity {
  body?: string; // Corpo da mensagem
  mediaKey?: string; // Chave de mídia, se presente
  ack?: number; // Status de confirmação
  hasMedia?: boolean; // Indica se há mídia associada
  type?: string; // Tipo de mensagem (ex: chat, image, etc.)
  timestamp?: number; // Timestamp da mensagem
  from?: string; // Identificador do remetente
  to?: string; // Identificador do destinatário
  author?: string; // Autor da mensagem
  deviceType?: string; // Tipo de dispositivo (ex: iOS, Android)
  isForwarded?: boolean; // Indica se a mensagem foi encaminhada
  forwardingScore?: number; // Quantidade de vezes que a mensagem foi encaminhada
  isStatus?: boolean; // Indica se é uma mensagem de status
  isStarred?: boolean; // Indica se a mensagem está marcada
  broadcast?: boolean; // Indica se a mensagem foi enviada em transmissão
  fromMe?: boolean; // Indica se a mensagem foi enviada por você
  hasQuotedMsg?: boolean; // Indica se há uma mensagem citada
  hasReaction?: boolean; // Indica se há reações na mensagem
  vCards?: string[]; // Lista de vCards associados
  mentionedIds?: string[]; // Lista de IDs mencionados na mensagem
  groupMentions?: string[]; // Mencionados em grupos
  isGif?: boolean; // Indica se a mídia é um GIF
  title?: string; // Título associado à mensagem (se aplicável)
  description?: string; // Descrição da mensagem
  links?: { link: string; isSuspicious: boolean }[]; // Lista de links na mensagem
  classified?: boolean; // Indica se a mensagem foi classificada
  isCrime?: boolean; // Indica se a mensagem se refere a um crime
  region?: string;
  crimeType?: string; // Tipo de crime identificado
  created_at?: Date; // Data de criação
  updated_at?: Date; // Data de atualização
}
