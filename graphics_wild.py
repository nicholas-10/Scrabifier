from tkinter import *
from tkinter import ttk
from constants import *

def open_wild_window(callback, event, snap_x, snap_y, grid_col, grid_row):
    def letter_chosen(letter):
        window.destroy()
        callback(event, letter, snap_x, snap_y, grid_col, grid_row)

    letters = [["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M"],
               ["N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]]

    window = Tk()
    style = ttk.Style()
    style.configure("Show.TLabel", font=("Helvetica", 15, "bold"))
    window.resizable(0, 0)
    window.title("Scrabble - Wild Tile")
    window.geometry("%dx%d%+d%+d" % (550, 150, 0, 0))

    board_frame = ttk.Frame(window)
    board_frame['padding'] = 2
    board_frame['borderwidth'] = 2
    board_frame['relief'] = 'groove'

    show_frame = ttk.Frame(window)

    board_frame.place(relx=0.5, rely=0.4, anchor=CENTER)
    show_frame.place(x=0, rely=0.7, relwidth=1)

    show_lbl = ttk.Label(show_frame, text="Pick a letter for the Wild Tile (?)", style="Show.TLabel", anchor="center")
    show_lbl.pack()

    for row in range(len(letters)):
        for col in range(len(letters[row])):
            square = Canvas(board_frame, width=SQUARE_SIZE, height=SQUARE_SIZE, bg="beige", highlightthickness=0)
            square.create_rectangle(0, 0, SQUARE_SIZE, SQUARE_SIZE, outline="black")
            square.grid(row=row, column=col)

    for row in range(len(letters)):
        for col in range(len(letters[row])):
            letter = letters[row][col]
            square = Canvas(board_frame, width=TILE_SIZE, height=TILE_SIZE, bg="burlywood1", highlightthickness=0)
            score = SCRABBLE_LETTER_POINTS.get(letter, 0)
            square.create_text(TILE_SIZE - 6, TILE_SIZE - 6, text=f"{score}", font=("Helvetica", 6))
            square.create_text(TILE_SIZE // 2, TILE_SIZE // 2, text=letter.upper(), font=("Helvetica", 10))
            square.create_rectangle(0, 0, TILE_SIZE, TILE_SIZE, outline="black")
            square.grid(row=row, column=col)
            square.bind("<Button-1>", lambda e, l=letter: letter_chosen(l.lower()))

    window.mainloop()
