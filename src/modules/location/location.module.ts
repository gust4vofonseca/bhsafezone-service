import { Module } from '@nestjs/common';
import { LocationController } from './services/location.controller';
import { LocationService } from './services/location.service';

@Module({
  imports: [],
  providers: [LocationService],
  controllers: [LocationController],
})
export class LocationModule {}
