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

  public async getByClassifiedTrue(): Promise<WhatsApp[]> {
    return this.model.find({ classified: true }).exec();
  }

  public async getByClassifiedFalse(): Promise<WhatsApp[]> {
    return this.model.find().exec();
  }

  public async getByIsCrimeTrueWithType(): Promise<WhatsApp[]> {
    return this.model
      .find({ isCrime: true, crimeType: { $exists: true } })
      .limit(20)
      .exec();
  }

  public async getByIsCrimeFalseWithType(): Promise<WhatsApp[]> {
    return this.model
      .find({ isCrime: false, crimeType: { $exists: true } })
      .limit(20)
      .exec();
  }

  public async getByIsCrimeFalseWithoutType(): Promise<WhatsApp[]> {
    return this.model
      .find({ isCrime: false, crimeType: { $exists: false } })
      .limit(20)
      .exec();
  }
}
