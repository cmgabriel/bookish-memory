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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""
def identifyTeleMarketers(callList,textList):
    callerList = list()
    receiverList = list()
    for item in callList:
        modifiedList = item[:2]
        if modifiedList[0].startswith("140"):
            callerList.append(modifiedList[0])
        if modifiedList[1].startswith("140"):
            receiverList.append(modifiedList[1])
    
    #convert the text list in a single caller list as the operation is going to remain the same
    # the number in the callerList should not be able to send or receive texts
    modifiedTextList = list()
    # ~O(3n)
    for textRec in textList:
        modifiedTextList.append(textRec[0])
        modifiedTextList.append(textRec[1])
    
    # convert the text list in unique values to reduce the number of iterations
    # k is number of items in set
    # worst case: k = n => O(n)
    textSet = set(modifiedTextList)
    receiverSet = set(receiverList)
    
    newCallerList = callerList.copy()

    for i,caller in enumerate(callerList):
        if caller in receiverSet or caller in textSet:
            newCallerList.remove(i)
    
    uniqueList = sorted(list(set(newCallerList)))
    return uniqueList
print("These numbers could be telemarketers: ")
uniqueList = identifyTeleMarketers(calls,texts)
for item in uniqueList:
    print("{}".format(item))