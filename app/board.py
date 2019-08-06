class Board:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.board = [[1,2,3,4],[1,2,3,4],[5,6,7,0],[5,6,7,0]]
        self.scores = {
            1: 0,
            2: 0
        }

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
        print("debug")
        print(self.last_flipped)
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
