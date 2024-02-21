import util
import random
from constants import *
class Dictionary:
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
class BoardTile:
    def __init__(self, type):
        self.type = type
        self.letterTile = None
    def set_letterTile(self, letterTile):
        self.letterTile = letterTile
    def get_letterTile(self):
        return self.letterTile
    def get_letter(self):
        return self.letterTile.get_letter()
    def get_type(self):
        return self.type
class LetterTile:
    def __init__(self, letter, x = -1, y = -1):
        self.letter = letter
        self.x = x
        self.y = y
        self.point = SCRABBLE_LETTER_POINTS[letter]
        self.put_on_round = -1
    def set_x(self, x):
        self.x = x
    def set_y(self, y):
        self.y = y
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_letter(self):
        return self.letter
    def get_points(self):
        return self.point
    def get_put_on_round(self):
        return self.put_on_round
    def set_put_on_round(self, put_on_round):
        self.put_on_round = put_on_round
class Bag:
    def __init__(self):
        self.bag = {}
        # deep copy
        self.remainingTiles = 0
        for k, v in INITIAL_SCRABBLE_BAG_COUNT.items():
            self.remainingTiles += v
            self.bag[k] = v
    def get_n_tiles(self, n):
        """
        Gets n LetterTile objects, returns list of the LetterTile objects
        """
        keys = list(self.bag.keys())
        # for k in self.bag.keys():
        #     keys.append(k)
        sampled_words = []
        for i in range(n):
            sample = random.choice(keys)
            self.bag[sample] -= 1
            self.remainingTiles -= 1
            sampled_words.append(sample)
            if self.bag[sample] == 0:
                self.bag.pop(sample)
        return sampled_words

