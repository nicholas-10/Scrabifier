from tkinter import *
from tkinter import ttk
from constants import *
import random
import copy

tile_size = 30
square_size = 35

board = [
        ["TW", "RT", "RT", "DL", "RT", "RT", "RT", "TW", "RT", "RT", "RT", "DL", "RT", "RT", "TW"],
        ["RT", "DW", "RT", "RT", "RT", "TL", "RT", "RT", "RT", "TL", "RT", "RT", "RT", "DW", "RT"],
        ["RT", "RT", "DW", "RT", "RT", "RT", "DL", "RT", "DL", "RT", "RT", "RT", "DW", "RT", "RT"],
        ["DL", "RT", "RT", "DW", "RT", "RT", "RT", "DL", "RT", "RT", "RT", "DW", "RT", "RT", "DL"],
        ["RT", "RT", "RT", "RT", "DW", "RT", "RT", "RT", "RT", "RT", "DW", "RT", "RT", "RT", "RT"],
        ["RT", "TL", "RT", "RT", "RT", "TL", "RT", "RT", "RT", "TL", "RT", "RT", "RT", "TL", "RT"],
        ["RT", "RT", "DL", "RT", "RT", "RT", "DL", "RT", "DL", "RT", "RT", "RT", "DL", "RT", "RT"],
        ["TW", "RT", "RT", "DL", "RT", "RT", "RT", "CT", "RT", "RT", "RT", "DL", "RT", "RT", "TW"],
        ["RT", "RT", "DL", "RT", "RT", "RT", "DL", "RT", "DL", "RT", "RT", "RT", "DL", "RT", "RT"],
        ["RT", "TL", "RT", "RT", "RT", "TL", "RT", "RT", "RT", "TL", "RT", "RT", "RT", "TL", "RT"],
        ["RT", "RT", "RT", "RT", "DW", "RT", "RT", "RT", "RT", "RT", "DW", "RT", "RT", "RT", "RT"],
        ["DL", "RT", "RT", "DW", "RT", "RT", "RT", "DL", "RT", "RT", "RT", "DW", "RT", "RT", "DL"],
        ["RT", "RT", "DW", "RT", "RT", "RT", "DL", "RT", "DL", "RT", "RT", "RT", "DW", "RT", "RT"],
        ["RT", "DW", "RT", "RT", "RT", "TL", "RT", "RT", "RT", "TL", "RT", "RT", "RT", "DW", "RT"],
        ["TW", "RT", "RT", "DL", "RT", "RT", "RT", "TW", "RT", "RT", "RT", "DL", "RT", "RT", "TW"]
        ]

