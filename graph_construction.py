#Graph Construction:
#Proof
#Given an encoded number of strings within a directed acyclic graph, there are only 2 classes of strings that exist :
#A subset of the string itself
#An extension of the string
# A subset of an extension if not part of the string, and will always be false
# An extension of the subset may only be part of the string, if the extension is a subset of multiple different strings. 
# The combined subset of 2 strings with the same length can never be correct unless the string is correct within the dag. 
# We thus can classify all relations of the strings of the same length within a single graph.
# With the space of 27 char * 17
#Implementation:
#Map every single character maps by groupiing them by length
#Same length same map
#17 maps total
strings=["wate","weth","eart","fire","earl","late","size","mellow","stop","arch","nope"]
#similar length hashmap
hashkey=list(map(chr,(range(0+ord('a'),26+ord('a'),1))))
hashkey.append('+')
hashmap=dict((i,[set(),set()]) for i in hashkey)
allLengthHashmap=dict()
for i in range(1,18,1):
    allLengthHashmap[i]=hashmap.copy()
#Backtrack 2x, might need optimization
for i in range(0,len(strings),1):
    for j in range(1,len(strings[i]),1):
        if strings[i][j] not in allLengthHashmap[len(strings)][strings[i][j-1]][0]:
            allLengthHashmap[len(strings)][strings[i][j-1]][0].add(strings[i][j])
        if j>=2:
            if strings[i][j-2] not in allLengthHashmap[len(strings)][strings[i][j]][1]:
                allLengthHashmap[len(strings)][strings[i][j]][1].add(strings[i][j-2])
print(allLengthHashmap[4])
def CheckInclude(stringname):
    print("String:"+stringname)
    for i in range(1,len(stringname),1):
        if stringname[i] not in allLengthHashmap[len(stringname)][stringname[i-1]][0]:
            print("Not included")
            return
        if(i>=2):
            if stringname[i-2] not in allLengthHashmap[len(stringname)][stringname[i]][1]:
                print("Not included")
                return
    print("Object Found")
    return

def GADDAGAdder(stringname,array):
    array.append(stringname)
    for i in range(1,len(stringname),1):
        array.append(stringname[-1:-i-1:-1]+'+'+stringname[0:len(stringname)-i:1])

newlist=list()
GADDAGAdder("zero",newlist)
print(newlist)

for i in strings:
    CheckInclude(i)



            





