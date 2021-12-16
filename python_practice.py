# Lists 
counties = ["Arapahoe", "Denver", "Jefferson"]
# List lengths 
len(counties)
# Slice Lists 
counties[0:2]
#Adding Items to a list
counties.append("El Paso")
# Adding Items to a List in a specific spot 
counties.insert(2, "El Paso")
counties
# Removing items from a list 
counties.remove("El Paso")
counties
# Removing items from a list in a certain index 
counties.pop(3) # Removes the 3rd indexed item from the counties list 
## Alternate ways to remove the 3rd indexed item from the counties list 
## counties.pop(3)
counties
#Changing an Element in a List 
counties.insert(2, "El Paso")
counties.remove("Arapahoe")
counties
order = [1,2,0]
counties = [counties[i] for i in order]
counties
counties.append("Arapahoe")
counties


print("Hello World")
# Tuples
counties_tuple = ("Arapahoe","Denver","Jefferson")
# Tuple Indexing
counties_tuple[:-1]
counties_tuple[:2]
counties_tuple[0:2]

# Dictionaries 
counties_dict = {}
# Creating a key in a dictionary 
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438
# Len of a dict
## REturns the number of keys in a dict
## Doesn't care if there are more than 1 thing under the certain key
## Just cares about the "Jefferson" key for example
len(counties_dict)
# Get all keys and values 
counties_dict.items() # Basically tells you what you'd get by just typing the object in and running it
# Get all the keys 
counties_dict.keys() # Gives you all the keys 
# Get all the values 
counties_dict.values()
# HOw to get specific values 
counties_dict.get("Denver") # Pulls the values associated with Denver
counties_dict.get("Arapahoe")
counties_dict["Arapahoe"]

# Lists in Dictionaries 
voting_data = [] # Creates an empty [list]
# Add county and registered_voter keys + the values for each respectively 
voting_data.append({"county":"Arapahoe", "registered_voters": 422829}) 
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})
# Add El Paso an voters into the second position in voting data 
voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
# Remove Arapahoe and voters from voting data 
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829}) # Is there an easier way to remove the something from a dictionary? What if it's a lot of data? WE don't want to have to write all that out. 
# Make denver the 3rd item, but keep jefferen and friends as the 2nd item 
voting_data
order = [0,2,1]
voting_data = [voting_data[i] for i in order]
voting_data
# Add arapahoe to the voting data
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data

# if you need to create an algorithm that calculates the percentage of votes a candidate receives in an election, you might write a simple algorithm like this:
# How many votes did you get?
my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")


#1.    # Declare the "my_votes" variable equal to an input function. The input function will prompt the user to type an amount, such as 200. 
#2.    # Wrap the input function with the int() method. When we use an input function, the data type of the user input defaults to a string. The int() method converts the user input value to an integer, which is necessary to perform the calculation for the percentage of votes. If we want the user to enter a floating-point decimal number, then we would use the float() method.
#3.    # Calculate the percentage of votes by dividing the users' votes by the total votes, and then multiplying by 100 using the multiplication operator, the asterisk.
#4.    # Create a print statement that tells the percentage of votes. The percentage_votes must be converted from int to a string data type using str(), which is necessary in order to print the percentage of votes in the sentence.

# If statements 
# if condition: 
    # statement 1
    # Statement 2
# The continuation of the if statement is based on the indentations, not certain character symbols

counties = ["Arapahoe","Denver","Jefferson"]
if counties[1] == 'Denver':
    print(counties[1])

# If else Python structure 
# if condition:
#    statement 1
#    statement 2
# else:
#    statement 1
#    statement 2

## Have to run below in a git hub or outside terminal to become interactive 

temperature = int(input("What is the temperature outside? "))
if temperature > 80:
    print("Turn on the AC.")
else:
    print("Open the windows.")

# Nested If Else Statements 
# both of these work in python 

#What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
else:
    if score >= 80:
        print('Your grade is a B.')
    else:
        if score >= 70:
            print('Your grade is a C.')
        else:
            if score >= 60:
                print('Your grade is a D.')
            else:
                print('Your grade is an F.')

# you use these in excel, when you did nested ifs 

# What is the score?
score = int(input("What is your test score? "))

# Determine the grade.
if score >= 90:
    print('Your grade is an A.')
elif score >= 80:
    print('Your grade is a B.')
elif score >= 70:
    print('Your grade is a C.')
elif score >= 60:
    print('Your grade is a D.')
else:
    print('Your grade is an F.')

    # The length of the decision structure determines whether you use a nested if-else statement or the if-elif-else statement. If you have to scroll horizontally on your computer screen to see all the code in an if-else statement , then you should use an if-elif-else statement.

# Membership Operators 
counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties.")
else:
    print("El Paso is not the list of counties.")

    # In the code, the decision statement checks if "El Paso" is in the counties list. If it is true, then the first print statement is printed to the screen. But the if statement is false, so the else statement is checked; since it is true, the second print statement is printed to the screen.

# Logical Operators 
# and, or, or not 

