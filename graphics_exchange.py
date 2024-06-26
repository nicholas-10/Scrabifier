from tkinter import *
from tkinter import ttk
from constants import *

def open_exchange_window(callback, hand, exchange, b, w):
    def letters_chosen(exchange):
        window.destroy()
        new = b.get_bag().exchange(len(exchange), exchange)
        new_hand = hand.copy()
        ex = False
        if(len(new) != 0):
            ex = True
            new_hand.extend(new)
        callback(new_hand, b, w, ex)

    def add_to_exchange(letter):
        hand.remove(letter)
        exchange.append(letter)
        window.destroy()
        open_exchange_window(callback, hand, exchange, b, w)

    def remove_from_exchange(letter):
        exchange.remove(letter)
        hand.append(letter)
        window.destroy()
        open_exchange_window(callback, hand, exchange, b, w)

    window = Tk()
    style = ttk.Style()
    style.configure("Show.TLabel", font=("Helvetica", 15, "bold"))
    window.resizable(0, 0)
    window.title("Scrabble - Exchange")
    window.geometry("%dx%d%+d%+d" % (550, 250, 0, 0))

    start_frame = ttk.Frame(window)
    start_frame['padding'] = 2
    start_frame['borderwidth'] = 2
    start_frame['relief'] = 'groove'

    end_frame = ttk.Frame(window)
    end_frame['padding'] = 2
    end_frame['borderwidth'] = 2
    end_frame['relief'] = 'groove'

    show_frame = ttk.Frame(window)

    start_frame.place(relx=0.5, rely=0.25, anchor=CENTER)
    end_frame.place(relx=0.5, rely=0.5, anchor=CENTER)
    show_frame.place(x=0, rely=0.7, relwidth=1)

    show_lbl = ttk.Label(show_frame, text="Pick letters to exchange", style="Show.TLabel", anchor="center")
    show_lbl.pack()

    exchange_button = ttk.Button(show_frame, text="Exchange", command=lambda: letters_chosen(exchange))
    exchange_button.pack()

    for col in range(7):
        square = Canvas(start_frame, width=SQUARE_SIZE, height=SQUARE_SIZE, bg='beige', highlightthickness=0)
        square.create_rectangle(0, 0, SQUARE_SIZE, SQUARE_SIZE, outline="black")
        square.grid(row=1, column=col+4)

    for col, letter in enumerate(hand):
        square = Canvas(start_frame, width=TILE_SIZE, height=TILE_SIZE, bg='burlywood', highlightthickness=0)
        square.create_rectangle(0, 0, TILE_SIZE, TILE_SIZE, outline="black")
        square.grid(row=1, column=col+4)
        score = SCRABBLE_LETTER_POINTS.get(letter.get_letter().upper(), 0)
        square.create_text(TILE_SIZE - 6, TILE_SIZE - 6, text=f"{score}", font=("Helvetica", 6))
        square.create_text(TILE_SIZE // 2, TILE_SIZE // 2, text=f"{letter.get_letter()}", font=("Helvetica", 10))
        square.create_rectangle(0, 0, TILE_SIZE, TILE_SIZE, outline="black")
        square.bind("<Button-1>", lambda e, l=letter: add_to_exchange(l))

    for col in range(7):
        square = Canvas(end_frame, width=SQUARE_SIZE, height=SQUARE_SIZE, bg='beige', highlightthickness=0)
        square.create_rectangle(0, 0, SQUARE_SIZE, SQUARE_SIZE, outline="black")
        square.grid(row=1, column=col+4)

    for col, letter in enumerate(exchange):
        square = Canvas(end_frame, width=TILE_SIZE, height=TILE_SIZE, bg='burlywood', highlightthickness=0)
        square.create_rectangle(0, 0, TILE_SIZE, TILE_SIZE, outline="black")
        square.grid(row=1, column=col+4)
        score = SCRABBLE_LETTER_POINTS.get(letter.get_letter().upper(), 0)
        square.create_text(TILE_SIZE - 6, TILE_SIZE - 6, text=f"{score}", font=("Helvetica", 6))
        square.create_text(TILE_SIZE // 2, TILE_SIZE // 2, text=f"{letter.get_letter()}", font=("Helvetica", 10))
        square.create_rectangle(0, 0, TILE_SIZE, TILE_SIZE, outline="black")
        square.bind("<Button-1>", lambda e, l=letter: remove_from_exchange(l))

    window.mainloop()
