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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
textFirstRecord = texts[0]
callLastRecord = calls[-1]
# first record of the texts printed
print("First record of texts, {} texts {} at time {}".format(str(textFirstRecord[0]),
str(textFirstRecord[1]),
str(textFirstRecord[2])))
# Last record of the call printed
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(
    str(callLastRecord[0]),str(callLastRecord[1]),str(callLastRecord[2]),str(callLastRecord[3])
))

