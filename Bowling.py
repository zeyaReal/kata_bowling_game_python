class Game:
    def __init__(self):
        self.throwBalls = []


    def throwBall(self, number):
        self.throwBalls.append(number)

    def isStrike(self, ball):
        return self.throwBalls[ball] == 10

    def isSpare(self, ball):
        return self.throwBalls[ball] + self.throwBalls[ball+1] == 10

    def getScore(self, turnNumber):
        score = 0;
        turn = 1 
        ball = 0
        while (turn <= turnNumber):
            if self.isStrike(ball):
                turnScore = self.throwBalls[ball] + self.throwBalls[ball+1] +self.throwBalls[ball+2]
                ball += 1
                score += turnScore;
            elif self.isSpare(ball):
                turnScore = self.throwBalls[ball] + self.throwBalls[ball+1]
                ball += 2
                score += turnScore;
                score += self.throwBalls[ball]
            else:
                turnScore = self.throwBalls[ball] + self.throwBalls[ball+1]
                ball += 2
                score += turnScore;
            
            turn += 1
        return score