from __future__ import division
from collections import Counter
from math import log

#useful source for calculating entropy - http://blog.dkbza.org/2007/05/scanning-data-for-entropy-anomalies.html

inputData = ""
progress = 0
joinCharacter = ''
entropyValue = dict()

with open('/Users/Gautam/Downloads/pwds300', 'r') as inf:
    for line in inf:
        inputData = inputData + line
inputData = inputData.strip()
print "data read and stripped"
inputDataList = inputData.split('\n')
print "data split"
inputData = inputData.replace('\n', '')
print "replaced"
occurrence = Counter(inputData)
base = len(inputData)
output = open('cse664spring16hw3Question2.txt', 'w')
print "opened"

for iteratorVar in inputDataList:
    entropy = 0.0
    scrape = joinCharacter.join(set(iteratorVar))
    for c in scrape:
        entropy = entropy - (occurrence[c]/base)*log((occurrence[c]/base), 2)
    entropyValue[iteratorVar] = entropy
    print progress
    progress = progress+1

for iteratorVar2 in sorted(entropyValue, key=entropyValue.get, reverse=True):
    output.write(str(entropyValue[iteratorVar2]) + '\t' + iteratorVar2 + '\n')
output.close()
print "EXECUTION COMPLETE"
