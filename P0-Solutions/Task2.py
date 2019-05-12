"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
def extractLongestCallInformation(itemList):
    callTimeRecords = dict()
    print("Length of itemList:",len(itemList))
    # O(n**2)
    for i,item in enumerate(itemList):
        callerPhone = item[0]
        callLength = int(item[-1])
        #If key already exists in the dictionary sum up the value
        if callerPhone in callTimeRecords:
            callTimeRecords[callerPhone] += callLength
        else:
            callTimeRecords[callerPhone] = callLength

        for rec in itemList:
            if callerPhone == rec[1]:
                callTimeRecords[callerPhone] += callLength
    # O(n Log n)
    sortedCallTimeRecords = sorted(callTimeRecords, key=callTimeRecords.get, reverse=True)
    return sortedCallTimeRecords[0],callTimeRecords[sortedCallTimeRecords[0]]

callPhone,duration = extractLongestCallInformation(calls)
print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(callPhone,duration))


