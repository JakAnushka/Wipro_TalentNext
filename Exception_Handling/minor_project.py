'''You had saved the items and their price details in a text file, which you purchased yesterday from a nearby super market.

You need to know:

1. How many items did you purchase?

2. How many items are free?

3. What is the total amount you had to pay?

4. What is the discount amount?

5. What is the final amount did you pay after the discount?

Help yourself by writing a python code to do this, include necessary code to handle the possible exceptions.

Note:

Data is stored in a text file Purchase-1.txt.

Each line contains one item's details.

Item name and price is separated by a space.

You have to enter the file name during run time.

Sample input 1:

Purchase-1.txt

Chocolate 50

Biscuit 35
ice cream 50
(blank line)
Discount 5'''
def process_purchase_file():
    try:
        filename = input("Enter the filename: ")
        with open(filename, 'r') as file:
            lines = file.readlines()

        total_items = 0
        free_items = 0
        total_amount = 0
        discount = 0

        for line in lines:
            line = line.strip()
            if not line:
                free_items += 1
                continue

            parts = line.split()
            if len(parts) < 2:
                continue

            item = parts[0]
            try:
                price = float(parts[1])
                if item.lower() == "discount":
                    discount += price
                else:
                    total_amount += price
                    total_items += 1
            except ValueError:
                print(f"Invalid price for item: '{line}' - Skipping it.")

        final_amount = total_amount - discount

        print("\nSummary:")
        print(f"1. Total items purchased      : {total_items}")
        print(f"2. Free items                 : {free_items}")
        print(f"3. Total amount before discount: ₹{total_amount}")
        print(f"4. Discount applied            : ₹{discount}")
        print(f"5. Final amount paid           : ₹{final_amount}")

    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print("An unexpected error occurred:", str(e))

process_purchase_file()


