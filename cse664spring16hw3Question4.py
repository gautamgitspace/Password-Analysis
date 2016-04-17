import hashlib

# useful sources:
# http://stackoverflow.com/questions/11111625/python-read-second-column-from-file
# http://stackoverflow.com/questions/2059111/python-if-statement-with-multiple-conditions

with open('cse664spring16hw3Question1.txt') as inf:
    for line in inf:
        parts = line.split("\t")
        if len(parts) > 1:
            f3 = open('sortedFile.txt', 'a')
            print 'writing to sortedFile.txt'
            f3.write(parts[1])
            print 'execution of sortedFile.txt complete'

f = open('sortedFile.txt', 'r')
print 'opened'
for line in f:
    line = line.rstrip()
    abc = str(hashlib.md5(line).hexdigest())
    if abc == 'ba931c15ec0163c4bb339f41571694ce' or abc == 'c9cd905fc459e5550b8c3b01d4346c25' or abc == 'e9269d9e52a692f52caece9d0e7cdae1' or abc == '660719b4a7591769583a7c8d20c6dfa4':
        print 'match found'
        f2 = open('cse664spring16hw3Question4.txt', 'a')
        print 'writing to file'
        f2.write(abc + "\t" + line + '\n')
        print 'done'







