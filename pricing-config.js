// User-provided preliminary Euro/m² base rates and multipliers.
// These are estimates only; the final quote depends on site measurements and confirmed scope.
window.ODER_PRICING = {
  basePriceEUR: {
    kitchen: 350,
    living_room: 250,
    kids_room: 200,
    flooring: 80,
    full_house: 450,
    extreme: 800
  },
  qualityMultiplier: {
    standard: 1.00,
    premium: 1.45,
    luxury: 2.20
  },
  countryMultiplier: {
    TR: 1.00,
    BG: 1.25, GR: 1.30, RS: 1.25, MK: 1.20, AL: 1.25,
    XK: 1.25, BA: 1.25, ME: 1.25, RO: 1.30, HR: 1.35, SI: 1.40,
    PL: 1.35, CZ: 1.40, SK: 1.40, HU: 1.35, LT: 1.35, LV: 1.35, EE: 1.40,
    DE: 1.55, AT: 1.55, NL: 1.60, BE: 1.60, LU: 1.65, FR: 1.60,
    IT: 1.50, ES: 1.50, PT: 1.50, CH: 1.75, GB: 1.65, IE: 1.65,
    DK: 1.65, SE: 1.60, NO: 1.70, FI: 1.65, IS: 1.75,
    MC: 2.00, AD: 1.60, LI: 1.75, SM: 1.50
  },
  rangeMargin: 0.15,
  extremeConsultancyAreaThreshold: 100,
  extremeConsultancyMultiplier: 1.10
};
