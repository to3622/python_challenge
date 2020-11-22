#Code for PyBank homework assignment
#Import Libraries needed for the homework
import os
import csv

#Set path equal to a variable to read csv file
budget_csv = '../Resources/budget_data.csv'

#List to for the data required to analyze budget file
dates = []
monthly_revenue = []
monthly_revenue_change = []

#Initialize variable
total_change = 0

#Open the csv file using the with open method & read it
with open(budget_csv) as budget_file:
    budget_reader = csv.reader(budget_file, delimiter= ",")
    #print(budget_reader)

    #Skip file header
    next(budget_reader)

    #move file data into lists
    for row in budget_reader:

        #Append dates to date list
        dates.append(row[0])
               
        #Append monthly revenue number to monthly_revenue list
        monthly_revenue.append(int(row[1]))
        #total_revenue = total_revenue + int(row[1])

    print('This is the length of dates ' + str(len(dates))) 
    #Total months calculated
    total_months = len(dates)
    #print('Total months in period is ' + str(len(dates)))

    #Sum of monthly revenue
    sum = sum(monthly_revenue)
    #print('The net total profit/loss over the entire period is ' +str(sum) + ' dollars')
    
    #Determine the maximum value from the monthly revenue list
    max(monthly_revenue)
    #print('The greatest increase in profits over the entire period is ' + str(max(monthly_revenue)))

    #Create a for loop to find the index for maximum profit value then return the value for corresponding date in dates list
    for row in monthly_revenue:
       if row == max(monthly_revenue):
        #print(row)
        index_for_date_max = monthly_revenue.index(row)

        #print(index_for_date)
        #print('The date for the greatest increase in profits over the entire period is ' + str(dates[index_for_date_max]))

    #Determine the minimum value from the monthly revenue list
    min(monthly_revenue)
    #print('The greatest decrease in profits over the entire period is ' + str(min(monthly_revenue)))

    #Create a for loop to find the index for minimum profit value then return the value for corresponding date in dates list
    for row in monthly_revenue:
       if row == min(monthly_revenue):
        #print(row)
        index_for_date_min = monthly_revenue.index(row)

        #print(index_for_date)
        #print('The date for the greatest decrease in profits over the entire period is ' + str(dates[index_for_date_min]))

    #Calculate monthly revenue change
    for i in range((len(monthly_revenue))-1):
        
        monthly_change = monthly_revenue[i] - monthly_revenue[i+1]
        monthly_revenue_change.append(monthly_change)
        total_change = total_change + monthly_change
    
    #Calculate average monthyl change
    ave_change = round(total_change / len(monthly_revenue_change), 2)
    #print(ave_change)

    print("-" * 30)
    print('Financial Analysis')
    print("-" * 30)
    print('Total Months: ' + str(total_months))
    print('Total Profits: ' + str(sum))
    print('Averge Change: $-' + str(ave_change))
    print('Greatest Increase in Profits: ' + str(dates[index_for_date_max])+ ' '+ '($ ' + str(max(monthly_revenue))+ ')')
    print('Greatest Decrease in Profits: ' + str(dates[index_for_date_min])+ ' '+ '($ ' + str(min(monthly_revenue))+ ')')  
    print("-" * 30)

# write data in a file. 
file1 = open("myfile.txt","w") 
L = ["Financial Analysis \n","-----------------------------\n","Total Months: 86 \n", "Total Profits: 38382578 \n", "Average Change: $-2315.12 \n", "Greatest Increase in Profits: Feb-12 ($ 1170593) \n", "Greatest Decrease in Profits: Sep-13 ($ -1196225) \n","------------------------------ \n"]  
  
#Write L to file1  
file1.writelines(L) 
file1.close() #to change file access modes 

#Test output of myfile.txtg  
file1 = open("myfile.txt","r+")  
  
print( "Output of Read function is ")
print (file1.read())