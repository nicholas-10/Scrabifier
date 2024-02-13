from tkinter import *
from tkinter import ttk
from constants import *

class DragTileManager():
    def __init__(self, frame):
        self.tile = None
        self.start_x = 0
        self.start_y = 0
        self.frame = frame

    def add_tile(self, tile):
        tile.bind("<ButtonPress-1>", self.on_drag_start)
        tile.bind("<B1-Motion>", self.on_drag)
        tile.bind("<ButtonRelease-1>", self.on_drag_end)
        tile.configure(cursor="hand1")

    def on_drag_start(self, event):
        self.tile = event.widget
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        if self.tile:
            x = event.widget.winfo_x() - self.start_x + event.x
            y = event.widget.winfo_y() - self.start_y + event.y

            board_width = self.frame.winfo_width()
            board_height = self.frame.winfo_height()
            tile_width = self.tile.winfo_width()
            tile_height = self.tile.winfo_height()

            x = min(max(x, 0) - 9, board_width - tile_width - 12)
            y = min(max(y, 0) - 9, board_height - tile_height - 12)

            event.widget.place_configure(x=x, y=y)

    def on_drag_end(self, event):
        self.tile = None

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
shuffle_btn = ttk.Button(btn_frame, text = "Shuffle", style="Bar.TButton")
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

tile = [
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

board_colors = {
    "CT": "deeppink1",
    "DL": "cyan",
    "TL": "deepskyblue2",
    "DW": "darkorchid1",
    "TW": "orange"
}

tile_size = 30
square_size = 35
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

hand = ["Z", "Q", "J", "Y", "Q", "K", "Z"]

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
    drag_tile_manager.add_tile(square)

window.mainloop()
