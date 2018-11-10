import pandas as pd
from datetime import datetime
budget_data_file = "budget_data.csv"

# Read and display the CSV with Pandas
budget_data_file_pd = pd.read_csv(budget_data_file)


budget_data_table = budget_data_file_pd[["Date", "Profit/Losses"]]

totalMonths = 0
for date in budget_data_table["Date"]:
    month = datetime.strptime(date, '%b-%Y')
    totalMonths += month.month
totalAbsValue = 0
totalIncome = 0
moneyAsInts = []
changes = 0
for i, money in enumerate(budget_data_table["Profit/Losses"]):
    if i != 0:
        changes += money - budget_data_table["Profit/Losses"][i-1]
    moneyAsInts.append(int(money))
    totalIncome += int(money)
    totalAbsValue += abs(int(money))

average = changes / len(budget_data_table["Date"])
greatestIncrease = budget_data_table.loc[budget_data_table['Profit/Losses'].idxmax()]
greatestDecrease = budget_data_table.loc[budget_data_table['Profit/Losses'].idxmin()]
f = open('output.txt', 'w')

f.write("Financial Analysis\n")
f.write("-------------------------")
f.write("\nTotal Months: " + str(len(budget_data_table["Date"])))
f.write("\nTotal: $" + str(totalIncome))
f.write("\nAverage Change: " + str(average))
f.write("\nGreatest Increase in Profits: " +
        str(greatestIncrease[0]) + " " + str(greatestIncrease[1]))
f.write("\nGreatest Decrease in Profits:  " +
        str(greatestDecrease[0]) + " " + str(greatestDecrease[1]))
f = open('output.txt', 'r')
for line in f:
    print(line)

f.close

# Financial Analysis
# ----------------------------
# Total Months: 86
# Total: $38382578
# Average  Change: $-2315.12
# Greatest Increase in Profits: Feb-2012 ($1926159)
# Greatest Decrease in Profits: Sep-2013 ($-2196167)
