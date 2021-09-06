class TicTacToe:
    XO = {"X":"P1", "O":"P2"}
    def __init__(self):
        self.board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
        self.P1_wins = 0
        self.P2_wins = 0
        self.start_player = "P1"
        self.current_player = "P1"
        self.render_board()

    def get_all_grid(self):
        all_grids = []
        for column in self.board:
            for i in column:
                all_grids.append(i)
        return all_grids

    def change_player(self):
        if self.current_player == "P1":
            self.current_player = "P2"
        else:
            self.current_player = "P1"

    def change_start_player(self):
        if self.start_player == "P1":
            self.start_player = "P2"
            self.current_player = "P2"
        else:
            self.start_player = "P1"
            self.current_player = "P1"

    def new_board(self):
        self.board = [[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]]
        self.change_start_player()
        self.render_board()


    #Used to describe the board so the player can see what is going on.
    def render_board(self):
        print()
        for col in self.board:
            print(*col)
            print()

    def make_move(self):
        move = int(input(self.current_player + " please Input a number: "))
        all_grids = self.get_all_grid()
        while move not in all_grids:
            move = int(input("The number is taken or doesn't exist! Please input a number again: "))
        for i,v in enumerate(self.board):
            if move in v:
                item_index = v.index(move)
                if self.current_player == "P1":
                    self.board[i][item_index] = "X"
                else:
                    self.board[i][item_index] = "O"
                self.change_player()
                self.render_board()


    def get_winner(self):
        #Vertical Win
        for col in range(3):
            if self.board[0][col] == self.board[1][col] and self.board[0][col] == self.board[2][col]:
                return TicTacToe.XO[self.board[0][col]]
        #Horizontal Win
        for row in range(3):
            if self.board[row][0] == self.board[row][1] and self.board[row][0] == self.board[row][2]:
                return TicTacToe.XO[self.board[row][0]]
        if self.board[0][0] == self.board[1][1] and self.board[0][0] == self.board[2][2]:
            return TicTacToe.XO[self.board[0][0]]
        elif self.board[0][2] == self.board[1][1] and self.board[0][2] == self.board[2][0]:
            return TicTacToe.XO[self.board[0][0]]
        if self.board_full():
            return "Tie"
        return "No Winner"

    def board_full(self):
        numbers = [1,2,3,4,5,6,7,8,9]
        all_grids = self.get_all_grid()
        check_grids = [i for i in all_grids if i in numbers]
        if len(check_grids) == 0:
            return True
        return False

    def end_game(self):
        result = self.get_winner()
        if result != "No Winner":
            if result == "P1":
                print("The winner is Player 1!")
                self.P1_wins += 1
            elif result == "P2":
                print("The winner is Player 2!")
                self.P2_wins += 1
            elif result == "Tie":
                print("Tie!")
            self.new_board()

NewGame = TicTacToe()

while True:
    NewGame.make_move()
    NewGame.end_game()



