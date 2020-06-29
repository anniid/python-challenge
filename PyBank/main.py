#import required libraries
import os
import csv
#"read" the csv file to python and setup output
budget_pth= os.path.join("C:/Users/annel/Desktop/python-challenge/PyBank/Resources/budget_data.csv")
txtOutput=os.path.join("C:/Users/annel/Desktop/python-challenge/PyBank/Analysis/budget_analysis.txt")
#track variables
Total_Months=0
previous_rev=0
rev_change=0
change_month=[]
rev_change_list=[]
gt_increase=["",0] #so it starts at the beinning month and anything >0
gt_decrease=["",9999999999999999999] #so it tracks the whichever month and anything < the second number
net_total=0
with open(budget_pth) as budget_data:
    csv_reader=csv.DictReader(budget_data)
    #loop thru rows to sum things
    for row in csv_reader:
        #update variables as they change
        Total_Months=Total_Months+1
        net_total=net_total+int(row["Profit/Losses"])
        rev_change=int(row["Profit/Losses"])-previous_rev
        previous_rev=int(row["Profit/Losses"])
        rev_change_list=rev_change_list+[rev_change]
        change_month=change_month+[row["Date"]]
            #track greatest increase and decrease
        if (rev_change>gt_increase[1]):
            gt_increase[0]=row["Date"]
            gt_increase[1]=rev_change
        if (rev_change<gt_decrease[1]):
            gt_decrease[0]=row["Date"]
            gt_decrease[1]=rev_change

#avg change in revenue
average_rev=sum(rev_change_list)/len(rev_change_list)


#print all the above results and then "write" to a text file
output=(
    f"\nFinancial Analysis\n"
    f"--------------------------------\n"
    f"Total Months: {Total_Months}\n"
    f"Net Total: ${net_total}\n"
    f"Average Change in Revenue: ${average_rev}\n"
    f"Greatest Increase in Revenue: {gt_increase[0]} (${gt_increase[1]})\n"
    f"Greatest Decrease in Revenue: {gt_decrease[0]} (${gt_decrease[1]})\n"
)
print(output)

with open(txtOutput,"w") as txtFile:
    txtFile.write(output)