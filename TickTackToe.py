from colors import MyColors
c = MyColors
class TicTacToe:
    def __init__(self):
    
        self.board = {'a1': '.', 'a2': '.', 'a3': '.', 'b1': '.', 'b2': '.', 'b3': '.', 'c1': '.', 'c2': '.', 'c3': '.'}
        self.keys = list(self.board)
        self.xup_right = ['a1', 'b2', 'c3']
        self.xdown_right = ['a3', 'b2', 'c1']
        self.turn = 1
        
        self.moves = []
        self.winner = None
    
    def print_board(self):
        title = ["\t\t TIC-TAC-TOE\n\n"]
        
        row3 = ["3", self.board['a3'], self.board['b3'], self.board['c3'], "\n\n"]
        row2 = ["2", self.board['a2'], self.board['b2'], self.board['c2'], "\n\n"]
        row1 = ["1", self.board['a1'], self.board['b1'], self.board['c1'], "\n\n"]
        row0 = [" ", "a", "b", "c"]
        to_screen = [title, row3, row2, row1, row0]
        for row in to_screen:
            for index in range(len(row)):
                if row[index] == 'X':
                    print(f"{c.cyan}{row[index]}{c.end}", end="      ")
                elif row[index] == 'O':
                    print(f"{c.red}{row[index]}{c.end}", end="      ")
                else:
                    print(row[index], end="      ")
        
    def get_player(self):
        if self.turn == 1:
            return 'X'
        else:
            return 'O'
            
    def make_move(self, coord):
        self.moves.append(coord)
        self.board[coord] = self.get_player()
        if self.won_game():
            self.print_board()
            print(f'{self.get_player()} won the game!')
            return 
        
        self.next_turn()
        return 
    
    def next_turn(self):
        self.turn *= -1
        
        
    def horizontal_win(self):
        keys = list(self.board)
        tally_h = 1
        for coordkey in range(1, len(list(self.board))):
            if self.board[keys[coordkey]] == self.board[keys[coordkey-1]] and keys[coordkey][0] == keys[coordkey-1][0]:
                tally_h += 1
                
                if tally_h == 3:
                    if self.board[keys[coordkey-1]] != '.':
                        return True
                
            else:
                tally_h = 1
    
        return False
        
    def vertical_win(self):
        ones = self.board[self.keys[0]]
        twos = self.board[self.keys[1]]
        threes = self.board[self.keys[2]]
    
        one_tally = 1 
        two_tally = 1 
        three_tally = 1

        for coordkey in range(3, len(list(self.board))):
            ending = (coordkey + 1) % 3     
            if ending == 0 and self.board[self.keys[coordkey]] == threes:
                three_tally += 1
                if three_tally == 3:
                    if self.board[self.keys[coordkey]] != '.':
                        return True
                    
            elif ending == 2 and self.board[self.keys[coordkey]] == twos:
                two_tally += 1
                if two_tally == 3:
                    if self.board[self.keys[coordkey]] != '.':
                        return True
                        
            elif ending == 1 and self.board[self.keys[coordkey]] == ones:
                one_tally += 1
                if one_tally == 3:
                    if self.board[self.keys[coordkey]] != '.':
                        return True
            else:
                continue
            
        return False
        
    def diagonal_win(self):
        if self.board['a1'] == '.' and self.board['a3'] == '.':
            return False
            
        tally = 0
        initial_value = self.board['a1']
        for coord in self.xup_right:
            if self.board[coord] == initial_value:
                tally += 1 
                if tally == 3:
                    return True
        tally = 0
        initial_value = self.board['a3']
        for coord in self.xup_right:
            if self.board[coord] == initial_value:
                tally += 1 
                if tally == 3:
                    return True
                    
        return False
        
    def won_game(self):
        if self.diagonal_win() or self.vertical_win() or self.horizontal_win():
            return True
        else:
            return False
            
    def get_valid_coord(self):
        valid is False
        while valid is False:
            move = input(f"{self.get_player()}, choose a square: ")
            if move in self.keys and move not in self.moves:
                valid = True
                self.make_move(move)
        return move
        
if __name__ == "__main__":
    game = TicTacToe()
    won = game.won_game()
    while won is False:
        valid = False
        while valid is False:
            game.print_board()
            move = input(f"{game.get_player()}, choose a square: ")
            if move in game.keys and move not in game.moves:
                valid = True
                game.make_move(move)
        
        
        if game.won_game() is True:
            won = True
