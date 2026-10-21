# 🛒 CompraPilot

[English](README.md) | [Português do Brasil](README.pt-BR.md)

![CompraPilot banner](assets/banner-github.png)

## Have you ever wondered if the price charged at checkout is the same as the one you saw on the shelf?

**CompraPilot** is an AI-powered shopping copilot built with Microsoft 365 Copilot Agent Builder.

It helps shoppers track purchases in real time, validate promotions, calculate the expected total, compare shelf prices against checkout receipts, and identify potential pricing discrepancies.

> **AI-powered receipt and price verification.**

Unlike a traditional shopping list or calculator, CompraPilot preserves the context behind each price, including quantities, promotional conditions, and shelf-label information.

**Validated in real shopping and receipt reconciliation scenarios.**

---

## 🎯 The Problem

Shopping promotions are not always easy to understand.

A shelf label may include:

- a regular retail price;
- a lower price for buying multiple units;
- loyalty program requirements;
- app-exclusive discounts;
- payment method conditions;
- short-dated product discounts;
- offers such as “buy 2, get 1 free.”

Even when the offer is understood correctly, the checkout price may not match the price shown on the shelf.

Verifying everything manually while standing in the checkout line can be slow and uncomfortable, especially when the shopper needs to find the original product information quickly.

CompraPilot was created to make this process more structured, transparent, and practical.

---

## 💡 The Solution

During a shopping trip, the shopper photographs the shelf label and informs the quantity placed in the cart.

CompraPilot then:

1. reads the product and pricing information;
2. interprets the promotional conditions;
3. applies the appropriate unit price;
4. calculates the item subtotal;
5. maintains the expected shopping total;
6. preserves the item information for later verification.

At checkout, the shopper can compare the expected total with the amount displayed by the cashier.

After payment, the shopper can submit a receipt image so CompraPilot can compare the registered prices with the amounts actually charged.

CompraPilot also distinguishes between:

- actual pricing discrepancies;
- discounts recorded separately on the receipt;
- legitimate differences caused by weighted products;
- additional items that were not included in the original estimate.

---

## ✨ Key Features

- ✅ Shelf-label recognition from photos
- ✅ Required quantity confirmation
- ✅ Regular and promotional price interpretation
- ✅ Minimum-quantity promotion validation
- ✅ Real-time subtotal and total calculation
- ✅ Compact responses during shopping
- ✅ Shopping list tracking
- ✅ Missing item identification
- ✅ Item correction and removal
- ✅ Compact Checkout Mode
- ✅ Expected total comparison
- ✅ Receipt analysis
- ✅ Separate discount interpretation
- ✅ Weighted product reconciliation
- ✅ Potential pricing discrepancy detection
- ✅ Legitimate difference explanation

---

## 📸 How It Works

### 1. Register a shopping list

The shopper can begin by submitting a list:

```text
Rice
Coffee
Milk
Toilet paper
```

CompraPilot tracks the planned products and identifies which items are still missing.

This step is optional. A shopping trip can begin without a predefined list.

---

### 2. Start a shopping trip

```text
Start shopping
```

CompraPilot creates a new empty cart and clears calculations from the previous shopping trip.

---

### 3. Register shelf labels

The shopper submits a shelf-label photo and informs the quantity:

```text
Quantity: 3
```

CompraPilot attempts to extract:

- product name;
- brand;
- package size;
- barcode, when visible;
- regular price;
- promotional price;
- minimum promotional quantity;
- additional promotion conditions;
- offer validity, when visible.

If the quantity is missing, CompraPilot asks for it instead of assuming one unit.

---

### 4. Track spending with compact responses

To reduce scrolling, information overload, and mobile data usage, CompraPilot uses a compact response after each registered item:

```text
✅ Item registered

Sweet Coco Grated Coconut
Qty: 2
Subtotal: R$ 7.84

Total: R$ 7.84
```

The full cart appears only when requested or when the shopping trip is finalized.

---

### 5. Correct or remove products

The shopper can update the cart using natural-language commands:

```text
Change the rice quantity to 3.
```

```text
Remove the coffee.
```

```text
The correct price is R$ 18.90.
```

CompraPilot recalculates the affected item and the expected total.

---

### 6. Finalize the shopping trip

```text
Finalize shopping
```

CompraPilot presents a compact report containing:

- item number;
- product;
- quantity;
- applied unit price;
- promotion condition;
- subtotal;
- expected total;
- missing shopping-list items.

---

### 7. Use Checkout Mode

When the shopper says:

```text
Checkout mode
```

CompraPilot displays a compact table ordered by financial impact:

| # | Product | Qty | Unit price | Subtotal |
|---:|---|---:|---:|---:|
| 1 | Product A | 4 | $12.50 | $50.00 |
| 2 | Product B | 2 | $8.00 | $16.00 |

This view is designed for fast consultation while standing at checkout.

The shopper can request a specific item:

```text
Show item 2
```

CompraPilot then displays only the information associated with that item.

> Displaying the original uploaded shelf-label image again depends on the chat interface. CompraPilot never claims to display an image unless it is actually visible in the response.

---

### 8. Compare the checkout total

The shopper can provide the total displayed by the cashier:

```text
The checkout total is $165.73.
```

CompraPilot compares:

```text
Expected total: $154.73
Checkout total: $165.73
Difference: $11.00
```

A total difference indicates that further verification may be necessary.

However, CompraPilot does not assign the difference to a specific product without item-level checkout or receipt data.

---

### 9. Analyze the receipt

After payment, the shopper can submit a receipt photo.

CompraPilot attempts to:

- extract receipt items;
- identify quantities;
- read unit prices;
- identify separate discounts;
- compare net charged amounts with expected amounts;
- detect missing or additional items;
- reconcile weighted products;
- highlight potential pricing discrepancies.

A higher gross price is not automatically considered an error.

Some checkout systems record the regular price first and apply the promotional discount on a separate line. CompraPilot compares the expected amount with the **net amount charged** whenever discount information is available.

---

## 🧾 Receipt Verification Example

Suppose the expected price is:

```text
2 × R$ 3.92 = R$ 7.84
```

The receipt shows:

```text
Gross amount: R$ 23.18
Discount: R$ 15.34
Net amount: R$ 7.84
```

CompraPilot should classify the item as:

```text
Difference: R$ 0.00