ori_tile = [
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "?", "R", "E", "S", "S"],
        ["-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "O", "-", "-", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "G", "R", "A", "P", "E", "S", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "H", "-", "-", "-", "-", "H", "-", "-"],
        ["-", "-", "-", "-", "-", "-", "-", "O", "R", "A", "L", "-", "O", "-", "-"],
        ["-", "-", "-", "J", "E", "S", "T", "S", "-", "-", "E", "-", "O", "-", "-"],
        ["-", "-", "-", "U", "-", "-", "-", "T", "E", "S", "T", "-", "T", "-", "-"],
        ["-", "B", "I", "G", "-", "-", "-", "S", "-", "-", "-", "-", "E", "-", "-"],
        ["-", "-", "-", "G", "-", "-", "-", "-", "-", "-", "-", "-", "R", "-", "-"],
        ["-", "-", "-", "L", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["S", "-", "-", "I", "N", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["U", "-", "-", "N", "O", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["?", "R", "A", "G", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"],
        ["S", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
        ]
tile = copy.deepcopy(ori_tile)

board_colors = {
    "CT": "deeppink1",
    "DL": "cyan",
    "TL": "deepskyblue2",
    "DW": "darkorchid1",
    "TW": "orange"
}

ori_hand = ["Z", "Q", "J", "Y", "Q", "K", "Z"]
hand = ori_hand.copy()

class DragTileManager():
    def __init__(self, frame):
        self.tile = None
        self.start_x = 0
        self.start_y = 0
        self.frame = frame
        self.letters = {}

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

    def on_drag_end(self, event):
        if self.tile:
            x, y = event.widget.winfo_x(), event.widget.winfo_y()
            board_width, board_height = self.frame.winfo_width(), self.frame.winfo_height()
            grid_col, grid_row = min(x // square_size, 14), min(y // square_size, 14)
            if y // square_size == 15 and 4 <= x // square_size <= 10:
                grid_col, grid_row = x // square_size, 15
                if hand[grid_col - 4] != "-":
                    grid_col, grid_row = self.ori_x // square_size, self.ori_y // square_size
                    snap_x, snap_y = min(max(grid_col * square_size, 0), board_width - tile_size) + 2.5, (min(max(grid_row * square_size, 0), board_height - tile_size) + 12.5) if self.ori_y // square_size == 15 else min(max(grid_row * square_size, 0), board_height - tile_size) + 2.5
                else:
                    print(f"Tile '{self.letters[event.widget]}' placed at hand:", grid_col - 4)
                    hand[grid_col - 4] = self.letters[event.widget]
                    snap_x, snap_y = min(max(grid_col * square_size, 0), board_width - tile_size) + 2.5, min(max(grid_row * square_size, 0), board_height - tile_size) + 12.5
                    grid_col, grid_row = self.ori_x // square_size, self.ori_y // square_size
                    if grid_row == 15:
                        print(f"Tile '{self.letters[event.widget]}' gone from hand:", grid_col - 4)
                        hand[grid_col - 4] = "-"
                    else:
                        print(f"Tile '{self.letters[event.widget]}' gone from board:", grid_col, grid_row)
                        tile[grid_row][grid_col] = "-"
            else:
                if tile[grid_row][grid_col] != "-":
                    grid_col, grid_row = self.ori_x // square_size, self.ori_y // square_size
                    snap_x, snap_y = min(max(grid_col * square_size, 0), board_width - tile_size) + 2.5, (min(max(grid_row * square_size, 0), board_height - tile_size) + 12.5) if self.ori_y // square_size == 15 else min(max(grid_row * square_size, 0), board_height - tile_size) + 2.5
                else:
                    print(f"Tile '{self.letters[event.widget]}' placed at position:", grid_col, grid_row)
                    tile[grid_row][grid_col] = self.letters[event.widget]
                    snap_x, snap_y = min(max(grid_col * square_size, 0), board_width - tile_size) + 2.5, min(max(grid_row * square_size, 0), board_height - tile_size) + 2.5
                    grid_col, grid_row = self.ori_x // square_size, self.ori_y // square_size
                    if grid_row == 15:
                        print(f"Tile '{self.letters[event.widget]}' gone from hand:", grid_col - 4)
                        hand[grid_col - 4] = "-"
                    else:
                        print(f"Tile '{self.letters[event.widget]}' gone from board:", grid_col, grid_row)
                        tile[grid_row][grid_col] = "-"
            event.widget.place_configure(x=snap_x, y=snap_y)
            self.tile = None

def reset():
    for widget in board_frame.winfo_children():
        widget.destroy()
    for widget in bar_frame.winfo_children():
        widget.destroy()

def shuffle_hand():
    global hand, ori_hand, tile, ori_tile, board_frame, bar_frame
    random.shuffle(ori_hand)
    hand = ori_hand.copy()
    tile = copy.deepcopy(ori_tile)
    reset()
    open_window()

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

drag_tile_manager = DragTileManager(board_frame)

board_frame.place(relx=0.5, rely=0.45, anchor = CENTER)
bar_frame.place(x = 0, rely = 0.85, relheight = 0.05, relwidth = 1)
btn_frame.place(x = 0, rely = 0.9, relheight = 0.05, relwidth = 1)

btn_frame.columnconfigure((0, 1, 2, 3), weight = 1, uniform = "a")
btn_frame.rowconfigure((0), weight = 1, uniform = "a")

style.configure("Bar.TButton", font=("Ubuntu", 10))
shuffle_btn = ttk.Button(btn_frame, text = "Shuffle", style="Bar.TButton", command=shuffle_hand)
exchange_btn = ttk.Button(btn_frame, text = "Exchange", style="Bar.TButton")
submit_btn = ttk.Button(btn_frame, text = "Submit", style="Bar.TButton")
quit_btn = ttk.Button(btn_frame, text = "Quit", style="Bar.TButton")

shuffle_btn.grid(row = 0, column = 0)
exchange_btn.grid(row = 0, column = 1)
submit_btn.grid(row = 0, column = 2)
quit_btn.grid(row = 0, column = 3)

style.configure("Turn.TLabel", font = ("Helvetica", 15, "bold"))
turn_lbl = ttk.Label(bar_frame, text = "Your Turn!", style = "Turn.TLabel", anchor = "center")
turn_lbl.pack()

def open_window():
    global hand, ori_hand, tile, ori_tile, window, board_frame, bar_frame, btn_frame, drag_tile_manager
    for row in range(len(board)):
        for col in range(len(board[row])):
            tile_type = board[row][col]
            color = board_colors.get(tile_type, "beige") 
            square = Canvas(board_frame, width=square_size, height=square_size, bg=color, highlightthickness=0)
            if(board[row][col] != "RT" and board[row][col] != "CT"):
                square.create_text(square_size // 2, square_size // 2, text=board[row][col], font=("Helvetica", 10))
            square.create_rectangle(0, 0, square_size, square_size, outline="black")
            square.grid(row=row, column=col)

    for row in range(len(tile)):
        for col in range(len(tile[row])):
            if(tile[row][col] != "-"):
                tile_type = board[row][col]
                color = board_colors.get(tile_type, "beige") 
                square = Canvas(board_frame, width=tile_size, height=tile_size, bg="burlywood1", highlightthickness=0)
                score = SCRABBLE_LETTER_POINTS.get(tile[row][col], 0)
                square.create_text(tile_size - 6, tile_size - 6, text=f"{score}", font=("Helvetica", 6))
                square.create_text(tile_size // 2, tile_size // 2, text=tile[row][col], font=("Helvetica", 10))
                square.create_rectangle(0, 0, tile_size, tile_size, outline="black")
                square.grid(row=row, column=col)

    board_frame.grid_rowconfigure(16, minsize=10)

    for col in range(7):
        square = Canvas(board_frame, width=square_size, height=square_size, bg='beige', highlightthickness=0)
        square.create_rectangle(0, 0, square_size, square_size, outline="black")
        square.grid(row=17, column=col+4)

    for col, letter in enumerate(hand):
        square = Canvas(board_frame, width=tile_size, height=tile_size, bg='burlywood', highlightthickness=0)
        square.create_rectangle(0, 0, tile_size, tile_size, outline="black")
        square.grid(row=17, column=col+4)
        score = SCRABBLE_LETTER_POINTS.get(letter.upper(), 0)
        square.create_text(tile_size - 6, tile_size - 6, text=f"{score}", font=("Helvetica", 6))
        square.create_text(tile_size // 2, tile_size // 2, text=f"{letter}", font=("Helvetica", 10))
        square.create_rectangle(0, 0, tile_size, tile_size, outline="black")
        drag_tile_manager.add_tile(square, letter)

    window.mainloop()

open_window()