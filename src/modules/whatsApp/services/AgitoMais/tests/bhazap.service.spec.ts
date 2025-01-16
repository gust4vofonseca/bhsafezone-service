import { Test, TestingModule } from '@nestjs/testing';
import { BhazapService } from '../agito-mais.service';

describe('BhazapService', () => {
  let service: BhazapService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [BhazapService],
    }).compile();

    service = module.get<BhazapService>(BhazapService);
  });

  it('should be defined', () => {
    expect(service).toBeDefined();
  });
});
