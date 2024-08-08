# code to support the csv file type across operating systems
import os
import csv

# set variable to dynamically identify the csv data file
csvpath = os.path.join('Resources', 'budget_data.csv')

# set variables to hold the column lists
dates = []
PnL = []

# create a dictionary for the csv data
profits = {}
profits = dict()

# open and set variable to hold the unread contents of the file
with open(csvpath) as csvfile:

    # set single variable to hold the full and open reader contents of the csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # set and display variable for the header row
    csvheader = next(csvreader)
    print(f"CSV Header: {csvheader}")

    # add the the list data into the variables from above
    for row in csvreader: 
        dates.append(row[0])
        PnL.append(int(row[1]))

    # add lists to the dictionary
    profits ["Date"] = dates
    profits ["Profit/Loss"] = PnL

    print(profits)

    # totalDates = len(dates)
    # totalPnL = sum(PnL)
    # averageChange = totalPnL/len(PnL)

    # print(f"Total months: {totalDates}.")
    # print(f"Total: {totalPnL}.")
    # print(f"Average Change: {averageChange}")
    # print(f"Greatest Increase in Profits: {totalPnL} ({totalPnL})")
    # print(f"Greatest Decrease...")
    



    #The total number of months included in the dataset

    #The net total amount of "Profit/Losses" over the entire period

    #The changes in "Profit/Losses" over the entire period, and then the average of those changes

    #The greatest increase in profits (date and amount) over the entire period

    #The greatest decrease in profits (date and amount) over the entire period

