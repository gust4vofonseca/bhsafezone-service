import { BaseEntity } from '../../entity/base.entity';
export interface IBaseMongoRepository<T extends BaseEntity> {
  findAll(): Promise<T[]>;
  findOneById(id: string, tenantid: string): Promise<T | null>;
  create(entity: T): Promise<T>;
  update(id: string, tenantid: string, entity: Partial<T>): Promise<T | null>;
  delete(id: string, tenantid: string): Promise<boolean>;
}
