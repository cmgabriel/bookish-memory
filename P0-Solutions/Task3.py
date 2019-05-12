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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def findCodesAndPrefixes(callerPrefix,itemList):
  # Get all records where calls made by callerPrefix
  callerList = list()
  codesList = list()
  totalCalls = list()
  for item in itemList:
    #shorten the list to first 2 elements as we donot need the rest of the information
    revisedList = item[:2]
    if callerPrefix in revisedList[0]:
      totalCalls.append(revisedList)
      #Check for the calls made to Bangalore fixed lines only
      if revisedList[1].startswith("(080)"):
        callerList.append(revisedList)
      areaCode = getAreaCode(revisedList[1])
      codesList.append(areaCode)    
  uniqueCodeList = sorted(list(set(codesList)))
  return uniqueCodeList, callerList, totalCalls

def getAreaCode(item):
  areaCode = ""
  if item.startswith("("):
    areaCode = item.split(')')[0]
    areaCode = areaCode[1:]
  #Check for calls made to all Telemarketers
  elif item.startswith("140"):
    areaCode = 140
  #Check for calls made to all mobile phones
  else:
    areaCode = (item.split(" ")[0])[:4]
  return areaCode

def calculateCallPercentage(noOfAreaSpCalls,totalNoOfCallsArea):
  return (noOfAreaSpCalls/totalNoOfCallsArea) * 100

uniqueCodeList, callerList, totalCalls = findCodesAndPrefixes("(080)",calls)

percentageOfCalls = calculateCallPercentage(len(callerList),len(totalCalls))

#Print the list of codes for the numbers in lexicographic order
print("The numbers called by people in Bangalore have codes: ")
for item in uniqueCodeList:
  print(item)

print("{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(percentageOfCalls))