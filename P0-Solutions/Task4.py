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
        callerList.append(modifiedList[0])
        receiverList.append(modifiedList[1])
    
    modifiedTextList = list()
    for textRec in textList:
        modifiedTextList.append(textRec[0])
        modifiedTextList.append(textRec[1])

    uniqueCallers = set(callerList)
    uniqueReceivers = set(receiverList)
    uniqueTextSenders = set(modifiedTextList)
    uniqueTextReceivers = set(receiverList)
    
    telemarketers = uniqueCallers.copy()

    for caller in uniqueCallers:
        if caller in uniqueReceivers or caller in uniqueTextSenders or caller in uniqueTextReceivers:
            telemarketers.remove(caller)

    return sorted(list(telemarketers))
print("These numbers could be telemarketers: ")
uniqueList = identifyTeleMarketers(calls,texts)
for item in uniqueList:
    print("{}".format(item))