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

import game as g
import copy as copy
import util 
wordChecker=g.Dictionary("dictionary.txt")
def GADDAGAdder(stringname,array):
    for i in range(1,len(stringname),1):
        array.append(stringname[0:i][::-1]+'+'+stringname[i:len(stringname)])
    array.append(stringname[::-1])
array=[]
GADDAGAdder("AARDVARK",array)
print(array)

wordCheckerReversed=g.Dictionary("revdictionary.txt")

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
    if (Square.get_letterTile()==None and not hand) :
        return 
    if Direction=="Vertical" and y<15 and (Square.get_letterTile()==None and hand):  #If extendable from position
        for i in range(0,len(hand)):
            print(hand)
            print("i="+hand[i])
            if wordChecker.check_word(play+hand[i]) and Board[x][y+1].get_letterTile()==None:
                words.append(play+hand[i])
            if wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1])==True :
                print("Check Reversed")
                temp=hand[i]
                hand.remove(hand[i])
                allsuffixes.append((play+temp)[::-1])
                hands.append(hand)
                hand.insert(i,temp)
            if (wordChecker.dictionary.t.has_subtrie(play+hand[i])==True or wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1])) and cross_check(hand[i],"Vertical",Board,x,y):
                print("Extension entered")
                temp=hand[i]
                hand.remove(hand[i])
                ExtendRight(Board[x][y+1],Board,hand,play+temp,Direction,allsuffixes,hands,words,x,y+1)
                hand.insert(i,temp)
                print("Appended")
    
    if Direction=="Horizontal" and x<15 and (Square.get_letterTile()==None and hand):
        for i in range(0,len(hand)):
            print(hand)
            print("i="+hand[i])
            print("play="+play+hand[i])
            
            if wordChecker.check_word(play+hand[i]) and Board[x+1][y].get_letterTile()==None:
                words.append(play+hand[i])
            if wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1])==True:
                print("Check Reversed")
                temp=hand[i]
                hand.remove(hand[i])
                allsuffixes.append((play+temp)[::-1])
                hands.append(copy.deepcopy(hand))
                hand.insert(i,temp)
            if (wordChecker.dictionary.t.has_subtrie(play+hand[i])==True or wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1]))and cross_check(hand[i],"Horizontal",Board,x,y):
                print("Extension entered")
                temp=hand[i]
                hand.remove(hand[i])
                ExtendRight(Board[x+1][y],Board,hand,play+temp,Direction,allsuffixes,hands,words,x+1,y)
                hand.insert(i,temp)
                print("Appended")

def ExtendLeft(Square,Board,hand,play,Direction,words,x,y):
        for m in range(0,len(hand)):
            if Direction =="Horizontal" and x>0 and Square.get_letterTile()==None and hand:
                print("play="+play)
                print(hand)
                print("i="+hand[m])
                if x>2:
                    if Board[x-2][y].get_letterTile()!=None:
                        break
                if wordCheckerReversed.check_word(play+hand[m]) and Board[x-1][y].get_letterTile()==None:
                    emptyword=""
                    for i in range(0,len(play+hand[m])):
                        phase=0
                        if phase==0:
                            if (play+hand[m])[i]=='+':
                                phase=1
                            else:
                                emptyword=(play+hand[m])[i]+emptyword
                        if phase==1:
                            emptyword=emptyword+(play+hand[m])[i]
                    words.append(emptyword)
                    print("Reversed True")
                if wordCheckerReversed.dictionary.t.has_subtrie(play+hand[m])==True and cross_check(hand[m],"Horizontal",Board,x,y):
                    temp=hand[m]
                    hand.remove(hand[m])
                    ExtendLeft(Board[x-1][y],Board,hand,play+temp,Direction,words,x-1,y)
                    hand.insert(m,temp)
                    
            if Direction=="Vertical" and y>0 and Square.get_letterTile()==None and hand:
                if y>2:
                    if Board[x][y-2].get_letterTile()!=None:
                        break
                if wordCheckerReversed.check_word(play+hand[m]) and Board[x][y-1].get_letterTile==None:
                    words.append((play+hand[m][::-1]))
                if wordCheckerReversed.dictionary.t.has_subtrie(play+hand[m])==True and cross_check(hand[m],"Vertical",Board,x,y):
                    temp=hand[m]
                    hand.remove(hand[m])
                    ExtendLeft(Board[x][y-1],Board,hand,play+temp,Direction,words,x,y-1)
                    hand.insert(m,temp)
                    print("Appended")



def wordSearch(Square,Board,hand,play,Direction,allsuffixes,allhands,words,x,y):
 ExtendRight(Square,Board,hand,play,Direction,allsuffixes,allhands,words,x,y)
 for i in range(0,len(allsuffixes)):
    play=allsuffixes[i]
    hand=allhands[i]
    ExtendLeft(Square,Board,hand,play,Direction,words,x,y)

def DictionaryGADDAG(filename):
    with open (filename,"r") as file:
        words=file.readlines()
    words=[word.rstrip() for word in words]
    file = open("revdictionary.txt","w")
    array=[]
    for k in words:
        GADDAGAdder(k,array)
    print(array)
    for i in array:
        file.write(i+"\n")
    file.close()


def cross_check(Letter,Direction,Board,x,y):
    word=Letter
    print("Test")
    if Direction=="Horizontal":
        j=0
        while(y<15):
            if Board[x][y+j].get_letterTile()==None:
                 break
            else:
                 j=j+1
                 word=word+Board[x][y+j].get_letterTile().get_letter()
        j=0
        while(y>0):
            if Board[x][y-j].get_letterTile()==None:
                break
            else:
                j=j+1
                word=Board[x][y-j].get_letterTile().get_letter()+word
        if len(word)<=1:
            return True
        else:
            return wordChecker.check_word(word)
    if Direction=="Vertical":
        j=0
        while(x<15):
            
            if Board[x+j][y].get_letterTile()==None:
                 break
            else:
                 j=j+1
                 word=word+Board[x+j][y].get_letterTile().get_letter()
        j=0
        while(x>0):
            if Board[x-j][y].get_letterTile()==None:
                break
            else:
                j=j+1
                word=word+Board[x-j][y].get_letterTile().get_letter()
        if len(word)<=1:
            return True
        else:
            return wordChecker.check_word(word)

abc=g.Board()
suffixlist=[]
words=[]
play=[]
hands=[]
DictionaryGADDAG("dictionary.txt")
#DictionaryReversal("dictionary.txt")
wordSearch(abc.board[0][0],abc.board,["S","T","A","B","A","L","E"],"","Horizontal",suffixlist,hands,words,3,3)
print(words)
print(""+"a")

print((wordChecker.dictionary.t.has_subtrie("AD")))

def BoardScanner(Board,hand):
    for i in range(0,16,1):
        for j in range(0,16,1):
            if Board[i][j+1].get_letterTile()!=None:
                suffixlist=[]
                hands=[]
                wordSearch(Board[i][j],Board,hand,"","Vertical",suffixlist,hands,words,i,j)
            if Board[i+1][j].get_letterTile()!=None:
                suffixlist=[]
                hands=[]
                wordSearch(Board[i][j],Board,hand,"","Horizontal",suffixlist,hands,words,i,j)



            





