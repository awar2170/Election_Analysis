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
file_to_save = os.path.join("Election_Analysis/analysis", "election_analysis.txt")

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

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)

# Add a vote count for each candidate.
# Get the total votes for each candidate.
# Get the total votes cast for the election.
