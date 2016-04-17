# -*- coding: utf-8 -*-

# sources:
# http://stackoverflow.com/questions/4183506/python-list-sort-in-descending-order

f = open('pwds300', 'r')
occurrence = dict()
data = list()
for line in f:
    line = line.rstrip()
    occurrence[line] = occurrence.get(line,0) + 1
for password, count in occurrence.items():
    data.append((count, password))
data.sort(reverse=True)
for entry in data:
    output = str(entry[0]) + "\t" + str(entry[1] + '\n')
    f2 = open('cse664spring16hw3Question1.txt', 'a')
    print "writing to file"
    f2.write(str(output))
print 'execution complete'