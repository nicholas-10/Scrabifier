import game
import graphics
if __name__ == "__main__":
    running = True
    b = game.Board()
    while running:
        b.print_board()
        # play = b.get_input() 
        # while b.play_word(play) == -1:
            # play = b.get_input()
        
