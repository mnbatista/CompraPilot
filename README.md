# 🛒 CompraPilot

[English](README.md) | [Português do Brasil](README.pt-BR.md)

![CompraPilot banner](assets/banner-github.png)

## Have you ever wondered if the price charged at checkout is the same as the one you saw on the shelf?

CompraPilot is an AI-powered shopping copilot built with Microsoft 365 Copilot Agent Builder.

It helps shoppers track purchases in real time, validate promotions, calculate the expected total, compare shelf prices against checkout receipts, and identify potential pricing discrepancies.

> Receipt and price verification powered by AI.

Unlike a traditional shopping list or calculator, CompraPilot preserves the context behind each price, including quantities, promotional conditions, and shelf-label evidence.

**Validated in real grocery shopping scenarios.**

---

## 🎯 The Problem

Shopping promotions are not always easy to understand.

A shelf label might include:

- a regular retail price;
- a lower price for buying multiple units;
- loyalty program requirements;
- app-exclusive discounts;
- payment method conditions;
- short-dated product discounts;
- combinations such as “buy 2, get 1 free.”

Even when the offer is understood correctly, the checkout price may not match the price shown on the shelf.

Verifying everything manually while standing in the checkout line can be slow and uncomfortable, especially when the shopper needs to find the original shelf-label photo.

CompraPilot was created to make this process more structured, transparent, and practical.

---

## 💡 The Solution

During a shopping trip, the shopper photographs the shelf label and informs the quantity placed in the cart.

CompraPilot then:

1. reads the product and pricing information;
2. interprets the promotion conditions;
3. applies the correct unit price;
4. calculates the item subtotal;
5. maintains the expected shopping total;
6. preserves the item information for later verification.

At checkout, the shopper can compare the expected total with the amount displayed by the cashier.

After payment, the shopper can submit a receipt image so CompraPilot can compare the registered prices with the amounts actually charged.

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
- ✅ Compact checkout mode
- ✅ Expected total comparison
- ✅ Receipt analysis
- ✅ Separate discount interpretation
- ✅ Potential pricing discrepancy detection

---

## 📸 How It Works

### 1. Register a shopping list

The shopper can start by submitting a list:

```text
Rice
Coffee
Milk
Toilet paper
```

CompraPilot keeps track of the planned products and identifies which items are still missing.

This step is optional. A shopping trip can also begin without a predefined list.

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

To reduce scrolling and mobile data usage, CompraPilot uses a compact response after each registered item:

```text
✅ Item registered

Sweet Coco Grated Coconut
Qty: 2
Subtotal: R$ 7.84

Total: R$ 7.84
```

The full cart is displayed only when requested or when the shopping trip is finalized.

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

CompraPilot recalculates the item and the expected total.

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
| 1 | Product A | 4 | R$ 12.50 | R$ 50.00 |
| 2 | Product B | 2 | R$ 8.00 | R$ 16.00 |

This view is designed for quick consultation while standing at checkout.

The shopper can request a specific item:

```text
Show item 2
```

CompraPilot then displays only the information associated with that item.

> The ability to display the original uploaded image again depends on the chat interface. CompraPilot never claims to show an image unless it is actually visible in the response.

---

### 8. Compare the checkout total

The shopper can provide the total displayed by the cashier:

```text
The checkout total is R$ 165.73.
```

CompraPilot compares:

```text
Expected total: R$ 154.73
Checkout total: R$ 165.73
Difference: R$ 11.00
```

A total difference indicates that further verification may be necessary, but it does not identify the responsible product without item-level checkout or receipt data.

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
- highlight potential discrepancies.

A higher gross price is not automatically considered an error. Some checkout systems record the regular price first and apply the promotion as a separate discount.

CompraPilot compares the expected amount with the **net amount charged** whenever discount information is available.

---

