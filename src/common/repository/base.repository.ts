import { Injectable } from '@nestjs/common';
import { Model } from 'mongoose';
import { BaseEntity } from '../entity/base.entity';
import { IBaseMongoRepository } from '../interfaces/baseCommon/base.mongo.repository.interface';

@Injectable()
export abstract class BaseMongoRepository<T extends BaseEntity>
  implements IBaseMongoRepository<T>
{
  protected model: Model<T>;

  constructor(model: Model<T>) {
    this.model = model;
  }

  async findAll(): Promise<T[]> {
    return await this.model.find().exec();
  }

  async findOneById(_id: string, tenantid: string): Promise<T | null> {
    return await this.model.findOne({ _id, tenantid }).exec();
  }

  async create(entity: T): Promise<T> {
    const createdEntity = new this.model(entity);
    return await createdEntity.save();
  }

  async update(
    _id: string,
    tenantid: string,
    entity: Partial<T>,
  ): Promise<T | null> {
    return await this.model
      .findOneAndUpdate({ _id, tenantid }, entity, { new: true })
      .exec();
  }

  async delete(_id: string, tenantid: string): Promise<boolean> {
    const result = await this.model.findOneAndDelete({ _id, tenantid }).exec();
    return !!result;
  }
}
