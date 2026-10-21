# Real-World Validation Journey

CompraPilot has evolved through real shopping trips rather than simulated demonstrations alone.

Each field test revealed a practical need and directly influenced the agent’s behavior, instructions, and user experience.

---

## Validation Timeline

### 1. Shelf-Price Verification

CompraPilot started with a simple question:

> Is the price charged at checkout the same as the price shown on the shelf?

The first version allowed the shopper to:

1. photograph a shelf label;
2. inform the purchased quantity;
3. calculate the expected subtotal;
4. maintain an estimated shopping total;
5. compare the result with the checkout amount.

Initial tests validated:

- shelf-label interpretation;
- quantity confirmation;
- subtotal calculation;
- total calculation;
- item correction;
- item removal.

---

### 2. Minimum-Quantity Promotions

The next tests included labels containing both regular and promotional prices.

Example:

```text
Regular price: R$ 57.99
Promotional price: R$ 54.99
Minimum quantity: 3 packages
```

CompraPilot correctly applied:

```text
Quantity 2 → R$ 57.99 per package
Quantity 3 or more → R$ 54.99 per package
```

This test also validated an important distinction:

```text
Package contents: 4 units
Minimum purchase: 3 packages
```

The four units inside each package were not interpreted as the number of packages purchased.

#### Result

✅ Regular and promotional prices interpreted correctly

✅ Minimum purchase quantity validated

✅ Package contents distinguished from purchase quantity

---

### 3. Short-Dated Product Promotion

During an early real-world test, a short-dated product was advertised for:

```text
R$ 3.92 per unit
```

A substantially higher amount appeared at checkout.

The expected total calculated by CompraPilot helped reveal that a difference existed.

The shopper then needed to locate the original shelf-label photo while standing at checkout.

Although the calculation was correct, the conversation had become too long, making the evidence difficult to find quickly.

#### Product Learning

Accuracy alone was not enough.

CompraPilot also needed to support fast verification in a time-sensitive checkout situation.

---

### 4. Compact Shopping Mode

The short-dated product test led to the creation of Compact Shopping Mode.

Before this improvement, each product generated a detailed response containing:

- product information;
- regular price;
- promotional price;
- promotion rules;
- subtotal;
- accumulated total;
- full cart summary.

This created excessive scrolling during a real shopping trip.

Compact Shopping Mode reduced each response to:

```text
✅ Item registered

[Product]
Qty: [quantity]
Subtotal: R$ [value]

Total: R$ [accumulated total]
```

The full cart now appears only when requested or when the shopping trip is finalized.

#### Result

✅ Less scrolling

✅ Lower information overload

✅ Faster product registration

✅ Better experience on mobile devices

✅ More practical use with mobile data

---

### 5. Checkout Mode

The need to locate a suspicious product quickly also led to Checkout Mode.

When activated, Checkout Mode presents a compact table:

| # | Product | Qty | Unit price | Subtotal |
|---:|---|---:|---:|---:|

Products can be ordered by subtotal to help the shopper inspect items with the greatest financial impact first.

The shopper can also request:

```text
Show item 3
```

CompraPilot then returns only the relevant information:

- product;
- quantity;
- registered price;
- expected subtotal;
- promotion condition.

#### Known Limitation

Retrieving and displaying the original uploaded shelf-label image depends on the chat interface.

CompraPilot must not claim that an image was displayed unless the image is actually visible in the response.

#### Result

✅ Faster item lookup

✅ Compact checkout summary

✅ Reduced need to search the full conversation

✅ Better support during checkout verification

---

### 6. Discounts Recorded Separately on Receipts

Another field test involved a receipt where the checkout system recorded:

1. the regular product price;
2. the promotional discount on a separate line.

A higher gross price could have been incorrectly classified as a discrepancy.

CompraPilot instead compared the expected amount with the net amount charged.

Example:

```text
Expected: 2 × R$ 3.92 = R$ 7.84
Gross amount: R$ 23.18
Discount: R$ 15.34
Net amount: R$ 7.84
Difference: R$ 0.00
```

#### Result

✅ Separate discount identified

✅ Net amount calculated

✅ False discrepancy avoided

✅ Receipt item successfully verified

---

### 7. Shopping List Tracking

CompraPilot was also tested with a shopping list containing product names and quantities.

During the shopping trip, the agent:

