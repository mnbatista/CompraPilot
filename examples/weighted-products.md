# Weighted Products

This example demonstrates how CompraPilot handles products sold by weight, including pre-weighed meat packages and produce weighed at checkout.

## Scenario

During a real shopping trip, the cart included two different types of weighted products:

1. Meat packages with a final price already printed on the product label.
2. Fruits weighed only at checkout, without a known final price during shopping.

These scenarios require different calculation strategies.

---

## Pre-Weighed Products

The meat packages already had:

- product name;
- net weight;
- price per kilogram;
- final package price.

Because the final price was available before checkout, CompraPilot included each package in the estimated total.

### Products Registered

| Product | Expected | Charged | Difference | Status |
|---|---:|---:|---:|---|
| Beef Shank | R$ 87.60 | R$ 87.60 | R$ 0.00 | ✅ Verified |
| Beef Top Round | R$ 106.76 | R$ 106.76 | R$ 0.00 | ✅ Verified |
| Beef Bottom Round | R$ 139.67 | R$ 139.67 | R$ 0.00 | ✅ Verified |
| Beef Sirloin | R$ 114.19 | R$ 114.19 | R$ 0.00 | ✅ Verified |
| Beef Eye of Round | R$ 190.13 | R$ 190.13 | R$ 0.00 | ✅ Verified |
| Beef Tenderloin | R$ 54.57 | R$ 54.57 | R$ 0.00 | ✅ Verified |
| Beef Lagarto Cut | R$ 95.11 | R$ 95.11 | R$ 0.00 | ✅ Verified |
| Beef Shoulder | R$ 126.56 | R$ 126.56 | R$ 0.00 | ✅ Verified |
| Beef Ribs | R$ 60.10 | R$ 60.10 | R$ 0.00 | ✅ Verified |

All registered meat packages matched the amounts charged on the receipt.

---

## Products Weighed at Checkout

The shopping trip also included produce without a known final price before checkout:

- lemons;
- bananas;
- papaya;
- avocados.

CompraPilot preserved these products for later verification but excluded them from the estimated total because their final weight and price were not yet available.

### Receipt Values

| Product | Checkout weight | Charged amount |
|---|---:|---:|
| Lemons | 1.430 kg | R$ 18.45 |
| Bananas | 1.020 kg | R$ 4.07 |
| Papaya | 2.030 kg | R$ 12.16 |
| Avocados | 0.910 kg | R$ 2.72 |
| **Total** |  | **R$ 37.40** |

---

## Receipt Reconciliation

Before the weighted produce was considered, CompraPilot calculated:

```text
Estimated total: R$ 1,415.57
Receipt total: R$ 1,452.97
Initial difference: R$ 37.40
```

The initial difference matched the total amount of the products weighed at checkout:

```text
Weighted produce total: R$ 37.40
Initial difference: R$ 37.40
Remaining unexplained difference: R$ 0.00
```

CompraPilot therefore determined that the difference did not represent incorrect pricing.

---

## Result

✅ All registered shelf-label prices were verified

✅ All pre-weighed meat packages matched the receipt

✅ Products weighed at checkout were identified separately

✅ The R$ 37.40 difference was fully explained

✅ No unexpected additional items were found

✅ No pricing discrepancy was detected

✅ The final receipt total was successfully reconciled

---

## Expected CompraPilot Behavior

When processing weighted products, CompraPilot should:

1. Include a product in the estimated total when the final package price is visible.
2. Preserve a product for later verification when only the price per kilogram is known.
3. Avoid estimating a final value without a confirmed weight.
4. Identify the final weight and amount from the receipt.
5. Add checkout-weighed products to the reconciliation total.
6. Distinguish an explained difference from a pricing discrepancy.
7. Report any remaining unexplained difference separately.

---

## Key Learning

A receipt total higher than the estimated total does not always indicate incorrect pricing.

For products sold by weight, the final amount may only become available at checkout. CompraPilot must reconcile these amounts before classifying a difference as a potential pricing discrepancy.

This scenario validated CompraPilot’s ability to explain a legitimate difference instead of generating a false alert.