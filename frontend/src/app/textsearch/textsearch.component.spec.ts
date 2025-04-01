import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TextsearchComponent } from './textsearch.component';

describe('TextsearchComponent', () => {
  let component: TextsearchComponent;
  let fixture: ComponentFixture<TextsearchComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [TextsearchComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(TextsearchComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