- associated registered products with planned items;
- tracked missing products;
- preserved the requested quantities;
- reported when the shopping list was completed.

The remaining list was not displayed after every product, reducing unnecessary output.

#### Result

✅ Planned items tracked

✅ Missing products identified

✅ Quantities preserved

✅ Shopping list completion confirmed

---

### 8. Weighted Product Reconciliation

A later shopping trip included:

- pre-weighed meat packages;
- fruits weighed only at checkout.

The meat packages already displayed their final prices, so CompraPilot included them in the estimated total.

The fruits did not have final prices before checkout, so CompraPilot preserved them for receipt verification without adding estimated values.

The initial totals were:

```text
Estimated total: R$ 1,415.57
Receipt total: R$ 1,452.97
Initial difference: R$ 37.40
```

CompraPilot identified the weighted produce on the receipt:

| Product | Weight | Amount |
|---|---:|---:|
| Lemons | 1.430 kg | R$ 18.45 |
| Bananas | 1.020 kg | R$ 4.07 |
| Papaya | 2.030 kg | R$ 12.16 |
| Avocados | 0.910 kg | R$ 2.72 |
| **Total** |  | **R$ 37.40** |

The weighted product total exactly matched the initial difference.

#### Result

✅ Receipt successfully reconciled

✅ All registered shelf-label prices matched

✅ Weighted products identified correctly

✅ No unexpected additional items found

✅ No pricing discrepancy detected

✅ Final total successfully validated

---

## Validated Environments

CompraPilot has been tested in:

- ✅ Supermarkets
- ✅ Wholesale and retail stores

---

## Validated Scenarios

- ✅ Shelf-label recognition
- ✅ Required quantity confirmation
- ✅ Regular pricing
- ✅ Minimum-quantity promotions
- ✅ Short-dated product discounts
- ✅ Package-content interpretation
- ✅ Multiple product quantities
- ✅ Item correction
- ✅ Product removal
- ✅ Shopping list tracking
- ✅ Missing item identification
- ✅ Real-time total calculation
- ✅ Compact Shopping Mode
- ✅ Checkout Mode
- ✅ Checkout total comparison
- ✅ Receipt verification
- ✅ Separate receipt discounts
- ✅ Pre-weighed meat packages
- ✅ Products weighed at checkout
- ✅ Receipt reconciliation
- ✅ Legitimate difference explanation
- ✅ Pricing discrepancy detection

---

## Product Principles Learned from Field Testing

### Accuracy is not enough

The user must also be able to retrieve relevant information quickly during checkout.

### A difference is not always an error

Discounts, weighted products, and additional legitimate charges must be reconciled before reporting a discrepancy.

### Mobile responses must remain compact

Long responses create friction during shopping and make evidence more difficult to locate.

### Quantity must never be assumed

The user must confirm the number of packages placed in the cart.

### Package contents and purchase quantity are different

A package containing four units does not mean that four packages were purchased.

### Receipt verification must use net values

Separate discounts must be applied before comparing the receipt with the expected amount.

### Real usage should guide development

Compact Shopping Mode and Checkout Mode were created directly from field-test observations.

---

## Current Validation Status

| Capability | Status |
|---|---|
| Shelf-label registration | ✅ Validated |
| Quantity confirmation | ✅ Validated |
| Promotional pricing | ✅ Validated |
| Item correction and removal | ✅ Validated |
| Shopping list tracking | ✅ Validated |
| Compact Shopping Mode | ✅ Validated |
| Checkout Mode | ✅ Validated |
| Checkout total comparison | ✅ Validated |
| Receipt analysis | ✅ Validated |
| Separate receipt discounts | ✅ Validated |
| Weighted products | ✅ Validated |
| Receipt reconciliation | ✅ Validated |
| Original image retrieval | ⚠️ Interface-dependent |
| Shopping trips with more than 100 items | 🧪 Field testing |
| Savings insights | 🚧 Planned |
| Purchase history | 🔮 Future |

---

## Conclusion

CompraPilot began as a small experiment for checking whether a shelf price matched the amount charged at checkout.

Real shopping trips expanded the project into an AI-powered shopping assistant capable of:

- tracking purchases;
- interpreting promotions;
- calculating expected totals;
- supporting checkout verification;
- analyzing receipts;
- reconciling legitimate differences;
- identifying potential pricing discrepancies.

The project continues to evolve through actual shopping experiences, measurable results, and documented field-test findings.