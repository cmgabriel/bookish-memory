"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def extractPhone(telephoneRecords, itemList):
    # Runs for n number of times
    for item in itemList:
        # Slice the value of item to first 2 -
        value = item[:2]
        # Runs 2 times every n number of times + 2 times execution of for loop
        # Runs 4 other statements inside the loop so + 4
        for i in value:
            telephoneRecords.append(i)
    return telephoneRecords

# Big O Notation - O(n)
telephoneRecords = []
uniquePhoneCount = 0
#Extract Telephone Records from Texts
telephoneRecords = extractPhone(telephoneRecords, texts)
#Extract Telephone Records from Calls
telephoneRecords = extractPhone(telephoneRecords, calls)
#Generate a set
uniqueRecords = set(telephoneRecords)
#Count the Number of Items in records that are unique
uniquePhoneCount = len(uniqueRecords)

print("There are {} different telephone numbers in the records.".format(str(uniquePhoneCount)))