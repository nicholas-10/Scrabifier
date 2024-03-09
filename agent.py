class Player:
    def __init__(self, player, hand, board):
        self.player = player
        self.score = 0
        self.hand = hand
        self.board = board
    def get_score(self):
        return self.score
    def set_score(self, score):
        self.score = score
    def get_hand(self):
        return self.hand
    def set_hand(self, hand):
        self.hand = hand
    def print_hand(self):
        print("(", end = "")
        for h in self.hand:
            print(h.get_letter(), end = "")
            print(", ", end = "")
        print(")")