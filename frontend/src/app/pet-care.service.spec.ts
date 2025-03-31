import { TestBed } from '@angular/core/testing';

import { PetCareService } from './pet-care.service';

describe('PetCareService', () => {
  let service: PetCareService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PetCareService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
