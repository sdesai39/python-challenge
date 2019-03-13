import csv

with open("budget_data.csv",'r') as budgetdata:
    dummybudgetlist = csv.reader(budgetdata,delimiter = ',')
    budgetlist = [r for r in dummybudgetlist]
    monthlist = []
    totalchange = 0
    greatestin = ["",0]
    greatestde = ["",0]
    for row in budgetlist[1:]:
        if int(row[1]) > greatestin[1]:
            greatestin[0]=row[0]
            greatestin[1]=int(row[1])
        if int(row[1]) < greatestde[1]:
            greatestde[0]=row[0]
            greatestde[1]=int(row[1])
        monthlist.append(row[0])
        totalchange = totalchange+int(row[1])
    monthtotal = len(monthlist)
    averagechange = totalchange/monthtotal
print("Financial Analysis")
print("--------------------------")
print("Total Months: "+str(monthtotal))
print("Total: ${:,.2f}".format(totalchange))
print("Average Change: ${:,.2f}".format(averagechange))
print("Greatest increase in profits: "+greatestin[0]+" ${:,.2f}".format(greatestin[1]))
print("Greatest decrease in profits: "+greatestde[0]+" ${:,.2f}".format(greatestde[1]))

outputfile = open("Output.txt","w")
outputfile.write("Financial Analysis\n")
outputfile.write("--------------------------\n")
outputfile.write("Total Months: "+str(monthtotal)+"\n")
outputfile.write("Total: ${:,.2f}\n".format(totalchange))
outputfile.write("Average Change: ${:,.2f}\n".format(averagechange))
outputfile.write("Greatest increase in profits: "+greatestin[0]+" ${:,.2f}".format(greatestin[1])+"\n")
outputfile.write("Greatest decrease in profits: "+greatestde[0]+" ${:,.2f}".format(greatestde[1])+"\n")
outputfile.close()