# Reflection 1:
# Excel is useful for quickly viewing data, sorting it, and making manual changes.
# Python makes repeatable tasks easier because a script can process many files the same way, while Excel is more visual for exploring a file.
#
# Reflection 2:
# A business could add a line to a log each time it generates a sales report, recording the time and total revenue.
# Append mode keeps the earlier entries, so the business can review a history of report runs.
#
# AI use: ChatGPT helped me draft and understand parts of this script.

import csv
from datetime import datetime
from pathlib import Path


sales_file = Path("data/sales.csv")
cleaned_file = Path("data/cleaned.csv")
log_file = Path("data/run_log.txt")


# Exercise 1: Check the CSV file and its structure
with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    data_rows = list(reader)

print("Exercise 1: File check")
print("Header:", header)
print("Number of data rows:", len(data_rows))


# Exercise 2: Read and print every raw row, including the header
print("\nExercise 2: Raw rows")
with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)


# Exercise 3: Print the header separately, then print the data rows
print("\nExercise 3: Header and data rows")
with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    header = next(reader)
    print("Header:", header)

    for row in reader:
        print(row)


# Exercise 4: Compute each order total and the overall revenue
print("\nExercise 4: Order totals")
total_revenue = 0.0

with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)  # Skip the header

    for row in reader:
        product = row[0]
        price = float(row[1])
        quantity = int(row[2])
        order_total = price * quantity
        total_revenue += order_total

        print(
            f"{product}: {quantity} units × "
            f"${price:.2f} = ${order_total:.2f}"
        )

print(f"Total revenue: ${total_revenue:.2f}")


# Exercise 5: Write only orders with a total greater than $100
original_count = 0
written_count = 0

with open(sales_file, "r", newline="", encoding="utf-8") as input_file:
    reader = csv.reader(input_file)
    next(reader)  # Skip the header

    with open(cleaned_file, "w", newline="", encoding="utf-8") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["Product", "Price", "Qty", "Total"])

        for row in reader:
            original_count += 1
            product = row[0]
            price = float(row[1])
            quantity = int(row[2])
            order_total = price * quantity

            if order_total > 100:
                writer.writerow(
                    [product, f"{price:.2f}", quantity, f"{order_total:.2f}"]
                )
                written_count += 1

print("\nExercise 5: Cleaned file")
print(f"Rows written: {written_count}")
print(f"Rows in original: {original_count}")


# Exercise 6: Use DictReader to access values by their column names
# csv.reader uses numeric indexes and works well when the column order is fixed.
# DictReader uses column names, which can make code easier to read and maintain.
dict_reader_total = 0.0

with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        price = float(row["price"])
        quantity = int(row["quantity"])
        dict_reader_total += price * quantity

print("\nExercise 6: DictReader total")
print(f"DictReader total revenue: ${dict_reader_total:.2f}")
print(f"Matches Exercise 4: {abs(dict_reader_total - total_revenue) < 0.005}")


# Exercise 7: Summarize revenue by product
product_totals = {}

with open(sales_file, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        product = row["product"]
        price = float(row["price"])
        quantity = int(row["quantity"])
        order_total = price * quantity

        if product not in product_totals:
            product_totals[product] = 0.0

        product_totals[product] += order_total

print("\nExercise 7: Revenue by product")
for product in sorted(product_totals):
    print(f"{product}: ${product_totals[product]:.2f}")


# Exercise 8: Append this run's timestamp and total revenue to the log
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

with open(log_file, "a", encoding="utf-8") as file:
    file.write(f"{timestamp} | Total revenue: ${total_revenue:.2f}\n")

print(f"\nExercise 8: Added this run to {log_file}")