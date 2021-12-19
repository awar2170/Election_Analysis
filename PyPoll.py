# Set the working directory 
import csv
import os
cwd = os.getcwd()
print("Current working directory: {0}".format(cwd))

path = 'C:/Users/adeve/Desktop/BootMaterials/Bootcamp/Module3Python'
os.chdir(path)

# Open the data file.

# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Election_Analysis/Resources", "election_results.csv")
# Open the election results and read the file.
# with open(file_to_load) as election_data:

    # Print the file object.
    # print(election_data)

# Write to Files with Python 

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("Election_Analysis/analysis", "election_analysis.txt") # Tells python where things are going to be saved 

# Total votes counter
total_votes = 0 

# Unique canidates, list 
candidate_options = []

# Candidate Votes dictionary 
candidate_votes = {}

# For the section: Finding the winning candidate 
        # We need these out of the for loops and before the open statement so that we are certain they are 0 and/or empty before we run any code here. 
    # Declare a variable that holds an empty string value for the winning candidate.
winning_candidate = ""
    # Declare a variable for the "winning count" equal to zero.
winning_count = 0
    # Declare a variable for the "winning_percentage" equal to zero.
winning_percentage = 0

# CHALLENGE VARIABLES 
county_options = []
county_votes = {}
lg_county_turnout = ""
lg_county_count = 0
lg_county_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    # HAve to make sure you do things with the election results indented under election data
    # Otherwise python things the file is closed and you're not using it 
    # for row in file_reader: 
    #     print(row)

    # #How to see the first item from each row 
    # for row in file_reader:
    #     print(row[0])

    # Read and the header row.
    headers = next(file_reader)
    # Print headers row if you want it 
    #print(headers)

# Add a vote count for each candidate.

# The total votes variable needs to be above the code where we open the file with the with open() statement
# This is because we want total_votes = 0 each time we run the file 
# IF we didn't do this, then every time we run the file, we would add to the total votes count 

# Total votes for all of the candidates 
    for row in file_reader: 
        total_votes += 1 # This is equal to number = number + 1
    # print(total_votes)
        # Print candidate name from each row 
        candidate_name = row[2]
        county_name = row[1]
        # Add the candidate name to the candidate list 
        # candidate_options.append(candidate_name)
        # If the candidate does not match any existing candidates...
        if county_name not in county_options:
            county_options.append(county_name)
            county_votes[county_name] = 0 

        if candidate_name not in candidate_options:
            # Add it to the list of candidates.
            # This works because candiate_options was a defined empty list, this just adds to the empty list if the name in the second row of the data was not already in the list 
            candidate_options.append(candidate_name)

# Get the total votes for each candidate.
    # Create a dictionary, where the key = candidate's name and the vote count = the value for that key 
    # We want that to be a part of the if statement in line 69
            candidate_votes[candidate_name] = 0 # Starts tracking the candidate's vote count 
            # This makes the dictionary look like: {"Name": 0, "Name2": 0, "Name3": 0}, so now we can do the math on the value for each key
            # This works because the candidate_votes object is an empty dictionary.  We have now filled it with keys from the candidate_name list 
            # How does Python know that the candidate_name list are the keys? 
                # It knows because each candidate_name is being assigned the value of 0, and only keys can be assigned values.
    # Now we want to add candidate votes to the candidate count 
        candidate_votes[candidate_name] += 1 # This says to add one to each of the candidate name values
        # We put this out of the if statement, but aligned with the for loop because it says that for each row that has one of the candidate names, add one to the value of that key 
        # We have all the candidate names because of the if statement above 
            # QUESTION: How would we add something along each of the candidate names? 
                # Ways to Change Keys in dictionary: https://www.geeksforgeeks.org/python-ways-to-change-keys-in-dictionary/
        county_votes[county_name] += 1

with open(file_to_save, "w") as txt_file: # the with open command tells python to open a file and "w" as txt_file
    # txt_file is the file_to_save, but the txt_file is the stand in variable for the file_to_save variable 
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n"
        f"County Votes: \n")
    print(election_results, end="")
    txt_file.write(election_results) # Why does this export onto the election analysis txt and not on the excel file? BEacuse you're printing the object onto the file, where do we define this as the file? 

# The for loop below uses the same logic and the for loop below (the candidate name and candidate votes loop)
    for county_name in county_votes: 
        votes_county = county_votes[county_name]
        vote_county_percentage = float(votes_county)/float(total_votes)*100
        county_results = (f"{county_name}: {vote_county_percentage:.1f}% ({votes_county:,})\n")
        print(county_results)
        txt_file.write(county_results)
        
        if (votes_county > lg_county_count) and (vote_county_percentage > lg_county_percentage): 
            lg_county_count = votes_county
            lg_county_percentage = vote_county_percentage
            lg_county_turnout = county_name
    lg_county_summary = (
        f"-------------------------\n"
        f"Largest County Turnout: {lg_county_turnout}\n"
        f"-------------------------\n")
    print(lg_county_summary)
    txt_file.write(lg_county_summary)

    # Determine the percentage of votes for each candidate by looping through the counts.
    # 1. Iterate through the candidate list.
    for candidate_name in candidate_votes: # remember: candidate_name = a list of unique candidate names and canidate votes is the dictionary that holds the candidate_name and the vote values 
        # 2. Retrieve vote count of a candidate.
        votes = candidate_votes[candidate_name] # This takes the total votes values from the dictionary and puts them in a list, so we basically have unnamed votes now  
        # 3. Calculate the percentage of votes.
        # We make the values floats because we want to have it as a percentage
            # Like R "as.numeric" but python has many types of numeric; this is just the one you need for this 
        vote_percentage = float(votes) / float(total_votes) * 100
        # 4. Print the candidate name and percentage of votes.
        # print(f"{candidate_name}: received {vote_percentage:.2f}% of the vote.") <- Alternate way to write the same thing as line 108
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        print(candidate_results)
            # This works because candidate_name is a unique list of the candidate names, and the vote_percentage is what we calculated before 
            # This is in a for loop, so it is going to loop for each candidate_name in the dictionary of candidate votes, we want to do this thing
            # That's why it will run for each candidate 
        txt_file.write(candidate_results)

    # Find the winning canidate, vote count, and percentage 

        # Determine winning vote count and candidate
        # Determine if the votes is greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # And, set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
    # print(f"{winning_candidate} won with {winning_count} votes, which is {winning_percentage:.2f}% of the total vote")
