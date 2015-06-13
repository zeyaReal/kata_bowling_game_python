import unittest
from Bowling import *

class BowlingTest(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def test_normal_throw(self):
        self.game.throwBall(3);
        self.game.throwBall(4);
        self.game.throwBall(1);
        self.game.throwBall(2);
        self.assertEqual(self.game.getScore(1) , 7);        
        self.assertEqual(self.game.getScore(2) , 10);        


    def test_spare_throw(self):
        self.game.throwBall(2);
        self.game.throwBall(8);
        self.game.throwBall(7);
        self.game.throwBall(3);
        self.game.throwBall(5);
        self.assertEqual(self.game.getScore(1) , 17);        
        self.assertEqual(self.game.getScore(2) , 32);        

    def test_strike_throw(self):
        self.game.throwBall(10);
        self.game.throwBall(7);
        self.game.throwBall(1);
        self.assertEqual(self.game.getScore(1) , 18);        


unittest.main()
