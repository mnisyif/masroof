# AGENTS.md

## Project Overview
A lightweight personal expense and income tracker using Python 3.13+ with CSV storage.

## Running the App
```bash
python main.py
```

## Data File
- `expenses.csv` - Contains all transaction records with columns: timestamp, type, amount, category, item_name, description, qty, unit, store

## Important Conventions
- Amount is always the **total line cost** (not unit price × quantity)
- Type must be `Income` or `Expense` (not positive/negative numbers)
- Categories are limited: Income (Salary, Gift/Bonus, Refund), Expense (Utilities, Houseware, Groceries, Health, Hygiene, Clothes)
- Python 3.13+ required (see `.python-version`)

## Dependencies
Minimal - no external dependencies required. Uses only Python standard library (csv).