# Project Documentation: Daily Cash Flow & Expense Tracker

## 1. Project Overview
This project is a lightweight, low-friction daily expense and income tracker. The primary philosophy is to prioritize logging consistency over extreme data normalization. It uses a "Receipt-Line" data architecture, allowing for quick entry of daily purchases, bills, and income without requiring complex unit conversions or relational tables.

## 2. Scope and Logic
* **Tracking Target:** Active Cash Flow. Only physical movement of money into or out of accounts is logged.
* **Income vs. Expense:** Calculated via a strict `type` column rather than using positive/negative floating integers. This keeps the data readable while allowing simple calculation of the remaining balance (Sum of Income - Sum of Expense).
* **The "Receipt-Line" Rule:** Items are logged exactly as they appear on a receipt. The recorded `amount` is always the total price paid for that specific line item, regardless of the quantity or unit purchased.

---

## 3. Category Framework
Categories are strictly limited to prevent data clutter. 

* **Income Categories:**
    * Salary
    * Gift / Bonus
    * Refund
* **Expense Categories:**
    * Utilities (Internet, electricity, water)
    * Houseware (Home goods, maintenance)
    * Groceries (Food and cooking supplies)
    * Health (Medical, pharmacy)
    * Hygiene (Personal care)
    * Clothes (Apparel and footwear)

---

## 4. Data Architecture (Database Schema)
The tracker relies on a single, flat table. 

| Field | Data Type | Description | Example |
| :--- | :--- | :--- | :--- |
| **`timestamp`** | Datetime | Date and time of the transaction, formatted in 24-hour time. | 2026-03-20 18:05 |
| **`type`** | String | Defines the cash flow direction. Must be `Income` or `Expense`. | Expense |
| **`amount`** | Float | The absolute total financial value of the line item. | 15.50 |
| **`category`** | String | The high-level budget bucket (from the framework above). | Groceries |
| **`item_name`** | String | Clean, descriptive name of the product or service. | Apples |
| **`qty`** | Float | The numerical quantity of the unit purchased. | 2.5 |
| **`unit`** | String | The physical metric or grouping of the item. | kg |

---

## 5. Standard Operating Procedures (Logging Examples)

**Scenario A: Standard Grocery Run**
Purchasing loose items and packed items together. The `amount` reflects the total line cost.
* `2026-03-20 18:15` | `Expense` | `8.50` | `Groceries` | `Apples` | `2.5` | `kg`
* `2026-03-20 18:15` | `Expense` | `4.00` | `Groceries` | `Eggs` | `1` | `12-pack`

**Scenario B: Monthly Bills**
Logging a recurring utility payment.
* `2026-03-01 09:00` | `Expense` | `45.00` | `Utilities` | `Internet Connection` | `1` | `month`

**Scenario C: Receiving Income**
Logging a paycheck or external funding.
* `2026-03-25 08:30` | `Income` | `1500.00` | `Salary` | `March Paycheck` | `1` | `deposit`
