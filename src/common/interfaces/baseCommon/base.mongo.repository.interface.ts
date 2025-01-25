import { BaseEntity } from '../../entity/base.entity';
export interface IBaseMongoRepository<T extends BaseEntity> {
  findAll(): Promise<T[]>;
  findOneById(id: string): Promise<T | null>;
  create(entity: T): Promise<T>;
  update(id: string, entity: Partial<T>): Promise<T | null>;
  delete(id: string): Promise<boolean>;
}
