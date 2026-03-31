# from tracker import add_entry
import csv

def add_entry(entry):
    time, trans_type, trans_amount, trans_cat, item_name, desc, qty, unit, store = entry

    with open('expenses.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([time, trans_type, trans_amount, trans_cat, item_name, desc, qty, unit, store])

    print("Successfully logged!")

def main():
    print("Hello to masroof")
    print("This is where you make a change in your life")
    print("--------------------------------------------\n")

    time = str(input("Enter the time of the transaction: "))
    trans_type = str(input("What type is it, Expense or Income?: "))
    trans_amount = float(input("How much did this item cost?: "))
    trans_cat = str(input("What is the category of this item?: "))
    item_name = str(input("What is the name of this item?: "))
    desc = str(input("Add a description to the item, if necessary: "))
    qty = float(input("How many of this item did you get?: "))
    unit = str(input("Was it in kg, lb, piece, pack?: "))
    store = str(input("Where did you get it from?: "))

    entry = (time, trans_type, trans_amount, trans_cat, item_name, desc, qty, unit,store)
    add_entry(entry)

if __name__ == "__main__":
    main()
