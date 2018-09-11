import os
import csv
csvpath = os.path.join('', 'Resources', 'budget_data.csv')
with open(csvpath, newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csvfile)

    total_months = 2
    total_revenue = 0
    prev_revenue = 0
    maximum = ["", 0]
    minimum = ["", 9999999999999999999]

    for counter, row in enumerate(csvreader):
        if counter > 0:
            # read only the first row after header
            break
        # prints first value
        first_value = row[1]

    for row in csvreader:
        total_months = total_months + 1
        total_revenue += int(row[1])
         # Track the revenue change
        revenue_change = int(row[1]) - prev_revenue
        prev_revenue = int(row[1])
        last_value = int(row[1])

        # Calculate the greatest increase
        if (revenue_change > maximum[1]):
            # capture date
            maximum[0] = row[0]
            maximum[1] = revenue_change

        # Calculate the greatest decrease
        if (revenue_change < minimum[1]):
            # capture date
            minimum[0] = row[0]
            minimum[1] = revenue_change

    revenue_avg = str((int(last_value) - int(first_value)) / int(total_months - 1))
    print("Financial Analysis")
    print("----------------------------")
    print("Total Months: " + str(total_months))
    print("Total: $" + str(total_revenue))
    print("Average Change: $" + str(revenue_avg))
    print("Greatest Increase in Profits: $" + str(maximum))
    print("Greatest Decrease in Profits: $" + str(minimum))


    # Generate Output Summary
output = (
    f"\nFinancial Analysis\n"
    f"----------------------------\n"
    f"Total Months: {total_months}\n"
    f"Total Revenue: ${total_revenue}\n"
    f"Average Revenue Change: ${revenue_avg}\n"
    f"Greatest Increase in Revenue: {maximum[0]} (${maximum[1]})\n"
    f"Greatest Decrease in Revenue: {minimum[0]} (${minimum[1]})\n")


# Print the output (to terminal)
print(output)

# save the output file path
output_file = os.path.join("output.txt")

# Export the results to text file
with open(output_file, "w") as txt_file:
    txt_file.write(output)
