# code to support the csv file type across operating systems
import os
import csv

# create list variables to hold the full csv data
allBallots = []
allCandidates = []

# create lists for the new datasets
candidates = []     #unique from allCandidates
votes = []          #counted from allBallots
pctVotes = []

polls = []

# create variables for stats
allVotes = 0

maxVotes = 0
maxName = "na"

# set variable to dynamically identify the csv data file
csvpath = os.path.join('Resources', 'election_data.csv')

# open and set variable to hold the unread contents of the file
with open(csvpath) as csvfile:

    # set single variable to hold the full and open reader contents of the csv file
    csvreader = csv.reader(csvfile, delimiter=',')

    # set variable for the header row
    csvheader = next(csvreader)

    # set the full csv data in lists ("counties" available but not used)
    for row in csvreader: 
        allBallots.append(row[0])
        allCandidates.append(row[2])
    
    # determine and set unique candidate list
    candidates = sorted(list(set(allCandidates)))

    # set variables for requested statistics
    allVotes = len(allBallots)

    # determine individual candidate votes & percentages
    for i in range(0,len(candidates)):
        votes.append(allCandidates.count(candidates[i]))
        pctVotes.append((votes[i] / allVotes) * 100)
        polls.append(f"{candidates[i]}:  {pctVotes[i]:.3f}%  ({votes[i]})")

    # determine winner's vote count
    maxVotes = max(votes)

    # index to determine winner's name
    indx = votes.index(maxVotes)
    maxName = candidates[indx]

    # show the requested statistics
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {allVotes}")
    print("-------------------------")
    for i in range(0,len(polls)):
        print(polls[i])
    print("-------------------------")
    print(f"Winner: {maxName}")
    print("-------------------------")

    # define the text file to store this data
    file = os.path.join('PyPollOutput.txt')
    
    # export the above printed items to the defined text file
    with open(file, "w") as file:
        file.write("Election Results\n")
        file.write("-------------------------\n")
        file.write(f"Total Votes: {allVotes}\n")
        file.write("-------------------------\n")
        for i in range(0,len(polls)):
            file.write(f"{polls[i]}\n")
        file.write("-------------------------\n")
        file.write(f"Winner: {maxName}\n")
        file.write("-------------------------\n")
