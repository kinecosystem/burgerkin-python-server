from random import randint

class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        # self.board = [[1,2,3,4],[1,2,3,4],[5,6,7,0],[5,6,7,0]]
        self.scores = {
            1: 0,
            2: 0
        }
        self.generate_board(x,y)

    def generate_board(self,x,y):
        # create the board structure
        self.board = []
        for i in range(x):
            row = []
            for z in range(y):
                row.append(0)
            self.board.append(row)

        # create a flat list of cards
        flat_list = []
        for card in range(int(x*y/2)):
            flat_list.append(card)
            flat_list.append(card)

        # loop through the board and pick a random card for each spot visited
        for i in range(x):
            for z in range(y):
                idx = randint(0,len(flat_list)-1)
                self.board[i][z] = flat_list[idx]
                flat_list.remove(flat_list[idx])

        # print(self.board)

    def get_x_y(self,x,y):
        return self.board[x][y]

    def flip1(self,player_id,x,y):
        self.last_flipped = {
            'x': x,
            'y': y
        }
        return self.board[x][y]

    def flip2(self,player_id,x,y):
        ret = self.board[x][y]
        if self.board[self.last_flipped['x']][self.last_flipped['y']] == ret:
            self.board[x][y] = 999
            self.board[self.last_flipped['x']][self.last_flipped['y']] = 999
            self.scores[player_id] += 1
        self.last_flipped = None
        return ret

    def get_score(self,player_id):
        return self.scores[player_id]

    def is_game_over(self):
        ret = True
        for x in self.board:
            for y in x:
                if y != 999:
                    ret = False
        return ret
