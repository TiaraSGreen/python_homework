#import os and csv

import os
import csv

#join path
budget_data = os.path.join("Resources", "budget_data.csv")

#open and read csv
with open(budget_data, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    header= next(csvreader)

    #make list to find net profit and loss 
    profit = []
    month =[]

    #read file and add to list

    for rows in csvreader:
        profit.append(int(rows[1]))
        month.append(rows[0])

    #make profit change list
    profit_change =[]

    #add profit/loss change to profit change list
    for x in range(1, len(profit)):
        profit_change.append((int(profit[x])- int(profit[x-1])))
    
    #formula for avg change
    avg_change = sum(profit_change)/ len(profit_change)

    #num of months length

    month_num = len(month)

    #greatest increase in profit
    great_increase = max(profit_change)

    #greatest decrease in profit

    great_decrease = min(profit_change)

    #print the final info

    print("Financial Analysis")

    print("-------------------")

    print("Total Months: " + str(month_num))

    print("Total: " + "$" + str(sum(profit)))

    print("Average change: " + "$" + str(avg_change))

    print("Greatest Increase in Profits: " + str(month[profit_change.index(max(profit_change))+1])) + " "+ "$" + str((great_increase))

    print("Greatest Decrease in Profits: " + str(month[profit_change.index(min(profit_change))+1])) + " "+ "$" + str((great_decrease))

    #write a text file containing printed information

    file = open("Analysis/bank_analysis.txt","w")
    file.write("Financial Analysis" + "\n")
    file.write("------------------" + "\n")
    file.write("Total months: " + str(month_num) + "\n"
    file.write("Average change: " + "$" + str(avg_change) + "\n")
    file.write("Greatest Increase in Profits: " + str(month[profit_change.index(max(profit_change))+1])) + " "+ "$" + str(great_increase) + "\n")
    file.write("Greatest Increase in Profits: " + str(month[profit_change.index(min(profit_change))+1])) + " "+ "$" + str((great_decrease)) + "\n")
    file.close()