## 🧾 Example of Receipt Verification

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
Status: Verified
```

This prevents a separate promotional discount from being incorrectly classified as a pricing discrepancy.

---

## ✅ Validated in Real Shopping Scenarios

CompraPilot has been tested during real shopping trips.

### Environments tested

- ✅ Supermarkets
- ✅ Wholesale and retail stores

### Scenarios tested

- ✅ Shelf-label registration
- ✅ Minimum-quantity promotions
- ✅ Short-dated product discounts
- ✅ Regular and promotional price selection
- ✅ Multiple product quantities
- ✅ Item correction
- ✅ Product removal
- ✅ Shopping list tracking
- ✅ Missing item identification
- ✅ Real-time total calculation
- ✅ Checkout total comparison
- ✅ Receipt verification
- ✅ Discounts recorded separately on receipts
- ✅ Compact Checkout Mode

### Real-world finding

During an early field test, the checkout total was higher than the expected total.

The discrepancy involved a short-dated product offered at a reduced shelf price. The calculations were correct, but finding the original shelf-label image in a long conversation was difficult while the cashier was waiting.

This finding led to two important product improvements:

1. **Compact Shopping Mode**, which reduces the amount of text generated after each item.
2. **Checkout Mode**, which provides a short item table for faster verification.

This project is being improved based on real usage, not only simulated demonstrations.

---

## 🧠 Design Principles

### Accuracy before automation

CompraPilot must not invent unreadable prices, quantities, barcodes, or promotional conditions.

### Quantity is always required

CompraPilot must not silently assume that the shopper bought one unit.

### Package contents are not purchase quantity

A package containing four units is different from four packages placed in the cart.

### Net price matters

Receipt discounts must be considered before identifying a pricing discrepancy.

### Compact mobile experience

Shopping responses should remain short because the shopper may be walking through a store, using a mobile device and relying on mobile data.

### Human verification remains important

CompraPilot provides decision support. Its output should not be treated as definitive proof of incorrect charging.

---

## 🚀 Feature Status

| Feature | Status |
|---|---|
| Shelf-label photo registration | ✅ Available |
| Required quantity validation | ✅ Available |
| Simple promotional pricing | ✅ Available |
| Minimum-quantity promotions | ✅ Available |
| Shopping cart calculations | ✅ Available |
| Compact Shopping Mode | ✅ Available |
| Checkout Mode | ✅ Available |
| Shopping list tracking | ✅ Available |
| Missing item identification | ✅ Available |
| Checkout total comparison | ✅ Available |
| Receipt analysis | ✅ Available |
| Separate receipt discounts | ✅ Available |
| Original image retrieval by item | ⚠️ Interface-dependent |
| Large shopping trips with 100+ items | 🧪 Field testing |
| Savings insights | 🚧 Planned |
| Promotion value analysis | 🚧 Planned |
| Purchase history | 🔮 Future |
| Consumption profile | 🔮 Future |

---

## 📂 Repository Structure

```text
CompraPilot/
│
├── README.md
├── README.pt-BR.md
├── LICENSE
├── CHANGELOG.md
├── CONTRIBUTING.md
│
├── agent/
│   ├── descricao.md
│   ├── instrucoes.md
│   ├── prompts-sugeridos.md
│   └── configuracao-agent-builder.md
│
├── skill/
│   ├── SKILL.md
│   └── scripts/
│       └── calcular_compra.py
│
├── docs/
├── exemplos/
│
└── assets/
    ├── banner-github.png
    └── icon.png
```

---

## ⚙️ Installation

### Prerequisites

The current implementation requires:

- access to Microsoft 365 Copilot;
- access to Microsoft 365 Copilot Agent Builder;
- permission to create an agent;
- support for image attachments;
- access to custom skills and script execution in the relevant environment.

Feature and custom skill availability may vary depending on the Microsoft 365 environment, licensing, organization settings, and preview program availability.

---

### 1. Create the agent

Open Microsoft 365 Copilot Agent Builder and create a new agent named:

```text
CompraPilot
```

---

### 2. Configure the description

Copy the content from:

```text
agent/descricao.md
```

Paste it into the agent description field.

---

### 3. Configure the instructions

Copy the content from:

```text
agent/instrucoes.md
```

Paste it into the Agent Builder instructions field.

---

### 4. Add the suggested prompts

Use the prompts documented in:

```text
agent/prompts-sugeridos.md
```

---

### 5. Package the custom skill

The skill package must contain:

```text
auditoria-compras.zip
├── SKILL.md
└── scripts/
    └── calcular_compra.py
