import { Injectable } from '@nestjs/common';
import { BaseMongoRepository } from '../../../common/repository/base.repository';
import { WhatsApp } from '../classes/WhatsApp.class';

@Injectable()
export class WhatsAppRepository extends BaseMongoRepository<WhatsApp> {}