class Board:
    def __init__(self):
        self.board = [
            [BoardTile(TW), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(TW)],
            [BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT)],
            [BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT)],
            [BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(DL)],
            [BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(RT)],
            [BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT)],
            [BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT)],
            [BoardTile(TW), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(CT), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(TW)],
            [BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT)],
            [BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT)],
            [BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(RT)],
            [BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(DL)],
            [BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT)],
            [BoardTile(RT), BoardTile(DW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DW), BoardTile(RT)],
            [BoardTile(TW), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(TW), BoardTile(RT), BoardTile(RT), BoardTile(RT), BoardTile(DL), BoardTile(RT), BoardTile(RT), BoardTile(TW)]
            ]
        self.playerToMove = 1
        self.round = 1
        self.dictionary = Dictionary("dictionary.txt")
    def set_letterTile(self, LetterTile):
        self.board[LetterTile.get_y()][LetterTile.get_x()].set_letterTile(LetterTile)
    def get_direction(self, play):
        direction = ""
        if len(play) == 1:
            direction = "neutral"
        else:
            if (play[0].get_x() - play[1].get_x()) != 0:
                direction = "horizontal"
            elif (play[0].get_y() - play[1].get_y()) != 0:
                direction = "vertical"
        return direction
    def check_valid_play(self, play, print_resulting_words = False):
        """
        checks if play is valid or not given the state of the board. play is a list of LetterTile objects. Returns True or False
        """
           
        for p in play:
            self.set_letterTile(p)
            p.set_put_on_round(self.round)
        words = []
        # verify in range
        if (play[0].get_x() < 0 or play[0].get_y() < 0 or play[-1].get_x() > MAX_YINDEX or play[-1].get_y() > MAX_YINDEX):
            print("NOT IN RANGE")
            return False

        direction = self.get_direction(play)

        # verify that word is connected to other word
        is_connected = False
        if self.round == 1:
            is_on_center = False
            for p in play:
                if p.get_x() == CENTER_X and p.get_y() == CENTER_Y:
                    is_on_center = True
                    break
            if not is_on_center:
                return False
            elif is_on_center:
                is_connected = True        
        if play[0].get_y() != 0:
            if self.board[play[0].get_y() - 1][play[0].get_x()].get_letterTile() != None:
                is_connected = True
        
        if direction == "horizontal" or direction == "neutral":
            if play[0].get_x() != 0:
                if self.board[play[0].get_y()][play[0].get_x() - 1].get_letterTile() != None:
                    is_connected = True
            if play[-1].get_x() != MAX_XINDEX:
                if self.board[play[-1].get_y()][play[-1].get_x()  + 1].get_letterTile() != None:
                    is_connected = True
            for i in range(0, len(play)):
                if play[i].get_y() != MAX_YINDEX:
                    if self.board[play[i].get_y() + 1][play[i].get_x()].get_letterTile() != None:
                        is_connected = True
                if play[i].get_y() != 0:
                    if self.board[play[i].get_y() - 1][play[i].get_x()].get_letterTile() != None:
                        is_connected = True
        elif direction == "vertical":
            if play[0].get_y() != 0:
                if self.board[play[0].get_y() - 1][play[0].get_x()].get_letterTile() != None:
                    is_connected = True
            if play[-1].get_y() != MAX_YINDEX:
                if self.board[play[-1].get_y() + 1][play[-1].get_x()].get_letterTile() != None:
                    is_connected = True
            for i in range(0, len(play)):
                if play[i].get_x() != MAX_XINDEX:
                    if self.board[play[i].get_y()][play[i].get_x() + 1].get_letterTile() != None:
                        is_connected = True
                if play[i].get_x() != 0:
                    if self.board[play[i].get_y()][play[i].get_x() - 1].get_letterTile() != None:
                        is_connected = True
        if is_connected == False:
            return False
        if direction == "horizontal":
            count = p.get_x()
            while (self.board[p.get_y()][count].get_letterTile() != None):
                count -= 1
                if count < MIN_XRANGE:
                    count = -1
                    break
            count += 1
            word = ""
            while (self.board[p.get_y()][count].get_letterTile() != None):
                word += self.board[p.get_y()][count].get_letter()
                count += 1
                if count == MAX_XRANGE:
                    break
            if (len(word) != 1):
                words.append(word)
            for p in play:
                count = p.get_y()
                while (self.board[count][p.get_x()].get_letterTile() != None):
                    count -= 1
                    if count < MIN_YRANGE:
                        count = -1
                        break
                count += 1
                word = ""
                while (self.board[count][p.get_x()].get_letterTile() != None):
                    word += self.board[count][p.get_x()].get_letter()
                    count += 1
                    if count == MAX_YRANGE:
                        break
                if (len(word) != 1):
                    words.append(word)
            
            # check if connected
            over = []
            for p in play:
                over.append(p)
            count = p.get_x()
            while (self.board[p.get_y()][count].get_letterTile() != None):
                count -= 1
                if count < MIN_XRANGE:
                    count = -1
                    break 
            count += 1
            while (self.board[p.get_y()][count].get_letterTile() != None):
                for o in over:
                    if o.get_x() == self.board[p.get_y()][count].get_letterTile().get_x() and o.get_y() == self.board[p.get_y()][count].get_letterTile().get_y():
                        over.remove(o)                        
                        break
                count += 1
                if count == MAX_XRANGE:
                    break   
            if len(over) != 0:
                return False
                

        elif direction == "vertical":
            count = p.get_y()
            while (self.board[count][p.get_x()].get_letterTile() != None):
                count -= 1
                if count < MIN_YRANGE:
                    count = -1
                    break

            count += 1
            word = ""
            while (self.board[count][p.get_x()].get_letterTile() != None):
                word += self.board[count][p.get_x()].get_letter()
                count += 1
                if count == MAX_YRANGE:
                    break
            if (len(word) != 1):
                words.append(word)

            for p in play:
                count = p.get_x()
                while (self.board[p.get_y()][count].get_letterTile() != None):
                    count -= 1
                    if count < MIN_XRANGE:
                        count = -1
                        break

                count += 1
                word = ""
                while (self.board[p.get_y()][count].get_letterTile() != None):
                    word += self.board[p.get_y()][count].get_letter()
                    count += 1
                    if count == MAX_XRANGE:
                        break
                if (len(word) != 1):
                    words.append(word)
            # check if connected
            over = []
            for p in play:
                over.append(p)
            count = p.get_y()
            while (self.board[count][p.get_x()].get_letterTile() != None):
                count -= 1
                if count < MIN_YRANGE:
                    count = -1
                    break 
            count += 1
            while (self.board[count][p.get_x()].get_letterTile() != None):
                for o in over:
                    if o.get_x() == self.board[count][p.get_x()].get_letterTile().get_x() and o.get_y() == self.board[count][p.get_x()].get_letterTile().get_y():
                        over.remove(o)                        
                        break
                count += 1
                if count == MAX_YRANGE:
                    break   
            if len(over) != 0:
                return False
        else:
            count = p.get_y()
            while (self.board[count][p.get_x()].get_letterTile() != None):
                count -= 1
                if count < MIN_YRANGE:
                    count = -1
                    break

            count += 1
            word = ""
            while (self.board[count ][p.get_x()].get_letterTile() != None):
                word += self.board[count][p.get_x()].get_letter()
                count += 1
                if count == MAX_XRANGE:
                    break
            if len(word) != 1:
                words.append(word)

            count = p.get_x()
            while (self.board[p.get_y()][count].get_letterTile() != None):
                count -= 1
                if  count < MIN_YRANGE:
                    count = -1
                    break
            count += 1
            word = ""
            while (self.board[p.get_y()][count].get_letterTile() != None):
                word += self.board[p.get_y()][count].get_letter()
                count += 1
                if count == MAX_XRANGE:
                    break
            if len(word) != 1:
                words.append(word)
        if print_resulting_words:
            print(words)
        for word in words:
            if self.dictionary.check_word(word) == False:
                return False
        if (len(words) == 0):
            return False
        return True
    def calculate_points(self, play):
        """
        Calculates score from a valid play. Returns score as an integer if valid or -1 if not
        """
        direction = self.get_direction(play)
        points = 0
        if direction == "horizontal":
            p = play[0]
            count = p.get_x()
            while (self.board[p.get_y()][count].get_letterTile() != None):
                count -= 1
                if count < MIN_XRANGE:
                    count = -1
                    break
            count += 1
            multiplier = 1
            
            while (self.board[p.get_y()][count].get_letterTile() != None):
                if self.board[p.get_y()][count].get_letterTile().get_put_on_round() == self.round:
                    if self.board[p.get_y()][count].get_type() == DL:
                        points += (2 * self.board[p.get_y()][count].get_letterTile().get_points())
                    elif self.board[p.get_y()][count].get_type() == TL:
                        points += (3 * self.board[p.get_y()][count].get_letterTile().get_points())
                    elif self.board[p.get_y()][count].get_type() == DW:
                        points += ( self.board[p.get_y()][count].get_letterTile().get_points())
                        multiplier *= 2
                    elif self.board[p.get_y()][count].get_type() == TW:
                        points += ( self.board[p.get_y()][count].get_letterTile().get_points())
                        multiplier *= 3
                    elif self.board[p.get_y()][count].get_type() == RT or self.board[p.get_y()][count].get_type() == CT:
                        points += ( self.board[p.get_y()][count].get_letterTile().get_points())
                else:
                    points += ( self.board[p.get_y()][count].get_letterTile().get_points())
                count += 1
                if count == MAX_XRANGE:
                    break
            points *= multiplier
            for p in play:
                count = p.get_y()
                while (self.board[count][p.get_x()].get_letterTile() != None):
                    count -= 1
                    if count < MIN_YRANGE:
                        count = -1
                        break
                count += 1
                multiplier = 1
                temp_points = 0
                l = 0
                while (self.board[count][p.get_x()].get_letterTile() != None):
                    l += 1
                    if self.board[count][p.get_x()].get_letterTile().get_put_on_round() == self.round:
                        if self.board[count][p.get_x()].get_type() == DL:
                            temp_points += (2 * self.board[count][p.get_x()].get_letterTile().get_points())
                        elif self.board[count][p.get_x()].get_type() == TL:
                            temp_points += (3 * self.board[count][p.get_x()].get_letterTile().get_points())
                        elif self.board[count][p.get_x()].get_type() == DW:
                            temp_points +=  (self.board[count][p.get_x()].get_letterTile().get_points())
                            multiplier *= 2
                        elif self.board[count][p.get_x()].get_type() == TW:
                            temp_points +=  (self.board[count][p.get_x()].get_letterTile().get_points())
                            multiplier *= 3
                        elif self.board[count][p.get_x()].get_type() == RT or self.board[count][p.get_x()].get_type() == CT:
                            temp_points +=  self.board[count][p.get_x()].get_letterTile().get_points()
                    else:
                        temp_points +=  self.board[count][p.get_x()].get_letterTile().get_points()
                    count += 1
                    if count == MAX_YRANGE:
                        break
                if l != 1:
                    points = points + (temp_points * multiplier)
            if len(play) == 7:
                points += 50


        elif direction == "vertical":
            p = play[0]
            count = p.get_y()
            while (self.board[count][p.get_x()].get_letterTile() != None):
                count -= 1
                if count < MIN_YRANGE:
                    count = -1
                    break
            count += 1
            multiplier = 1
            while (self.board[count][p.get_x()].get_letterTile() != None):
                if self.board[count][p.get_x()].get_letterTile().get_put_on_round() == self.round:
                    
                    if self.board[count][p.get_x()].get_type() == DL:
                        points += (2 * self.board[count][p.get_x()].get_letterTile().get_points())
                    elif self.board[count][p.get_x()].get_type() == TL:
                        points += (3 * self.board[count][p.get_x()].get_letterTile().get_points())
                    elif self.board[count][p.get_x()].get_type() == DW:
                        points += ( self.board[count][p.get_x()].get_letterTile().get_points())
                        multiplier *= 2
                    elif self.board[count][p.get_x()].get_type() == TW:
                        points += ( self.board[count][p.get_x()].get_letterTile().get_points())
                        multiplier *= 3
                    elif self.board[count][p.get_x()].get_type() == RT or self.board[count][p.get_x()].get_type() == CT:
                        points += ( self.board[count][p.get_x()].get_letterTile().get_points())
                else:
                    points += ( self.board[count][p.get_x()].get_letterTile().get_points())
                count += 1
                if count == MAX_YRANGE:
                    break
            
            points *= multiplier
            for p in play:

                count = p.get_x()
                while (self.board[p.get_y()][count].get_letterTile() != None):
                    count -= 1
                    if count < MIN_XRANGE:
                        count = -1
                        break

                count += 1
                temp_points = 0
                multiplier = 1

                l = 0
                while (self.board[p.get_y()][count].get_letterTile() != None):
                    l += 1
                    if self.board[p.get_y()][count].get_letterTile().get_put_on_round() == self.round:
                        if self.board[p.get_y()][count].get_type() == DL:
                            temp_points += (2 * self.board[p.get_y()][count].get_letterTile().get_points())
                        elif self.board[p.get_y()][count].get_type() == TL:
                            temp_points += (3 * self.board[p.get_y()][count].get_letterTile().get_points())
                        elif self.board[p.get_y()][count].get_type() == DW:
                            temp_points += ( self.board[p.get_y()][count].get_letterTile().get_points())
                            multiplier *= 2
                        elif self.board[p.get_y()][count].get_type() == TW:
                            temp_points += ( self.board[p.get_y()][count].get_letterTile().get_points())
                            multiplier *= 3
                        elif self.board[p.get_y()][count].get_type() == RT or self.board[p.get_y()][count].get_type() == CT:
                            temp_points += ( self.board[p.get_y()][count].get_letterTile().get_points())
                    else:
                        temp_points += ( self.board[p.get_y()][count].get_letterTile().get_points())
                    count += 1
                    if count == MAX_XRANGE:
                        break
                if l != 1:
                    points = points + (multiplier * temp_points)
            if len(play) == 7:
                points += 50
        elif  direction == "neutral":
            p = play[0]
            count = p.get_y()
            while (self.board[count][p.get_x()].get_letterTile() != None):
                count -= 1
                if count < MIN_YRANGE:
                    count = -1
                    break
            count += 1
            multiplier = 1
            temp_points = 0
            l = 0
            while (self.board[count][p.get_x()].get_letterTile() != None):
                l += 1
                if self.board[count][p.get_x()].get_letterTile().get_put_on_round() == self.round:

                    if self.board[count][p.get_x()].get_type() == DL:
                        temp_points += (2 * self.board[count][p.get_x()].get_letterTile().get_points())
                    elif self.board[count][p.get_x()].get_type() == TL:
                        temp_points += (3 * self.board[count][p.get_x()].get_letterTile().get_points())
                    elif self.board[count][p.get_x()].get_type() == DW:
                        temp_points += ( self.board[count][p.get_x()].get_letterTile().get_points())
                        multiplier *= 2
                    elif self.board[count][p.get_x()].get_type() == TW:
                        temp_points += ( self.board[count][p.get_x()].get_letterTile().get_points())
                        multiplier *= 3
                    elif self.board[count][p.get_x()].get_type() == RT or self.board[count][p.get_x()].get_type() == CT:
                        temp_points += ( self.board[count][p.get_x()].get_letterTile().get_points())
                else:
                    temp_points += ( self.board[count][p.get_x()].get_letterTile().get_points())
                count += 1
                if count == MAX_YRANGE:
                    break
            if l != 1:
                points += (temp_points * multiplier)
            # points *= multiplier
            p = play[0]
            count = p.get_x()
            while (self.board[p.get_y()][count].get_letterTile() != None):
                count -= 1
                if count < MIN_XRANGE:
                    count = -1
                    break
            count += 1
            multiplier = 1
            temp_points = 0
            l = 0
            while (self.board[p.get_y()][count].get_letterTile() != None):
                l += 1
                if self.board[p.get_y()][count].get_letterTile().get_put_on_round() == self.round:
                    if self.board[p.get_y()][count].get_type() == DL:
                        temp_points += 2 * self.board[p.get_y()][count].get_letterTile().get_points()
                    elif self.board[p.get_y()][count].get_type() == TL:
                        temp_points += 3 * self.board[p.get_y()][count].get_letterTile().get_points()
                    elif self.board[p.get_y()][count].get_type() == DW:
                        temp_points +=  self.board[p.get_y()][count].get_letterTile().get_points()
                        multiplier *= 2
                    elif self.board[p.get_y()][count].get_type() == TW:
                        temp_points +=  self.board[p.get_y()][count].get_letterTile().get_points()
                        multiplier *= 3
                    elif self.board[p.get_y()][count].get_type() == RT or self.board[p.get_y()][count].get_type() == CT:
                        temp_points +=  self.board[p.get_y()][count].get_letterTile().get_points()
                else:
                    temp_points +=  self.board[p.get_y()][count].get_letterTile().get_points()
                count += 1
                if count == MAX_XRANGE:
                    break
            if l != 1:
                points += (multiplier * temp_points)

        return points
    def play_word(self, play):
        """
        Accepts a list with LetterTiles to determine where the play is made
        Returns number of points
        """
        t = False
        t = self.check_valid_play(play)
        
        # "retakes" letter tiles if the word is not valid
        if t == False:
            for p in play:
                self.board[p.get_y()][ p.get_x()].set_letterTile(None)
        self.playerToMove = 1 + ((1 + self.round) % 2)
        pts = 0
        if t == True:
            pts =  (self.calculate_points(play))
        else:
            pts = -1
        self.round += 1
        return pts
    def print_board(self):
        print("  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
        for i, row in enumerate(self.board):
            print(str(i % 10) + " ", end="")
            for t in row:
                if t.get_letterTile() == None:
                    print("- ", end="")
                else:
                    print(t.get_letter() + " ", end="")
            print("")
        print("")


def MainLoop():
    d = Dictionary("dictionary.txt")
    print("LOOP")


