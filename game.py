import util
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
class LetterTile:
    def __init__(self, letter, x = -1, y = -1):
        self.letter = letter
        self.x = x
        self.y = y
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
    def check_valid_play(self, play):
        """
        checks if play is valid or not given the state of the board. play is a list of LetterTile objects
        note: there is a bug where you cant play single letter as openning move. Should fix later
        """
        if self.round == 1:
            is_on_center = False
            for p in play:
                if p.get_x() == CENTER_X and p.get_y() == CENTER_Y:
                    is_on_center = True
                    break
            if not is_on_center:
                return False
        for p in play:
            self.set_letterTile(p)
        words = []
        direction = ""
        if len(play) == 1:
            direction = "Neutral"
        else:
            if play[0].get_x() < 0 or play[0].get_y() < 0 or play[-1].get_x() > MAX_YRANGE or play[-1].get_y() > MAX_YRANGE:
                return False
            if (play[0].get_x() - play[1].get_x()) != 0:
                direction = "horizontal"
            elif (play[0].get_y() - play[1].get_y()) != 0:
                direction = "vertical"
        if direction == "horizontal":
            count = p.get_x()
            while (self.board[p.get_y()][count].get_letterTile() != None):
                count -= 1
                print(count)
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
        else:
            count = p.get_y()
            while (self.board[count][p.get_x()].get_letterTile() != None):
                count -= 1
            count += 1
            word = ""
            while (self.board[count ][p.get_x()].get_letterTile() != None):
                word += self.board[count][p.get_x()].get_letter()
                count += 1
            if (len(word) != 1):
                words.append(word)

            count = p.get_x()
            while (self.board[p.get_y()][count].get_letterTile() != None):
                count -= 1
            count += 1
            word = ""
            while (self.board[p.get_y()][count].get_letterTile() != None):
                word += self.board[p.get_y()][count].get_letter()
                count += 1
            if (len(word) != 1):
                words.append(word)
        print(words)
        for word in words:
            if self.dictionary.check_word(word) == False:
                return False
        if (len(words) == 0):
            return False
        return True
    def calculate_points(self, board, play):
        """
        Calculates score from a valid play
        """
    def play_word(self, play):
        """
        Accepts a list with LetterTiles to determine where the play is made
        Returns number of points
        """

        t = self.check_valid_play(play)
        self.round += 1
        self.playerToMove = 1 + ((1 + self.round) % 2)
        return t
    def print_board(self):
        for row in self.board:
            for t in row:
                if t.get_letterTile() == None:
                    print("0 ", end="")
                else:
                    print(t.get_letter() + " ", end="")
            print("")
# put into separate file "test_cases.py" later   
def test_case():
    word = "ENTAILS"
    x  = 7
    y = 7
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        x += 1
    b = Board()
    print("ENTAILS Horizontal starting at Center " + str(b.play_word(play)))
    b.print_board()
    word = "NGLISH"
    x  = 7
    y = 8
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        y += 1
    print("ENGLISH Vertical starting at Center " + str(b.play_word(play)))
    b.print_board()

    word = "DOMI"
    x  = 8
    y = 3
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        y += 1
    y += 1
    play.append(LetterTile("O", x, y))

    print("DOMINO Vertical starting at (8, 3) " + str(b.play_word(play)))
    b.print_board()

    word = "ON"
    x  = 13
    y = 8
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        x += 1
    print("ON Horizontal starting at (13, 8) " + str(b.play_word(play)))
    b.print_board()

    word = "RUNNING"
    x  = 0
    y = 12
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        x += 1
    print("RUNNINGS Horizontal starting at (0, 12) " + str(b.play_word(play)))
    b.print_board()

    word = "GRANDIO"
    x  = 13
    y = 0
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        y += 1
    print("GRANDIOSO Vertical starting at (13, 0) " + str(b.play_word(play)))
    b.print_board()

test_case()
def MainLoop():
    d = Dictionary("dictionary.txt")
    print("LOOP")


