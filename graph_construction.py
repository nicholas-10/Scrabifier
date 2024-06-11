

import copy as copy
import util 
class Dictionary1:
    """
    Dictionary object for game
    """
    def __init__(self, filename):
        with open(filename, "r") as file:
            words = file.readlines()
        words = [word.rstrip() for word in words]
        self.dictionary = util.Trie(words)
    def check_word(self, word):
        """
        Used to check if word is in dictionary. Example, d.check_word("ADMIRE"). Return True if it is, False if not
        """
        if self.dictionary.search(word) == True:
            return True
        else:
            return False
wordChecker=Dictionary1("dictionary.txt")
def GADDAGAdder(stringname,array):
    for i in range(1,len(stringname),1):
        array.append(stringname[0:i][::-1]+'+'+stringname[i:len(stringname)])
    array.append(stringname[::-1])
array=[]

wordCheckerReversed=Dictionary1("revdictionary.txt")

#Row/Column Checker
# Flow:
# We start by putting a play container so that its extendable to the right.
# When the node is extendable to left,insert. Then check if node extendable to right, then extend. If node not extendable to right, then append to words, if the word is not extendable anymore.
def ExtendRight(Square,Board,hand,play,Direction,allsuffixes,hands,words,x,y,lefttrail,initial,positions,temppositions):
     #insert contains all letters
    print("play="+play)
    if Square.get_letterTile()!=None and Direction=="Horizontal":
        if y<14:
            print("Down not empty")
            ExtendRight(Board[x][y+1],Board,hand,play+Board[x][y].get_letterTile().get_letter(),Direction,allsuffixes,hands,words,x,y+1,lefttrail,initial,positions,temppositions)
            if wordCheckerReversed.dictionary.t.has_subtrie((play+Board[x][y].get_letterTile().get_letter())[::-1])==True and Board[x][y+1].get_letterTile()==None :
                allsuffixes.append((play+Board[x][y].get_letterTile().get_letter())[::-1])
                hands.append(copy.deepcopy(hand))
                temppositions.append([initial,y])
        if y==14 and wordCheckerReversed.dictionary.t.has_subtrie((play+Board[x][y].get_letterTile().get_letter())[::-1])==True:
            allsuffixes.append((play+Board[x][y].get_letterTile().get_letter())[::-1])
            hands.append(copy.deepcopy(hand))
            temppositions.append([initial,y])
        return
        
    if Square.get_letterTile()!=None and Direction=="Vertical":
        if x<14:
            print("Right not empty")
            ExtendRight(Board[x+1][y],Board,hand,play+Board[x][y].get_letterTile().get_letter(),Direction,allsuffixes,hands,words,x+1,y,lefttrail,initial,positions,temppositions)
            if wordCheckerReversed.dictionary.t.has_subtrie((play+Board[x][y].get_letterTile().get_letter())[::-1])==True and Board[x+1][y].get_letterTile()==None:
                allsuffixes.append((play+Board[x][y].get_letterTile().get_letter())[::-1])
                hands.append(copy.deepcopy(hand))
                temppositions.append([initial,x])
            return
        if x==14 and wordCheckerReversed.dictionary.t.has_subtrie((play+Board[x][y].get_letterTile().get_letter())[::-1])==True:
            allsuffixes.append((play+Board[x][y].get_letterTile().get_letter())[::-1])
            hands.append(copy.deepcopy(hand))
            temppositions.append([initial,y])
        return
    if (Square.get_letterTile()==None and not hand) :
        return 
    if Direction=="Horizontal" and (Square.get_letterTile()==None and hand):  #If extendable from position
        if y<14: 
            for i in range(0,len(hand)):
                print(hand)
                print("i="+hand[i])
                if wordChecker.check_word(play+hand[i]) and Board[x][y+1].get_letterTile()==None:
                    if lefttrail==None:
                        words.append(play+hand[i])
                        positions.append([initial,y])
                if wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1])==True and Board[x][y+1].get_letterTile()==None and cross_check(hand[i],"Horizontal",Board,x,y):
                    print("Check Reversed")
                    temp=hand[i]
                    hand.pop(i)
                    allsuffixes.append((play+temp)[::-1])
                    hands.append(copy.deepcopy(hand))
                    hand.insert(i,temp)
                    temppositions.append([initial,y])
                if (wordChecker.dictionary.t.has_subtrie(play+hand[i])==True or wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1])) and cross_check(hand[i],"Horizontal",Board,x,y):
                    print("Extension entered")
                    temp=hand[i]
                    hand.pop(i)
                    ExtendRight(Board[x][y+1],Board,hand,play+temp,Direction,allsuffixes,hands,words,x,y+1,lefttrail,initial,positions,temppositions)
                    hand.insert(i,temp)
                    print("Appended")
        if y==14:
            for i in range(0,len(hand)):
                if wordChecker.check_word(play+hand[i]):
                    if lefttrail==None:
                            words.append(play+hand[i])
                            positions.append([initial,y])
                    if wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1])==True and cross_check(hand[i],"Horizontal",Board,x,y):
                        print("Check Reversed")
                        temp=hand[i]
                        hand.pop(i)
                        allsuffixes.append((play+temp)[::-1])
                        hands.append(copy.deepcopy(hand))
                        hand.insert(i,temp)
                        temppositions.append([initial,y])
            



    
    if Direction=="Vertical" and x<15 and (Square.get_letterTile()==None and hand):
        if x<14:
            for i in range(0,len(hand)):
                if wordChecker.check_word(play+hand[i]) and (Board[x+1][y].get_letterTile()==None):
                    if lefttrail==None:
                        words.append(play+hand[i])
                        positions.append([initial,x])
                        
                if wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1])==True and (Board[x+1][y].get_letterTile()==None or x==14)  and cross_check(hand[i],"Vertical",Board,x,y):
                    print("Check Reversed")
                    temp=hand[i]
                    hand.pop(i)
                    allsuffixes.append((play+temp)[::-1])
                    hands.append(copy.deepcopy(hand))
                    hand.insert(i,temp)
                    temppositions.append([initial,x])
                if (wordChecker.dictionary.t.has_subtrie(play+hand[i])==True or wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1])) and cross_check(hand[i],"Vertical",Board,x,y):
                    print("Extension entered")
                    temp=hand[i]
                    hand.pop(i)
                    ExtendRight(Board[x+1][y],Board,hand,play+temp,Direction,allsuffixes,hands,words,x+1,y,lefttrail,initial,positions,temppositions)
                    hand.insert(i,temp)
                    print("Appended")
        if x==14:
            for i in range(0,len(hand)):
                if wordChecker.check_word(play+hand[i]):
                    if lefttrail==None:
                            words.append(play+hand[i])
                            positions.append([initial,x])
                if wordCheckerReversed.dictionary.t.has_subtrie((play+hand[i])[::-1])==True and cross_check(hand[i],"Vertical",Board,x,y):
                        print("Check Reversed")
                        temp=hand[i]
                        hand.pop(i)
                        allsuffixes.append((play+temp)[::-1])
                        hands.append(copy.deepcopy(hand))
                        hand.insert(i,temp)
                        temppositions.append([initial,x])


