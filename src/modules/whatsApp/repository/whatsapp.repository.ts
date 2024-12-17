import { Injectable } from '@nestjs/common';
import { BaseMongoRepository } from '../../../common/repository/base.repository';
import { WhatsApp } from '../classes/WhatsApp.class';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';

@Injectable()
export class WhatsAppRepository extends BaseMongoRepository<WhatsApp> {
  constructor(@InjectModel(WhatsApp.name) model: Model<WhatsApp>) {
    super(model);
  }
}
