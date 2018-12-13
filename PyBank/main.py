import os
import csv

csvpath = os.path.join("Resources", "budget_data.csv")
months = []
totals = []
changes = []

with open(csvpath, newline="") as csvfile:
	csvreader = csv.reader(csvfile, delimiter=",")
	next(csvreader)

	for row in csvreader:
		months.append(row[0])
		totals.append(float(row[1]))

totalmonths = (len(months))
profit = int((sum(totals)))

for i in range (1, len(months)):
	changes.append(totals[i] - totals[i-1])

avgchange = round(sum(changes)/len(changes), 2)
maxincrease = int(max(changes))
maxincreasemonth = str(months[((changes.index(maxincrease))+1)])
maxdecrease = int(min(changes))
maxdecreasemonth = str(months[((changes.index(maxdecrease))+1)])

print(f"Financial Analysis")
print(f"-------------------")
print(f"Total Months: {totalmonths}")
print(f"Total: ${profit}")
print(f"Average Change: ${avgchange}")
print(f"Greatest Increase in Profits: {maxincreasemonth} (${maxincrease})")
print(f"Greatest Decrease in Profits: {maxdecreasemonth} (${maxdecrease})")

outputpath = os.path.join("output.txt")

with open(outputpath, 'w', newline='') as txtfile:
	txtfile.write("Financial Analysis")
	txtfile.write("\nTotal Months: " + str(totalmonths))
	txtfile.write("\nTotal: $" + str(profit))
	txtfile.write("\nAverage Change: $" + str(avgchange))
	txtfile.write("\nGreatest Increase in Profits: " + str(maxincreasemonth) + " ($" + str(maxincrease) + ")")
	txtfile.write("\nGreatest Decrease in Profits: " + str(maxdecreasemonth) + " ($" + str(maxdecrease) + ")")
	txtfile.close()