```

`SKILL.md` must be located at the root of the ZIP package.

---

### 6. Upload the skill

In Agent Builder:

1. Open the agent configuration.
2. Locate the Skills section.
3. Add a custom skill.
4. Upload `auditoria-compras.zip`.
5. Review the skill name, description, and included files.
6. Save or update the agent.

---

### 7. Run a basic test

Start with:

```text
Start shopping
```

Submit a clear shelf-label photo and provide a quantity.

Then test:

```text
Show cart
```

```text
Finalize shopping
```

```text
Checkout mode
```

```text
Show item 1
```

---

## 🧪 Recommended Test Scenarios

Before using CompraPilot in a large shopping trip, test:

1. a product with only a regular price;
2. a product with a minimum-quantity promotion;
3. a product below the promotional quantity;
4. an item correction;
5. an item removal;
6. multiple products in the same conversation;
7. checkout total comparison;
8. a receipt containing separate discounts;
9. an incomplete or unreadable receipt image.

---

## ⚠️ Current Limitations

- Shopping data is maintained in the current conversation.
- A new conversation may not recover a previous cart.
- Long shopping trips may reach context or usability limits.
- Blurred, cropped, dark, or reflective photos may reduce reading quality.
- Receipt descriptions may be abbreviated and difficult to associate.
- Original uploaded images may not be displayed again by the chat interface.
- Loyalty, app, payment-method, and membership promotions may require user confirmation.
- CompraPilot does not replace the retailer’s official pricing or customer service process.
- The project is still being tested with shopping trips containing more than 100 items.

---

## 🔒 Privacy

Before uploading a receipt, review whether it contains:

- personal identification numbers;
- payment information;
- loyalty account information;
- store membership data;
- other information that should not be shared.

CompraPilot does not require access to email, Teams messages, or unrelated organizational files for its core shopping workflow.

---

## 💡 Use Cases

### Grocery Stores

- Shelf and checkout price verification
- Promotion validation
- Real-time budget tracking
- Receipt analysis

### Wholesale and Retail Stores

- Quantity-based pricing
- Volume discounts
- Minimum-unit promotions
- Large-cart total tracking

### Pharmacies and Other Retailers

- Discount validation
- Offer comparison
- Receipt verification
- Purchase total monitoring

---

## 🗺️ Roadmap

### Version 1.0

- Shelf-label registration
- Quantity validation
- Promotional pricing
- Shopping cart calculations
- Final shopping report

### Version 1.1

- Shopping list tracking
- Missing item identification
- Compact Shopping Mode
- Checkout Mode
- Receipt verification improvements

### Version 1.2

- Large shopping trip validation
- Improved receipt reconciliation
- Better discrepancy prioritization
- Field-test metrics

### Version 1.3

- Savings insights
- Promotion value analysis
- Detection of promotions that reduce unit price but increase unnecessary spending
- Waste and expiration considerations

### Version 2.0

- Purchase history
- Consumption patterns
- Price history
- Personalized shopping recommendations

---

## 🤝 Contributing

Contributions, ideas, field-test reports, and improvement suggestions are welcome.

Before submitting a pull request, read:

```text
CONTRIBUTING.md
```

Useful contributions include:

- new promotion scenarios;
- receipt formats;
- international pricing rules;
- localization improvements;
- prompt improvements;
- calculation tests;
- accessibility and mobile UX suggestions.

---

## 🌍 Localization

The primary README is written in English to make the project accessible to an international audience.

The Brazilian Portuguese version is available here:

[Leia o README em Português do Brasil](README.pt-BR.md)

Future contributions may add other languages and regional promotion formats.

---

## 📄 👨‍💻 Author

Created by **Maycon de Novaes Batista**.

CompraPilot started as a personal experiment to answer a simple question:

> Is the price charged at checkout the same as the price shown on the shelf?

The project evolved through real shopping trips, real pricing conditions, and real checkout verification scenarios.

---

## ⚖️ Disclaimer

CompraPilot is an independent open-source community project.

It is not an official Microsoft product and is not affiliated with or endorsed by Microsoft or any retailer.

Microsoft, Microsoft 365, and Copilot are trademarks of the Microsoft group of companies.

CompraPilot provides estimates and decision support. Users should verify prices, promotions, receipts, and store policies directly with the retailer.

---

## ⭐ Support the Project

If CompraPilot helped you or inspired a real-world Copilot scenario:

- ⭐ Star the repository
- 🐛 Open an issue
- 💡 Suggest a promotion or receipt scenario
- 🧪 Share field-test feedback
- 🚀 Contribute to the project

---

**CompraPilot**

*Track your cart. Verify your receipt. Understand what you paid.*