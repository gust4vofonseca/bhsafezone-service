import { Schema } from 'mongoose';

export const WhatsAppSchema = new Schema(
  {
    body: { type: 'string', unique: true },
  },
  {
    strict: false,
    timestamps: { createdAt: 'created_at', updatedAt: 'updated_at' },
  },
);
