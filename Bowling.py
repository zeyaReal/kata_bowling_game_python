class Game:
    def __init__(self):
        self.throwBalls = []

    def throwBall(self, number):
        self.throwBalls.append(number)

    def isStrike(self):
        return self.throwBalls[self.ball] == 10

    def isSpare(self):
        return self.throwBalls[self.ball] + self.throwBalls[self.ball+1] == 10

    def getScore(self, turnNumber):
        turn = 1 
        self.score = 0
        self.ball = 0
        while (turn <= turnNumber):
            if self.isStrike():
                self.score += 10 + self.throwBalls[self.ball+1] +self.throwBalls[self.ball+2];
                self.ball += 1                
            elif self.isSpare():
                self.score += 10 + self.throwBalls[self.ball+2]
                self.ball += 2
            else:
                self.score += self.throwBalls[self.ball] + self.throwBalls[self.ball+1]
                self.ball += 2
            
            turn += 1
        return self.score