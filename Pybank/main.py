import os

import csv

#Define path to budget_data csv
budget_csv = os.path.join('..', 'Assignment 3', 'challenge3-python', 'Resources', 'budget_data.csv')

#Read budget_data file
with open(budget_csv, encoding='utf') as budgetfile:
    csvreader = csv.reader(budgetfile, delimiter=',')
    next(budgetfile, None) #To not count the header in calculations

# Define variables for the for loop
    totalmonths = 0
    net_profit_loss = 0
    last_value = 0
    diff_net_profit = 0
    changes_in_net_profit = []
    changes_in_net_profit_months = []
    

# For loops for total month, net profit/loss, changes in profit/loss over entire period, greatest increase and greatest decrease
    for row in csvreader:

#Calculates total months and net profit/loss
        totalmonths = totalmonths + 1
        net_profit_loss = net_profit_loss + int(row[1])
       

#Creates a list of changes in net profit using the for loop        
        diff_net_profit = int(row[1]) - int(last_value)
        changes_in_net_profit.append(diff_net_profit)
        last_value = row[1]

        changes_in_net_profit_months.append(row[0])


# Removes first month and first month value from the list of changes in net profit, then caculates the average and rounds to 2 decimal places
    del changes_in_net_profit[0]
    average_change_in_profit = round(sum(changes_in_net_profit)/len(changes_in_net_profit), 2)

    changes_in_net_profit_months.remove(changes_in_net_profit_months[0])

    changes_zip = zip(changes_in_net_profit_months, changes_in_net_profit)

    print(changes_zip)

    greatest_profit = 0
    greatest_loss = 0

    for change in changes_zip:
         if greatest_profit < int(change[1]):
             greatest_profit = int(change[1])
             greatest_profit_month = change[0]
        
         if greatest_loss > int(change[1]):
             greatest_loss = int(change[1])
             greatest_loss_month = change[0]

    print("Financial Analysis")

    print("-------------------------------------------------")

    print(f'Total Months: {totalmonths}')
    print(f'Net: ${net_profit_loss}')
    print(f'Average Change: ${average_change_in_profit}') 
    print(f'Greatest Increase in Profits: {greatest_profit_month} (${greatest_profit})')
    print(f'Greatest Increase in Profits: {greatest_loss_month} (${greatest_loss})')    
