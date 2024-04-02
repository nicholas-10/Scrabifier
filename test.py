from game import *
def test_case(print_board = False):
    """
    test cases for point checking logic. print_board argument to set whether to print board of not
    To create own test cases:
    Define a play, for example play = [LetterTile("O", 2, 11), LetterTile("B", 2, 8), LetterTile("O", 2, 9)]
    This specifies where the tiles are placed
    set:
    points = (b.play_word(play))
    Use to check if points equals proper value:
    ("returns " +str(points) + " which is " + str(points == 13))
    or use the following if the play is not valid
    ("returns " +str(points) + " which is " + str(True if points == -1 else False))
    """
    word = "ENTAILS"
    x  = 7
    y = 7
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        x += 1
    b = Board()
    points = (b.play_word(play))
    print("ENTAILS Horizontal starting at Center " +  "returns " +str(points) + " which is " + str(points == 58))

    b.print_board() if print_board else None
    word = "NGLISH"
    x  = 7
    y = 8
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        y += 1
    points = (b.play_word(play))
    print("ENGLISH Vertical starting at Center " + "returns " +str(points) + " which is " + str(points == 12))
    b.print_board() if print_board else None

    word = "DOMI"
    x  = 8
    y = 3
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        y += 1
    y += 1
    play.append(LetterTile("O", x, y))
    points = (b.play_word(play))
    print("DOMINO Vertical starting at (8, 3)  and NO at (7, 8) " + "returns " +str(points) + " which is " + str(points == 14))
    b.print_board() if print_board else None

    word = "ON"
    x  = 13
    y = 8
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        x += 1
    points = (b.play_word(play))

    print("ON Horizontal starting at (13, 8) " + "returns " +str(points) + " which is " + str(points == 4))
    b.print_board() if print_board else None

    word = "RUNNING"
    x  = 0
    y = 12
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        x += 1
    points = b.play_word(play)
    print("RUNNINGS Horizontal starting at (0, 12) " + "returns " +str(points) + " which is " + str(points == 72))
    b.print_board() if print_board else None

    word = "GRANDIO"
    x  = 13
    y = 0
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        y += 1
    points = b.play_word(play)
    print("GRANDIOSO Vertical starting at (13, 0) " + "returns " +str(points) + " which is " + str(points == 76))
    b.print_board() if print_board else None

    word = "RENT"
    x  = 0
    y = 0
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        y += 1
    points = b.play_word(play)
    print("RENT Vertical starting at (0, 0) " + "returns " +str(points) + " which is " + str(True if points == -1 else False))
    b.print_board() if print_board else None

    word = "RENT"
    x  = 3
    y = 0
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        x += 1
    points = b.play_word(play)
    print("ROLL Vertical starting at (3, 0) " + "returns " +str(points) + " which is " + str(True if points == -1 else False))
    b.print_board() if print_board else None

    word = "BENT"
    x  = 14
    y = 10
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        y += 1
    points = b.play_word(play)
    print("BENT Vertical starting at (14, 10) " + "returns " +str(points) + " which is " + str(True if points == -1 else False))
    b.print_board() if print_board else None

    word = "SENT"
    x  = 9
    y = 14
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        x += 1
    points = b.play_word(play)
    print("SENT Vertical starting at (14, 10) " + "returns " +str(points) + " which is " + str(True if points == -1 else False))
    b.print_board() if print_board else None

    word = "A"
    x  = 14
    y = 2
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
        x += 1
    points = b.play_word(play)
    print("AA Horizontal starting at (14, 2) " + "returns " +str(points) + " which is " + str(points == 2))
    b.print_board() if print_board else None

    word = "N"
    x  = 11
    y = 8
    play = []
    for l in word:
        play.append(LetterTile(l, x, y))
    points = b.play_word(play)
    print("IN Vertical starting at (11, 8) " + "returns " +str(points) + " which is " + str(points == 2))
    b.print_board() if print_board else None

    play = [LetterTile("M", 11, 3), LetterTile("E", 9, 3), LetterTile("O", 12, 3)]
    points = b.play_word(play)
    print("DE - MON Horizontal starting at (8, 3) " + "returns " +str(points) + " which is " + str(True if points == -1 else False))
    b.print_board() if print_board else None

    play = [LetterTile("O", 2, 11), LetterTile("B", 2, 8), LetterTile("O", 2, 9)]
    points = b.play_word(play)
    print("BO - ON Vertical starting at (2, 8) " + "returns " +str(points) + " which is " + str(True if points == -1 else False))
    b.print_board() if print_board else None

    play = [LetterTile("J", 0, 10), LetterTile("A", 0, 11)]
    points = b.play_word(play)
    print("JA - R Vertical starting at (0, 10) " + "returns " +str(points) + " which is " + str(points == 11))
    b.print_board() if print_board else None

    play = [LetterTile("A", 2, 11), LetterTile("J", 2, 10), LetterTile("K", 2, 13)]
    points = b.play_word(play)
    print("JA - N - K Vertical starting at (2, 10) " + "returns " +str(points) + " which is " + str(True if points == -1 else False))
    b.print_board() if print_board else None

    play = [LetterTile("O", 12, 1), LetterTile("O", 9, 3)]
    points = b.play_word(play)
    print("O - O Vertical starting at (12, 1) " + "returns " +str(points) + " which is " + str(True if points == -1 else False))
    b.print_board() if print_board else None

    play = [LetterTile("O", 9, 3), LetterTile("O", 12, 1)]
    points = b.play_word(play)
    print("DO and OR Non-continous " + "returns " +str(points) + " which is " + str(True if points == -1 else False))
    b.print_board() if print_board else None

    play = [LetterTile("N", 8, 11), LetterTile("N", 9, 11)]
    points = b.play_word(play)
    print("INN Horizontal Starting at (7, 11) " + "returns " +str(points) + " which is " + str(points == 3))
    b.print_board() if print_board else None

# test_case(print_board=False)

def test_case_2():
    b = Board()
    b.print_board()

test_case_2()

def test_player():
    pass

def test_exchange():
    b = Bag()
    print(b.bag)
    temp = (b.exchange(3, [LetterTile("O", 12, 1), LetterTile("O", 12, 1), LetterTile("O", 9, 3)]))
    for t in temp:
        print(t, end="")
    print(b.bag)
    print()

    b = Bag()
    b.bag = {'A': 9, 'B': 2, 'C': 2, 'D': 4, 'E': 12, 'F': 2, 'G': 3, 'H': 2, 'I': 9, 'J': 1, 'K': 1, 'L': 4, 'M': 2, 'N': 6, 'O': 8, 'P': 2, 'Q': 1, 'R': 6, 'S': 4, 'T': 6, 'U': 4, 'V': 2, 'W': 2, 'X': 1, 'Y': 2, '?': 2}
    print(b.bag)
    
    temp = (b.exchange(5, [LetterTile("Q", 12, 1), LetterTile("Z", 12, 1), LetterTile("O", 12, 1), LetterTile("O", 12, 1), LetterTile("O", 9, 3)]))
    for t in temp:
        print(t, end="")
    print(b.bag)

    print()
    b = Bag()
    print(b.bag)

    temp = (b.exchange(7, [LetterTile("O", 12, 1), LetterTile("O", 12, 1), LetterTile("O", 12, 1), LetterTile("O", 12, 1),LetterTile("O", 12, 1), LetterTile("O", 12, 1), LetterTile("O", 9, 3)]))
    for t in temp:
        print(t, end="")
    print(b.bag)

# test_exchange()