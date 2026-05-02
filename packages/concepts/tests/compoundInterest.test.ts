import { describe, expect, it } from 'vitest';
import { compoundInterest } from '../src/compoundInterest.js';

describe('compoundInterest', () => {
  it('computes annual compounding', () => {
    expect(compoundInterest(1000, 0.05, 1, 2)).toBeCloseTo(1102.5, 6);
  });
});