def ExtendLeft(Square,Board,hand,play,Direction,words,x,y,positions,temppositions):
    if Direction == "Vertical"  and Square.get_letterTile()!=None:
        if x>0:
            ExtendLeft(Board[x-1][y],Board,hand,play+Board[x][y].get_letterTile().get_letter(),"Vertical",words,x-1,y,positions,temppositions)
            print("Left Appended:"+play+Board[x][y].get_letterTile().get_letter())
            if wordCheckerReversed.check_word(play+Board[x][y].get_letterTile().get_letter()) and Board[x-1][y]==None:
                words.append((play+Board[x][y].get_letterTile().get_letter())[::-1])
                positions.append([x,temppositions[0][1]])
                temppositions.pop(0)
                print("Reversed True")
        if x==0 and wordCheckerReversed.check_word(play+Board[x][y].get_letterTile().get_letter()) :
            words.append((play+Board[x][y].get_letterTile().get_letter())[::-1])
            positions.append([x,temppositions[0][1]])
            temppositions.pop(0)
            print("Reversed True")

    if Direction == "Horizontal"  and Square.get_letterTile()!=None:
        if y>0:
            ExtendLeft(Board[x][y-1],Board,hand,play+Board[x][y].get_letterTile().get_letter(),"Horizontal",words,x,y-1,positions,temppositions)
            if wordCheckerReversed.check_word(play+Board[x][y].get_letterTile().get_letter()) and Board[x][y-1]==None:
                words.append((play+Board[x][y].get_letterTile().get_letter())[::-1])
                positions.append([y,temppositions[0][1]])
                temppositions.pop(0)
                print("Reversed True")
        if y==0 and wordCheckerReversed.check_word(play+Board[x][y].get_letterTile().get_letter()):
            words.append((play+Board[x][y].get_letterTile().get_letter())[::-1])
            positions.append([y,temppositions[0][1]])
            temppositions.pop(0)
            print("Reversed True")

    for m in range(0,len(hand)):
        if Direction =="Vertical" and x>0 and Square.get_letterTile()==None and hand:
            if x>0:
                if wordCheckerReversed.check_word(play+hand[m]) and Board[x-1][y].get_letterTile()==None and cross_check(hand[m],"Vertical",Board,x,y):
                    words.append((play+hand[m])[::-1])
                    positions.append([x,temppositions[0][1]])
                    temppositions.pop(0)
                    print("Reversed True")
                if wordCheckerReversed.dictionary.t.has_subtrie(play+hand[m])==True and cross_check(hand[m],"Vertical",Board,x,y):
                    temp=hand[m]
                    hand.pop(m)
                    ExtendLeft(Board[x-1][y],Board,hand,play+temp,Direction,words,x-1,y,positions,temppositions)
                    hand.insert(m,temp)
            if x==0 and wordCheckerReversed.check_word(play+hand[m]) and cross_check(hand[m],"Vertical",Board,x,y):
                words.append((play+hand[m])[::-1])
                positions.append([x,temppositions[0][1]])
                temppositions.pop(0)
                print("Reversed True")
            
                
                    
        if Direction=="Horizontal" and y>0 and Square.get_letterTile()==None and hand:
            print("left play="+play)
            print(hand)
            print("i="+hand[m])
            if y>0:
                if wordCheckerReversed.check_word(play+hand[m]) and Board[x][y-1].get_letterTile==None and wordCheckerReversed.check_word(play+hand[m]):
                    words.append((play+hand[m])[::-1])
                    positions.append( [y,temppositions[0][1]])
                    temppositions.pop(0)
                    print("Reversed True")
                if wordCheckerReversed.dictionary.t.has_subtrie(play+hand[m])==True and cross_check(hand[m],"Horizontal",Board,x,y):
                    temp=hand[m]
                    hand.pop(m)
                    ExtendLeft(Board[x][y-1],Board,hand,play+temp,Direction,words,x,y-1,positions,temppositions)
                    hand.insert(m,temp)
                    print("Appended")
            if y==0 and wordCheckerReversed.check_word(play+hand[m]) and wordCheckerReversed.check_word(play+hand[m]):
                words.append((play+hand[m])[::-1])
                positions.append([y,temppositions[0][1]])
                temppositions.pop(0)
                print("Reversed True")



