#import required libraries
import os
import csv
#"read" the csv file to python
budget_pth= os.path.join("C:/Users/annel/Desktop/python-challenge/PyBank/Resources/budget_data.csv")
with open(budget_pth) as csvfile:
    csv_reader=csv.reader(csvfile, delimiter=",")
#get a count of months in the budget (there is one row per month)
    listbud= list((csv_reader))
    Total_Months=((len(listbud))-1)
    print(Total_Months)
    #There are 86 months recorded in the budget data file
    
    #Sum the Profits/Losses column to get net total over entire period

    #average change in profits/losses over entire period

    #greatest increase in profits/losses (date and amount)

    #greatest decrease in profits/losses (date and amount)

    #print all the above results as you go ^^ and then "write" to a text file when done
