from __future__ import division
from collections import Counter
from math import log

#useful source for calculating entropy - http://blog.dkbza.org/2007/05/scanning-data-for-entropy-anomalies.html

inputData = ""
progress = 0
entropyValue = dict()
joinCharacter = ''

with open('/Users/Gautam/Downloads/pwds300', 'r') as inf:
    for line in inf:
        inputData = inputData + line
inputData = inputData.strip()
print "data read and stripped"
inputDataList = inputData.split('\n')
print "data split"
uniqueInputDataList = set(inputDataList)
print "fetched unique"

inputData = joinCharacter.join(uniqueInputDataList)
occurrence = Counter(inputData)
base = len(inputData)
print "calculating entropy"
for iteratorVar in uniqueInputDataList:
    entropy = 0.0
    scrape = joinCharacter.join(set(iteratorVar))
    for c in scrape:
        entropy = entropy - (occurrence[c]/base)*log((occurrence[c]/base), 2)
    entropyValue[iteratorVar] = entropy
    print progress
    progress = progress + 1

output = open('cse664spring16hw3Question3.txt', 'w')
print 'opening output file'
for iteratorVar2 in sorted(entropyValue, key=entropyValue.get, reverse=True):
    output.write(str(entropyValue[iteratorVar2]) + '\t' + iteratorVar2 + '\n')
output.close

print 'EXECUTION COMPLETE'

