import { Schema as NestSchema, Prop } from '@nestjs/mongoose';

@NestSchema({
  timestamps: { createdAt: 'created_at', updatedAt: 'updated_at' },
})
export class BaseEntityWithoutTenant {
  @Prop({ type: String })
  created_by_name?: string;

  @Prop({ type: String })
  created_by_email?: string;

  @Prop({ type: String })
  updated_by_name?: string;

  @Prop({ type: String })
  updated_by_email?: string;

  @Prop({ type: Date })
  deleted_at?: Date;
}

export class BaseEntity extends BaseEntityWithoutTenant {
  @Prop({ nullable: true })
  _id: string;
}
