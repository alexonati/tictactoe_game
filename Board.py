class Board:
    def __init__(self):
        self.cells = [" " for x in range(9)]

    def display(self):
        print(" %s | %s | %s " % (self.cells[0], self.cells[1], self.cells[2]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[3], self.cells[4], self.cells[5]))
        print("-----------")
        print(" %s | %s | %s " % (self.cells[6], self.cells[7], self.cells[8]))

    @staticmethod
    def print_title():
        print("Welcome to the Tic Tac Toe game\n")

    @staticmethod
    def refresh_screen(board):
        board.print_title()

        board.display()

    def update_board(self, choice, player):
        if self.cells[choice] == " ":
            self.cells[choice] = player

    def is_winner(self, player):
        for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
            result = True
            for cell_no in combo:
                if self.cells[cell_no] != player:
                    result = False
        if result:
            return True
        return False

    def is_tie(self):
        used_cells = 0
        for cell in self.cells:
            if cell != " ":
                used_cells += 1
        if used_cells == 9:
            return True
        else:
            return False

    def computer_move(self, player):
        for i in range(0, 9):
            if self.cells[i] == " ":
                self.update_board(i, player)
                break

    def reset_game(self):
        self.__init__()
