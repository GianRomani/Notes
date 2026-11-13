Created: 2026-11-13 10:45
#coffee/recipe #note

This baseline **Sage Espresso Recipe** serves as the starting anchor for dialing in new specialty coffee bags on the Sage espresso machine, pairing either the **Sage integrated conical burr grinder** or the **Timemore Chestnut C3S Pro** with structured puck preparation.

---

## Equipment & Baseline Parameters

- **Machine:** Sage Espresso Machine (54mm portafilter basket)
- **Grinder & Baseline Setting:**
  - **Sage Built-in Grinder:** Step **8 – 14** (Inner burr default: 4–6; finer for light roasts, coarser for medium/dark)
  - **Timemore Chestnut C3S Pro:** **7 – 9 clicks** (Espresso range)
- **Dose ($D$):** **18.0g** (17.5g–18.5g depending on roast density)
- **Target Yield ($Y$):** **36.0g – 40.0g** liquid out (1:2 to 1:2.2 Normale ratio)
- **Water Temperature (PID):**
  - **Light Roast:** +1°C to +2°C (~94°C–95°C)
  - **Medium Roast:** Default (~93°C)
  - **Medium-Dark Roast:** -1°C to -2°C (~90°C–91°C)
- **Target Shot Time ($t$):** **26 – 32 seconds** (from pump start, including ~7–9s low-pressure pre-infusion)

---

## Step-by-Step Protocol

1. **Warm-Up Flush:** Lock the empty portafilter into the group head and run a blank shot for 5 seconds to thermally stabilize the group head, basket, and cup. Wipe the basket bone-dry.
2. **Gravimetric Dose:** Weigh **18.0g** of whole beans (single dosing) or grind directly into the portafilter on a 0.1g scale.
3. **Puck Preparation (WDT & Tamp):**
   - Use a WDT needle tool in deep circular motions from bottom to top to break all clumps and level the bed.
   - Tap the portafilter once vertically on the mat to settle grounds.
   - Tamp firmly and dead-level until the bed offers full resistance (~15kg). Apply puck screen if using.
4. **Extraction (Manual Mode Recommended):**
   - Place scale + preheated cup under the portafilter and tare.
   - Hold the brew button to engage **low-pressure pre-infusion** for **7–9 seconds** until the first drops appear across the basket bottom.
   - Release the button to ramp to full 9-bar pressure.
   - Press the button to stop the shot roughly **2.0g before target weight** (e.g., at 34.0g for a 36.0g yield) to account for residual drip.

---

## Quick Dial-In Matrix

| Roast Profile | Target Ratio | Target Yield (18g Dose) | Target Time | Typical Adjustment |
| :--- | :--- | :--- | :--- | :--- |
| **Light / Fruity** | 1:2.2 – 1:2.5 | 40g – 45g out | 28 – 34s | Finer grind, longer pre-infusion (9–10s), higher PID temp. |
| **Medium / Balanced** | 1:2.0 | 36g out | 26 – 30s | Standard 8s pre-infusion, default 93°C PID temp. |
| **Dark / Chocolatey** | 1:1.5 – 1:1.8 | 27g – 32g out | 24 – 28s | Coarser grind, shorter ratio to prevent bitter tannins. |

---

## See Also
- [[Coffee Dashboard]]
- [[Coffee/Theory/Espresso Extraction & Dialing In|Espresso Extraction & Dialing In]]
- [[Coffee/Theory/Barista Toolkit & Puck Preparation|Barista Toolkit & Puck Preparation]]
- [[Coffee/Theory/Milk Steaming & Beverage Craft|Milk Steaming & Beverage Craft]]

#### Tags
#coffee #coffee_recipe #espresso #sage #dialing_in #brewing
