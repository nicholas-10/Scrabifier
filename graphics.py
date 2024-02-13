from tkinter import *
from tkinter import ttk

window = Tk()
style = ttk.Style()
window.resizable(0, 0)
window.title("Scrabble")
window.geometry("%dx%d%+d%+d" % (600, 600, 0, 0))

board_frame = ttk.Frame(window)
bar_frame = ttk.Frame(window)
tile_frame = ttk.Frame(window)
btn_frame = ttk.Frame(window)

board_frame.place(relx=0.5, rely=0.4, anchor = CENTER)
bar_frame.place(x = 0, rely = 0.8, relheight = 0.05, relwidth = 1)
tile_frame.place(x = 0, rely = 0.85, relheight = 0.05, relwidth = 1)
btn_frame.place(x = 0, rely = 0.9, relheight = 0.1, relwidth = 1)

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

board_colors = {
    "CT": "deeppink1",
    "DL": "cyan",
    "TL": "deepskyblue2",
    "DW": "darkorchid1",
    "TW": "orange"
}

square_size = 30
for row in range(len(board)):
    for col in range(len(board[row])):
        tile_type = board[row][col]
        color = board_colors.get(tile_type, "beige") 
        square = Canvas(board_frame, width=square_size, height=square_size, bg=color, highlightthickness=0)
        if(board[row][col] != "RT" and board[row][col] != "CT"):
            square.create_text(square_size // 2, square_size // 2, text=board[row][col])
        square.create_rectangle(0, 0, square_size, square_size, outline="black")
        square.grid(row=row, column=col)
tile_frame.grid_columnconfigure(0, weight = 1)
tile_frame.grid_columnconfigure(9, weight = 1)

for col in range(7):
    square = Canvas(tile_frame, width=square_size, height=square_size, bg='beige', highlightthickness=0)
    square.create_rectangle(0, 0, square_size, square_size, outline="black")
    square.grid(row=0, column=col+1)

window.mainloop()
