import os
import csv
bank_csv = os.path.join('Resources','03-Python_Homework_Instructions_PyBank_Resources_budget_data.csv')

def budget(banks):
     print("~ file:main.py ~ line 6 ~ banks",banks)
     months = str(banks[0])
     profit = int(banks[1])
     print("~ file:main.py ~ line 10 ~ profit",profit)
     profit_inc = int(banks[1])
     print("~ file:main.py ~ line 12 ~ profit_inc",profit_inc)
     profit_dec = int(banks[1])
     num_rows = 0
     increase_month = str(banks[0])
     decrease_month = str(banks[0])
     for row in csvreader:
         num_rows +=1

     total_months = num_rows 
     total_profit = sum(profit for r in csv.reader(csv_header)) 
     profit_avg = total_profit/total_months
     for i in csvreader:
         print(" ~ file: main.py ~ line 31 ~ i", i)
         print(" ~ file: main.py ~ line 33 ~ profit", profit)
         print(" ~ file: main.py ~ line 34 ~ profit_inc", profit_inc)

         if profit > profit_inc:
            profit_inc = profit[i]
            increase_month = months[i]
         elif profit < profit_dec:
            profit_dec = profit[i]
            decrease_month = months[i]

     print("Financial Analysis")
     print("-----------------------------")
     print(f"Total Months: {total_months}")
     print(f"Total: {total_profit}")
     print(f"Average change: {profit_avg}")
     print(f"Greatest Increase in Profits: {increase_month} ({profit_inc})")
     print(f"Greatest Decrease in Profits: {decrease_month} ({profit_dec})") 

with open(bank_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader) 
    num_rows=0
    for row in csvreader:
        #print(" ~ file: main.py ~ line 40 ~ row", row)     
        budget(row)