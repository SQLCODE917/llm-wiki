export function compoundInterest(
  principal: number,
  annualRate: number,
  compoundsPerYear: number,
  years: number
): number {
  return principal * (1 + annualRate / compoundsPerYear) ** (compoundsPerYear * years);
}
