import { TestBed } from '@angular/core/testing';
import { PetCareService } from './pet-care.service';
import { HttpClientTestingModule } from '@angular/common/http/testing';

describe('PetCareService', () => {
  let service: PetCareService;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [HttpClientTestingModule]
    });
    service = TestBed.inject(PetCareService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
