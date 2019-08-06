import os
import csv

    
months = 0
revenue = 0
previous_month = 0
previous_month_revenue = 0
revenue_change = 0
revenue_changes = []

csvpath = os.path.join('budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')

    rows = [r for r in csvreader]
    
    revenue_change = int(rows[1][1])
    max = rows[1]
    min = rows[1]
    for i in range(1,len(rows)):
        
        months = months + 1
        row = rows[i]
        revenue = int(row[1]) + revenue
        
        if i > 1:
            revenue_change = revenue_change + int(row[1])-int(rows[i-1][1])
        if int(max[1]) < int(row[1]):
            max = row
        
        if int(min[1]) > int(row[1]):
            min = row
           

average= int(revenue /months)
average_revenue_change = int(revenue_change/months)

#Print the Outputs
print("Financial Analysis")
print("------------------")
print("Total Months: " + str(months))
print("Total: " +"$" + str(revenue))       
print("Average Change: " +"$"+ str(average_revenue_change))
print("Greatest Increase in Revenue:" + str(max[0])+" ($" + str(max[1])+")")
print("Greatest Decrease in Revenue:" + str(min[0])+" ($" + str(min[1])+")")

with open('financial_analysis.txt', 'w') as text:
    text.write("----------------------------------------------------------\n")
    text.write("  Financial Analysis"+ "\n")
    text.write("----------------------------------------------------------\n\n")
    text.write("    Total Months: " + str(months) + "\n")
    text.write("    Total Profits: " + "$" + str(revenue) +"\n")
    text.write("    Average Change: " + '$' + str(int(average_revenue_change)) + "\n")
    text.write("    Greatest Increase in Profits: " + str(max[0]) + " ($" + str(max[1]) + ")\n")
    text.write("    Greatest Decrease in Profits: " + str(min[0]) + " ($" + str(min[1]) + ")\n")
    text.write("----------------------------------------------------------\n")