# And operators
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe or El Paso is not in the list of counties.")

    # In the code, the decision statement checks if both Arapahoe and El Paso are in the counties list. Arapahoe is in the counties list, which is "true," but El Paso is not in the counties list, which is "false." Therefore, the compound expression is false.

# Or operators 
if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso is in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties.")

# Practice 
if "Arapahoe" in counties and "El Paso" not in counties:
    print("Only Arapahoe is in the list of counties.")
else:
    print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# For Loops 
# for item in [items]:
#     statement 1
#     statement 2

for county in counties:
    print(county)

# Range Function 
#  The range() function creates an iterable object or a list. For example, if we had a list of numbers, we could print each number using a for loop like this:
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

for num in range(5):
    print(num)

for i in range(len(counties)):
    print(counties[i])

for county in counties_tuple:
    print(county)

# How to Iterate through a dictionary 
counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438} # Dictionary because {}
for county in counties_dict:
    print(county) # Don't forget the ":" in the for loop!

for county in counties_dict.keys():
    print(county)

# How to get the values of a dictionary 
for voters in counties_dict.values: 
    print(voters)

for county in counties_dict:
    print(counties_dict[county])

for county in counties_dict:
    print(counties_dict.get(county))

# How to get teh key value pairs of a dictionary 
# for key, value in dictionary_name.items():
#     print(key, value)

for county, voters in counties_dict.items():
    print(county, voters) # Basically print the table, but not in a table format for each key and output

# IMPORTANT: When iterating over a dictionary
    # The first variable declared in the for loop is assigned to the keys.
    # The second variable is assigned to the values.

for county, voters in counties_dict.items():
    print(f"{county} has {voters} registered voters.") 

# Iterate Through a List of DIctionaries 
# A for loop can be used to iterate through a list of dictionaries like our voting_data list of dictionaries we created earlier. With a for loop we can:

#     Retrieve each dictionary in the list
#     Retrieve only the values of each dictionary
#     Retrieve the key-value pairs of each dictionary

# Get Each Dictionary in a List of Dictionaries 
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

# Using range function to iterate over a list of dictionaries and print the counties in voting_data
for i in range(len(voting_data)):
    print(voting_data[i]['county'])

# Get the values from a list of dictionaries 
for county_dict in voting_data:
    for value in county_dict.values():
        print(value)

# How would you retrieve the number or registered voters from each dictionary? 
for county_dict in voting_data: 
    print(county_dict["registered_voters"]) # Replace the registered_voters for county if you just want county 

# YOu might have to run the python_practice first document to get some of these variables in the working environment for this to run properly 

# Printing Formats 
# So far, we have used the Python print() function to print the following:

#     A string, or a sentence displayed between quotes. For example: print("Hello World") and print("Arapahoe and Denver are not in the list of counties.").
#     A string with integer values converted to a string using concatenation with the "+" sign. For example: print("Your interest for the year is $" + str(interest)) 

# Printing with F-strings 
# The general format for f-strings is as follows:

#     The f-string begins with an f followed by a string contained within quotes. (The term f-string comes from the leading "f" character preceding the string literal.)
#     In the f-string, curly braces are used to add variables or expressions to the f-string.

# Here's the original code:

my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
percentage_votes = (my_votes / total_votes) * 100
print("I received " + str(percentage_votes)+"% of the total votes.")

# With F-strings 
my_votes = int(input("How many votes did you get in the election? "))
total_votes = int(input("What is the total votes in the election? "))
print(f"I received {my_votes / total_votes * 100}% of the total votes.")

#Using F-strings with dictionaries 
counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

# Multiline f-strings 
candidate_votes = int(input("How many votes did the candidate get in the election? "))
total_votes = int(input("What is the total number of votes in the election? "))
message_to_candidate = (
    f"You received {candidate_votes} number of votes. "
    f"The total number of votes in the election was {total_votes}. "
    f"You received {candidate_votes / total_votes * 100}% of the total votes.")

print(message_to_candidate)

# Format floating-point decimals 
# The general format for a number to format it in an f-string is as follows:

# f'{value:{width}.{precision}}'

# In the format, the width specifies the number of characters used to display the value. However, if a value needs more space than the width specifies, the additional space is used.

# The precision indicates the number of decimal places to format the value. For example, to format the interest to two decimal places, we would use .2f, where f means "floating-point decimal format".

# When formatting a number, we can also add a thousands separator with a comma, using the following format. The comma is placed after the {width}.

# f'{value:{width},.{precision}}'

message_to_candidate = (
    f"You received {candidate_votes:,} number of votes. "
    f"The total number of votes in the election was {total_votes:,}. "
    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county, voters in counties_dict.items():
    print(f"{county} has {voters:,} registered voters.") 

# This code below doesn't run and I don't know why: QUESTION 
# Last skill drill on 3.2.11 Printing Formats 
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}] # This is a list with dictionaries in it 
# for county, voters in voting_data: 
#     print(f"{"county"} has {"voters"} registered voters.")