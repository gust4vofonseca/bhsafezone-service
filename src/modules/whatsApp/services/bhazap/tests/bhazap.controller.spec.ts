import { Test, TestingModule } from '@nestjs/testing';
import { BhazapController } from './bhazap.controller';

describe('BhazapController', () => {
  let controller: BhazapController;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      controllers: [BhazapController],
    }).compile();

    controller = module.get<BhazapController>(BhazapController);
  });

  it('should be defined', () => {
    expect(controller).toBeDefined();
  });
});
