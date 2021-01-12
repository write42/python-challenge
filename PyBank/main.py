import os
import csv
bank_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')
analysis_file = os.path.join('Analysis','PyBank_analysis.txt')
num_rows = 0

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader) 
    total_profit = 0
    profits = []
    date = []
    profits_change = []
    profit_change = 0
    for row in csvreader:
        num_rows +=1
        date.append(row[0])
        profits.append(float(row[1]))

    for i in range(1,len(profits)):
        profits_change.append(profits[i]-profits[i-1])
        avg_change = sum(profits_change)/len(profits_change)
        max_avg_change = max(profits_change)
        min_avg_change = min(profits_change)
        max_date = str(date[profits_change.index(max(profits_change))])
        min_date = str(date[profits_change.index(min(profits_change))])

report = f"""
Financial Analysis
------------------------
Total Months: {num_rows}
Total: {sum(profits)}
Average Change: {avg_change}
Greatest Increase in Profits: {max_date} ({max_avg_change})
eatest Decrease in Profits: {min_date} ({min_avg_change})
"""
print("Financial Analysis")
print("------------------------")
print(f"Total Months: {num_rows}")
print(f"Total: {sum(profits)}")
print(f"Average Change: {avg_change}")
print(f"Greatest Increase in Profits: {max_date} ({max_avg_change})")
print(f"Greatest Decrease in Profits: {min_date} ({min_avg_change})")
with open(analysis_file, 'w') as f:
    f.write(report)