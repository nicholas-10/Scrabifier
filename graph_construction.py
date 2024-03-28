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

import game as g
import test as t

wordChecker=g.Dictionary("dictionary.txt")
#Row/Column Checker


# Flow:
# We start by putting a play container so that its extendable to the right.
# When the node is extendable to left,insert. Then check if node extendable to right, then extend. If node not extendable to right, then append to words, if the word is not extendable anymore.
def ExtendRight(Square,Board,hand,play,Direction,allsuffixes,hands,words,x,y):
     #insert contains all letters
    print("play="+play)
    if Square.get_letterTile()!=None and Direction=="Vertical":
        ExtendRight(Board[x][y+1],Board,hand.remove(i),play+Board[x][y].get_letterTile().get_letter(),Direction,allsuffixes,hands,words,x,y+1)
        return
    if Square.get_letterTile()!=None and Direction=="Horizontal":
        ExtendRight(Board[x+1][y],Board,hand.remove(i),play+Board[x][y].get_letterTile().get_letter(),Direction,allsuffixes,hands,words,x+1,y)
        return
    if wordChecker.check_prefix(play+"+") and not play: #For all +
            print("CHECK GADDAG")
            allsuffixes.append(play[::-1]+"+")
            hands.append(hand)
    if (Square.get_letterTile()==None and not hand) :
        return 
    if Direction=="Vertical" and y<15 and (Square.get_letterTile()==None and hand):  #If extendable from position
        sentinel=0
        for i in range(0,len(hand)):
            print(hand)
            print("i="+hand[i])
            if wordChecker.check_word(play+hand[i]) and sentinel==0 and Board[x][y+1].get_letterTile==None:
                words.append(play+hand[i])
            if wordChecker.dictionary.t.has_subtrie(play+hand[i])==True and cross_check(hand[i],"Vertical",Board,x,y):
                print("Extension entered")
                temp=hand[i]
                hand.remove(hand[i])
                ExtendRight(Board[x][y+1],Board,hand,play+temp,Direction,allsuffixes,hands,words,x,y+1)
                hand.insert(i,temp)
                print("Appended")
    
    if Direction=="Horizontal" and x<15 and (Square.get_letterTile()==None and hand):
        sentinel=0
        for i in range(0,len(hand)):
            print(hand)
            print("i="+hand[i])
            if wordChecker.check_word(play+hand[i]) and sentinel==0 and Board[x+1][y].get_letterTile==None:
                words.append(play+hand[i])
            if wordChecker.dictionary.t.has_subtrie(play+hand[i])==True and cross_check(hand[i],"Horizontal",Board,x,y):
                print("Extension entered")
                temp=hand[i]
                hand.remove(hand[i])
                ExtendRight(Board[x+1][y],Board,hand,play+temp,Direction,allsuffixes,hands,words,x+1,y)
                hand.insert(i,temp)
                print("Appended")
    
def cross_check(LetterTile,Direction,Board):
    word=[LetterTile]
    if Direction=="Horizontal":
        j=0
        while(LetterTile.get_y()<15):
            
            if Board[LetterTile.get_x()][LetterTile.get_y()+j].get_letter()==None:
                 break
            else:
                 j=j+1
            word.append(Board[LetterTile.get_x()][LetterTile.get_y()+j])
        j=0
        while(LetterTile.get_y()>0):
            if Board[LetterTile.get_x()][LetterTile.get_y()-j].get_letter()==None:
                break
            else:
                j=j+1
            word.insert(0,Board[LetterTile.get_x()][LetterTile.get_y()-j])
        return wordChecker.check_word(word)
    if Direction=="Vertical":
        j=0
        while(LetterTile.get_y()<15):
            
            if Board[LetterTile.get_x()+j][LetterTile.get_y()].get_letter()==None:
                 break
            else:
                 j=j+1
            word.append(Board[LetterTile.get_x()+j][LetterTile.get_y()])
        j=0
        while(LetterTile.get_y()>0):
            if Board[LetterTile.get_x()]-j[LetterTile.get_y()].get_letter()==None:
                break
            else:
                j=j+1
            word.insert(0,Board[LetterTile.get_x()-j][LetterTile.get_y()])
        return wordChecker.check_word(word)



            





