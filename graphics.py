from tkinter import *
from tkinter import ttk
from constants import *
from graphics_wild import open_wild_window
from graphics_exchange import open_exchange_window
import random
import copy
import sys

player_score = 0

ori_hand = []
hand = ori_hand.copy()

board_frame = None
bar_frame = None

class DragTileManager():
    def __init__(self, window, frame, board, b):
        self.window = window
        self.board = board
        self.tile = None
        self.start_x = 0
        self.start_y = 0
        self.frame = frame
        self.letters = {}
        self.b = b

    def add_tile(self, tile, letter):
        tile.bind("<ButtonPress-1>", self.on_drag_start)
        tile.bind("<B1-Motion>", self.on_drag)
        tile.bind("<ButtonRelease-1>", self.on_drag_end)
        tile.configure(cursor="hand1")
        self.letters[tile] = letter

    def on_drag_start(self, event):
        self.tile = event.widget
        self.ori_x = event.widget.winfo_x()
        self.ori_y = event.widget.winfo_y()
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        if self.tile:
            x = event.widget.winfo_x() - self.start_x + event.x
            y = event.widget.winfo_y() - self.start_y + event.y

            board_width = self.frame.winfo_width()
            board_height = self.frame.winfo_height()

            x = min(max(x, 0) - 9, board_width - 18)
            y = min(max(y, 0) - 9, board_height - 18)

            event.widget.place_configure(x=x, y=y)

    def set_wild_letter(self, event, letter, snap_x, snap_y, grid_col, grid_row):
        print("SET LETTER TO", letter)
        self.letters[event.widget].set_letter(letter)
        print(f"Tile '{self.letters[event.widget].get_letter()}' placed at board:", grid_col, grid_row)
        self.b.add_play(self.letters[event.widget].get_letter(), grid_col, grid_row)
        self.board[grid_row][grid_col].set_letterTile_split(self.letters[event.widget].get_letter(), grid_col, grid_row)
        grid_col, grid_row = self.ori_x // SQUARE_SIZE, self.ori_y // SQUARE_SIZE
        if grid_row == 15:
            print(f"Tile '{self.letters[event.widget].get_letter()}' gone from hand:", grid_col - 4)
            hand[grid_col - 4] = "-"
        else:
            print(f"Tile '{self.letters[event.widget].get_letter()}' gone from board:", grid_col, grid_row)
            self.b.remove_play(grid_col, grid_row)
            self.board[grid_row][grid_col].set_letterTile(None)
        event.widget.place_configure(x=snap_x, y=snap_y)
        self.tile = None

    def on_drag_end(self, event):
        if self.tile:
            x, y = event.widget.winfo_x(), event.widget.winfo_y()
            board_width, board_height = self.frame.winfo_width(), self.frame.winfo_height()
            grid_col, grid_row = min(x // SQUARE_SIZE, 14), min(y // SQUARE_SIZE, 14)
            if y // SQUARE_SIZE == 15 and 4 <= x // SQUARE_SIZE <= 10:
                grid_col, grid_row = x // SQUARE_SIZE, 15
                if hand[grid_col - 4] != "-":
                    grid_col, grid_row = self.ori_x // SQUARE_SIZE, self.ori_y // SQUARE_SIZE
                    snap_x, snap_y = min(max(grid_col * SQUARE_SIZE, 0), board_width - TILE_SIZE) + 2.5, (min(max(grid_row * SQUARE_SIZE, 0), board_height - TILE_SIZE) + 12.5) if self.ori_y // SQUARE_SIZE == 15 else min(max(grid_row * SQUARE_SIZE, 0), board_height - TILE_SIZE) + 2.5
                else:
                    if(self.letters[event.widget].get_points() == 0):
                        self.letters[event.widget].reset_letter()
                    print(f"Tile '{self.letters[event.widget].get_letter()}' placed at hand:", grid_col - 4)
                    hand[grid_col - 4] = self.letters[event.widget].get_letter()
                    snap_x, snap_y = min(max(grid_col * SQUARE_SIZE, 0), board_width - TILE_SIZE) + 2.5, min(max(grid_row * SQUARE_SIZE, 0), board_height - TILE_SIZE) + 12.5
                    grid_col, grid_row = self.ori_x // SQUARE_SIZE, self.ori_y // SQUARE_SIZE
                    if grid_row == 15:
                        print(f"Tile '{self.letters[event.widget].get_letter()}' gone from hand:", grid_col - 4)
                        hand[grid_col - 4] = "-"
                    else:
                        print(f"Tile '{self.letters[event.widget].get_letter()}' gone from board:", grid_col, grid_row)
                        self.b.remove_play(grid_col, grid_row)
                        self.board[grid_row][grid_col].set_letterTile(None)
                event.widget.place_configure(x=snap_x, y=snap_y)
                self.tile = None
            else:
                if self.board[grid_row][grid_col].get_letterTile():
                    grid_col, grid_row = self.ori_x // SQUARE_SIZE, self.ori_y // SQUARE_SIZE
                    snap_x, snap_y = min(max(grid_col * SQUARE_SIZE, 0), board_width - TILE_SIZE) + 2.5, (min(max(grid_row * SQUARE_SIZE, 0), board_height - TILE_SIZE) + 12.5) if self.ori_y // SQUARE_SIZE == 15 else min(max(grid_row * SQUARE_SIZE, 0), board_height - TILE_SIZE) + 2.5
                    event.widget.place_configure(x=snap_x, y=snap_y)
                    self.tile = None
                else:
                    if(self.letters[event.widget].get_points() == 0):
                        snap_x, snap_y = min(max(grid_col * SQUARE_SIZE, 0), board_width - TILE_SIZE) + 2.5, min(max(grid_row * SQUARE_SIZE, 0), board_height - TILE_SIZE) + 2.5
                        open_wild_window(self.set_wild_letter, event, snap_x, snap_y, grid_col, grid_row)
                    else:
                        print(f"Tile '{self.letters[event.widget].get_letter()}' placed at board:", grid_col, grid_row)
                        self.b.add_play(self.letters[event.widget].get_letter(), grid_col, grid_row)
                        self.board[grid_row][grid_col].set_letterTile_split(self.letters[event.widget].get_letter(), grid_col, grid_row)
                        snap_x, snap_y = min(max(grid_col * SQUARE_SIZE, 0), board_width - TILE_SIZE) + 2.5, min(max(grid_row * SQUARE_SIZE, 0), board_height - TILE_SIZE) + 2.5
                        grid_col, grid_row = self.ori_x // SQUARE_SIZE, self.ori_y // SQUARE_SIZE
                        if grid_row == 15:
                            print(f"Tile '{self.letters[event.widget].get_letter()}' gone from hand:", grid_col - 4)
                            hand[grid_col - 4] = "-"
                        else:
                            print(f"Tile '{self.letters[event.widget].get_letter()}' gone from board:", grid_col, grid_row)
                            self.b.remove_play(grid_col, grid_row)
                            self.board[grid_row][grid_col].set_letterTile(None)
                        event.widget.place_configure(x=snap_x, y=snap_y)
                        self.tile = None

def exit(w):
    w.destroy()
    sys.exit()
def pass_turn(w, b):
    w.destroy()
    b.switchPlayerToMove()
    open_window(b)
def shuffle_hand(w, b):
    global hand, ori_hand
    random.shuffle(ori_hand)
    hand = ori_hand.copy()
    w.destroy()
    open_window(b)
    
def exchange_hand(hand, b, w, ex):
    b.get_players()[b.get_playerToMove()].set_hand(hand)
    ori_hand = hand.copy()
    hand = ori_hand.copy()
    if ex:
        b.switchPlayerToMove()
    w.destroy()
    open_window(b)

def submit(w, b):
    global player_score
    if(b.check_play()):
        points = (b.play_word(b.get_play()))
        if(points != -1):
            player_score += points
        w.destroy()

        # print("  0 1 2 3 4 5 6 7 8 9 0 1 2 3 4")
        # for i, row in enumerate(b.board):
        #     print(str(i % 10) + " ", end="")
        #     for t in row:
        #         if t.get_letterTile() == None:
        #             print("- ", end="")
        #         else:
        #             print(t.get_letter() + " ", end="")
        #     print("")
        # print("")
        
        b.clear_play()
        b.print_board()
    else:
        b.clear_play()

def submit_board(w, b, board):
    submit(w, b)
    board[:] = copy.deepcopy(b.board)

def open_window(b):
    global board_frame, bar_frame, hand, ori_hand
    board = copy.deepcopy(b.board)
    ori_hand = b.get_players()[b.get_playerToMove()].get_hand()
    hand = ori_hand.copy()

    window = Tk()
    style = ttk.Style()
    window.resizable(0, 0)
    window.title("Scrabble")
    window.geometry("%dx%d%+d%+d" % (700, 750, 0, 0))

    board_frame = ttk.Frame(window)
    board_frame['padding'] = 5
    board_frame['borderwidth'] = 5
    board_frame['relief'] = 'groove'
    bar_frame = ttk.Frame(window)
    btn_frame = ttk.Frame(window)

    drag_tile_manager = DragTileManager(window, board_frame, board, b)

    board_frame.place(relx=0.5, rely=0.45, anchor = CENTER)
    bar_frame.place(x = 0, rely = 0.85, relheight = 0.05, relwidth = 1)
    btn_frame.place(x = 0, rely = 0.9, relheight = 0.05, relwidth = 1)

    btn_frame.columnconfigure((0, 1, 2, 3, 4), weight = 1, uniform = "a")
    btn_frame.rowconfigure((0), weight = 1, uniform = "a")

    style.configure("Bar.TButton", font=("Ubuntu", 10))
    shuffle_btn = ttk.Button(btn_frame, text = "Shuffle", style="Bar.TButton", command=lambda: shuffle_hand(window, b))
    exchange_btn = ttk.Button(btn_frame, text = "Exchange", style="Bar.TButton", command=lambda: open_exchange_window(exchange_hand, hand, [], b, window))
    submit_btn = ttk.Button(btn_frame, text = "Submit", style="Bar.TButton", command=lambda: submit_board(window, b, board))
    quit_btn = ttk.Button(btn_frame, text = "Quit", style="Bar.TButton", command=lambda: exit(window))

    pass_btn = ttk.Button(btn_frame, text = "Pass", style="Bar.TButton", command=lambda: pass_turn(window, b))

    shuffle_btn.grid(row = 0, column = 0)
    exchange_btn.grid(row = 0, column = 1)
    submit_btn.grid(row = 0, column = 2)
    pass_btn.grid(row = 0, column = 3)

    quit_btn.grid(row = 0, column = 4)

    style.configure("Turn.TLabel", font = ("Helvetica", 15, "bold"))
    turn_lbl = ttk.Label(bar_frame, text = f"Player 1: {b.players[0].get_score()} | Player 2: {b.players[1].get_score()}", style = "Turn.TLabel", anchor = "center")
    turn_lbl.pack()

    for row in range(len(board)):
        for col in range(len(board[row])):
            tile_type = BOARD_TILES[board[row][col].get_type()]
            color = BOARD_COLORS.get(tile_type, "beige") 
            square = Canvas(board_frame, width=SQUARE_SIZE, height=SQUARE_SIZE, bg=color, highlightthickness=0)
            if(tile_type != "RT" and tile_type != "CT"):
                square.create_text(SQUARE_SIZE // 2, SQUARE_SIZE // 2, text=tile_type, font=("Helvetica", 10))
            square.create_rectangle(0, 0, SQUARE_SIZE, SQUARE_SIZE, outline="black")
            square.grid(row=row, column=col)

    for row in range(len(board)):
        for col in range(len(board[row])):
            if(board[row][col].get_letterTile()):
                tile_type = board[row][col].get_type()
                color = BOARD_COLORS.get(tile_type, "beige") 
                square = Canvas(board_frame, width=TILE_SIZE, height=TILE_SIZE, bg="burlywood1", highlightthickness=0)
                score = SCRABBLE_LETTER_POINTS.get(board[row][col].get_letter(), 0)
                square.create_text(TILE_SIZE - 6, TILE_SIZE - 6, text=f"{score}", font=("Helvetica", 6))
                square.create_text(TILE_SIZE // 2, TILE_SIZE // 2, text=board[row][col].get_letter().upper(), font=("Helvetica", 10))
                square.create_rectangle(0, 0, TILE_SIZE, TILE_SIZE, outline="black")
                square.grid(row=row, column=col)

    board_frame.grid_rowconfigure(16, minsize=10)

    for col in range(7):
        square = Canvas(board_frame, width=SQUARE_SIZE, height=SQUARE_SIZE, bg='beige', highlightthickness=0)
        square.create_rectangle(0, 0, SQUARE_SIZE, SQUARE_SIZE, outline="black")
        square.grid(row=17, column=col+4)

    for col, letter in enumerate(hand):
        square = Canvas(board_frame, width=TILE_SIZE, height=TILE_SIZE, bg='burlywood', highlightthickness=0)
        square.create_rectangle(0, 0, TILE_SIZE, TILE_SIZE, outline="black")
        square.grid(row=17, column=col+4)
        score = SCRABBLE_LETTER_POINTS.get(letter.get_letter().upper(), 0)
        square.create_text(TILE_SIZE - 6, TILE_SIZE - 6, text=f"{score}", font=("Helvetica", 6))
        square.create_text(TILE_SIZE // 2, TILE_SIZE // 2, text=f"{letter.get_letter()}", font=("Helvetica", 10))
        square.create_rectangle(0, 0, TILE_SIZE, TILE_SIZE, outline="black")
        drag_tile_manager.add_tile(square, letter)

    window.mainloop()
    return board