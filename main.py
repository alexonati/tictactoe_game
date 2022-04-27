from Board import Board

if __name__ == "__main__":

    board = Board()

    while True:
        board.refresh_screen(board)
        try:
            x_choice = int(input("\n X-Player please choose 0-8 ---> "))
        except ValueError as NotIntInput:
            print("\n Please enter a value between 0 and 8 ---> ")

        board.update_board(x_choice, "X")

        board.refresh_screen(board)

        try:
            o_choice = int(input("\n 0-Player please choose 0-8 ---> "))
        except ValueError as NotIntInput:
            print("\n Please enter a value between 0 and 8 ---> ")

        board.update_board(o_choice, "0")

        if board.is_winner("X"):
            print("\n X is the winner!\n")
            play_again = input("Would you like to play again (Y/N): ----> ").upper()
            if play_again == "Y":
                board.reset_game()
                continue
            else:
                break

        if board.is_winner("0"):
            print("\n 0 is the winner!\n")
            play_again = input("Would you like to play again (Y/N): ----> ").upper()
            if play_again == "Y":
                board.reset_game()
                continue
            else:
                break

        if board.is_tie():
            print("\n The game is a tie.\n")
            play_again = input("Would you like to play again (Y/N): ----> ").upper()
            if play_again == "Y":
                board.reset_game()
                continue
            else:
                break
