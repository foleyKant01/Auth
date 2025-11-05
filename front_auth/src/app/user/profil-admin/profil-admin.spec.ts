import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProfilAdmin } from './profil-admin';

describe('ProfilAdmin', () => {
  let component: ProfilAdmin;
  let fixture: ComponentFixture<ProfilAdmin>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [ProfilAdmin]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProfilAdmin);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