def wordSearch(Square,Board,hand,play,Direction,words,x,y):
    lefttrail=None
    temppositions=[]
    positions=[]
    allsuffixes=[]
    allhands=[]
    for i in range(0,len(hand)):
        hand[i]=hand[i].upper()
    if Direction=="Vertical":
        if Board[x-1][y].get_letterTile()!=None:
            lefttrail=1
        ExtendRight(Square,Board,hand,play,Direction,allsuffixes,allhands,words,x,y,lefttrail,x,positions,temppositions)
    if Direction=="Horizontal":
        if Board[x][y-1].get_letterTile()!=None:
            lefttrail=1
        ExtendRight(Square,Board,hand,play,Direction,allsuffixes,allhands,words,x,y,lefttrail,y,positions,temppositions)
    if Direction=="Vertical" and x>0:
        for i in range(0,len(allsuffixes)):
            play=allsuffixes[i]
            hand=allhands[i]
            ExtendLeft(Board[x-1][y],Board,hand,play,Direction,words,x-1,y,positions,temppositions)
    if Direction=='Horizontal' and y>0:
        for i in range(0,len(allsuffixes)):
            play=allsuffixes[i]
            hand=allhands[i]
            ExtendLeft(Board[x][y-1],Board,hand,play,Direction,words,x,y-1,positions,temppositions)
    print(words)
    print(positions)
    
    


def DictionaryGADDAG(filename):
    with open (filename,"r") as file:
        words=file.readlines()
    words=[word.rstrip() for word in words]
    file = open("revdictionary.txt","w")
    array=[]
    for k in words:
        GADDAGAdder(k,array)
    for i in array:
        file.write(i+"\n")
    file.close()


def cross_check(Letter,Direction,Board,x,y):
    pass
    word=Letter
    print("Test")
    if Direction=="Horizontal":
        j=1
        while(y<14):
            if Board[x][y+j].get_letterTile()==None:
                 break
            else:
                 word=word+Board[x][y+j].get_letterTile().get_letter()
                 j=j+1
        j=1
        while(y>0):
            if Board[x][y-j].get_letterTile()==None:
                break
            else:
                word=Board[x][y-j].get_letterTile().get_letter()+word
                j=j+1
        if len(word)<=1:
            return True
        else:
            return wordChecker.check_word(word)
    if Direction=="Vertical":
        j=1
        while(x<14):
            
            if Board[x+j][y].get_letterTile()==None:
                 break
            else:
                 word=word+Board[x+j][y].get_letterTile().get_letter()
                 j=j+1
        j=1
        while(x>0):
            if Board[x-j][y].get_letterTile()==None:
                break
            else:
                word=word+Board[x-j][y].get_letterTile().get_letter()
                j=j+1
        if len(word)<=1:
            return True
        else:
            return wordChecker.check_word(word)

DictionaryGADDAG("dictionary.txt")
#DictionaryReversal("dictionary.txt")


print((wordChecker.dictionary.t.has_subtrie("AD")))



            





