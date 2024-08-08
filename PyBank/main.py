# code to support the csv file type across operating systems
import os
import csv

# create list variables to hold the full csv data
dates = []
PnL = []
change = []

# create variables for min and max, with dates
upDate = "na"
downDate = "na"

upChange = 0
downChange = 0

# set variable to dynamically identify the csv data file
csvpath = os.path.join('Resources', 'budget_data.csv')

# open and set variable to hold the unread contents of the file
with open(csvpath) as csvfile:

    # set single variable to hold the full and open reader contents of the csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # set variable for the header row
    csvheader = next(csvreader)

    # set the full csv data in lists
    for row in csvreader: 
        dates.append(row[0])
        PnL.append(int(row[1]))

    # find changes between rows
    for i in range(0,len(PnL)):
        change.append(PnL[i] - PnL[i-1])
        
    # find min and max changes
    upChange = max(change)
    downChange = min(change)

    # calculate the requested statistics
    totalDates = len(dates)
    totalPnL = sum(PnL)
    averageChange = sum(change[1:len(PnL)])/len(change[1:len(PnL)])

    # index the rows to determine max and min dates
    indexMax = change.index(upChange)
    upDate = dates[indexMax]

    indexMin = change.index(downChange)
    downDate = dates[indexMin]

    # show the requested statistics
    print("Financial Analysis")
    print("----------------------------")
    print(f"Total months: {totalDates}")
    print(f"Total: {totalPnL}")
    print(f"Average Change: ${averageChange:,.2f}")
    print(f"Greatest Increase in Profits: {upDate} (${upChange})")
    print(f"Greatest Decrease in Profits: {downDate} (${downChange})")

    # define the text file to store this data
    file = os.path.join('PyBankOutput.txt')

    # export the above printed items to the defined text file
    with open(file, "w") as file:
        file.write("Financial Analysis\n")
        file.write("----------------------------\n")
        file.write(f"Total months: {totalDates}\n")
        file.write(f"Total: {totalPnL}\n")
        file.write(f"Average Change: ${averageChange:,.2f}\n")
        file.write(f"Greatest Increase in Profits: {upDate} (${upChange})\n")
        file.write(f"Greatest Decrease in Profits: {downDate} (${downChange})")
