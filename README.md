# Election_Analysis
## Project Overview 
A hypothetical Colorade Board of Election employee has given me the following tasks to complete the election audit of a recent local congressional election. 

1. Calculate the total number of votes cast. 
2. Get a complete list of candidates who received votes. 
3. Calculate the total number of cotes each candidate received. 
4. Calculate the precentage of votes each candidate won. 
5. Determine the winner of the elciton based on popular vote. 
6. Calculate the number of votes and the percentages of votes for each county. 
7. Determine which county had the largest number of votes.

## Resources 
- Data Source: election_results.csv
- Software: Python 3.10.1, Visual Studio Code 1.63.2

## Summary
The analysis of the eleciton shows that: 

- There were 369,711 votes cast in the election. 
- The candidates were: 
   - Charles Casper Stockham 
   - Diana DeGette
   - Raymon Anthony Doane 
 - The candidate results were: 
   - Charles Casper Stockham received 23.0% of the vote and 85,213 votes.
   - Diana DeGette received 73.8% of the vote and 272,892 votes. 
   - Raymon Anthony Doane received 3.1% of the vote and 11,606 votes. 
 - The winner of the election was: 
   - Diana DeGette, who received 73.8% of the vote and 272,892 votes. 

 - The county vote results were: 
   - Jefferson County recieved 10.5% of the vote and 38,855 votes.
   - Denver County received 82.8% of the vote and 306,055 votes. 
   - Arapahoe County received 6.7% of the vote and 24,801 votes.
 - The county with the largest turnout was:
   - Denver County, which received 82.8% of the vote and 306,055 votes. 

![Click here to see the results from the txt file.](https://github.com/awar2170/Election_Analysis/blob/main/analysis/election_analysis.txt)

## Challenge Overview 
The purpose of the challenge was to replicate similar code from the module to calculate the total number of votes for each county, the percentages of votes for each county, and determine which county had the largest turnout.  

This was accomplished by using a for loop with a nested if statement in python that looped through each county name in a empty python dictionary.  The first argument in the loop computes the vote counts per county, but does not assign any names for the associated counties.  The second expression calculates the percentage of the total votes for each of the associated counties from the first argument. The loop then creates a string with that outputs the name of the county along with the percentage and total votes that were calcualted in the first two arguments.  This is printed to the terminal and written to ![the analysis file](https://github.com/awar2170/Election_Analysis/blob/main/analysis/election_analysis.txt).

The nested if statement targets the county with the largest vote count and the largest percentage, by cycling through each of the votes and percentages for each county in the loop.  If one county votes is greater than the largest county vote count and that county's vote percentage is greater than the largest county's vote count, that county is replaced as the largest county turnout.  This if statement will loop through each of the counties, meaning that whichever has the largest votes and largest percentage of votes will be the county that is saved to the lg_county_turnout variable.  This is because the if statement will update with the largest votes and vote percentage value each time it loops.  Therefore, if the loop does not encounter something that beats the if conditions, it will keep the county that it deemed the largest for turnout. 

## Challenge Summary 
The purpose of this section is to provide a business proposal to the election commission on how this script can be used - with some modifications - for any election. 

### Modification 1: Reading in a Different CSV File
The first modification would be to read in a different csv file that has the correct data for the specific election.  After reading in the CSV file, you would have to make sure that it follows the same format as the ![elections_results.csv](https://github.com/awar2170/Election_Analysis/tree/main/Resources).  This means you would have to clean the data or modify the csv file so that it follows the same format of "Ballot ID" in the first column, "County" in the second column, and "Candidate" in the third column.  If the csv file does not follow this format, the code will run the analysis on the wrong columns or the code may not run at all.  

### Modificaiton 2: 
