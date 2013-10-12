from selection2 import *

# read list from file
infile = 'wordlst.txt'
f = open(infile,'r')
list = f.readlines()
f.close()

# define median such that if nElements is even, chooses
# smaller of two possible choices
nElements = len(list)
mediank = (nElements-1)//2

callsArr = []
for i in range(0,1000):
    (str,numCalls) = selection2(list,mediank,1)
    callsArr.append(numCalls)
    print(i,numCalls)

print("min is: ",min(callsArr))
print("max is: ",max(callsArr))
print("avg is: ",sum(callsArr)/len(callsArr))
