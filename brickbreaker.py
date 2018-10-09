from graphics import *
from paddle import Paddle
from ball import Ball
from time import sleep
import random
from inputlistener import InputListener
from brick import Brick
from circleRectIntersect import *

class BrickBreaker:

    def __init__(self):
        self.win = GraphWin("Breakout", 900, 700)


    def playBrickBreaker(self):
        
        self.win.setBackground("orange")

        #Border
        border = Rectangle(Point(20, 20), Point(880, 680))
        border.draw(self.win)
        border.setFill("black")

        #Right Barrier
        r_barrier = Line(Point(602, 20), Point(602, 680))
        r_barrier.setFill("orange")
        r_barrier.draw(self.win)

        #Bricks Remaining Box
        score_box_text = Text(Point(670, 125), "Score:")
        score_box_text.setFill("white")
        score_box_text.draw(self.win)
        bricks_remaining_text = Text(Point(720, 125), 0)
        bricks_remaining_text.setFill("white")
        bricks_remaining_text.draw(self.win)

        #Number of lives

        lives = Text(Point(710, 200), "Lives Remaining:")
        lives.setFill("white")
        lives.draw(self.win)
        lives_remaining_text = Text(Point(780, 200), "5")
        lives_remaining_text.setFill("white")
        lives_remaining_text.draw(self.win)

        #Restart Button
        self.restart_button = Rectangle(Point(650, 250), Point(780, 350))
        self.restart_button.setFill("orange")
        self.restart_button.draw(self.win)

        restart_text = Text(Point(710, 300), "Restart")
        restart_text.setFill("white")
        restart_text.draw(self.win)


        #quit Button
        self.quit_button = Rectangle(Point(650, 400), Point(780, 500))
        self.quit_button.setFill("orange")
        self.quit_button.draw(self.win)

        quit_text = Text(Point(710, 450), "Quit")
        quit_text.setFill("white")
        quit_text.draw(self.win)

        iL = InputListener(self.win)
        iL.setMouseClickHandler(self.click)

        #PADDLE PORTION
    
        paddle = Paddle(Point(250,550),Point(350,570), self.win, border, r_barrier)
        paddle.color_paddle()
        iL.setKeyPressHandler(paddle.move_paddle)

        

        #Bricks
        x1 = 20
        y1 = 20
        x2 = 92.5
        y2 = 60
        self.bricks_list = []
        for i in range(4):
            for i in range(8):
                bricks = Brick(Point(x1, y1), Point(x2, y2), self.win)
                x1 += 72.5
                x2 += 72.5
                bricks.color_brick()
                self.bricks_list.append(bricks)
            x1 = 20
            x2 = 92.5
            y1 += 40
            y2 += 40
    
        #BALL PORTION

        game_ball = Ball(Point(300,400), 15, self.win)
        game_ball.color_ball()
        rand_x = random.randrange(-5, 5)
        rand_y = random.randrange(-10, 0)

        self.flag = True
        
        while self.flag:
        
            game_ball.move(rand_x, rand_y)
            sleep(0.020)
            #Right Barrier
            if game_ball.getCenter().getX() + game_ball.getRadius() >= r_barrier.getP2().getX():
                rand_x = rand_x * -1
            #Left Barrier
            if game_ball.getCenter().getX() - game_ball.getRadius() <= border.getP1().getX():
                rand_x = rand_x * -1
            #Top Barrier
            if game_ball.getCenter().getY() - game_ball.getRadius() <= border.getP1().getY():
                rand_y = rand_y * -1
            #Bottom Barrier
            if game_ball.getCenter().getY() + game_ball.getRadius() >= border.getP2().getY():
                lives_tally = self.lives_tally(lives_remaining_text, game_ball, self.win)
                rand_y = rand_y * -1
                
                dx = 300 - game_ball.getCenter().getX()
                dy = 400 - game_ball.getCenter().getY()

                game_ball.move(dx, dy)

                self.flag = lives_tally

            #Paddle Zones
                
            #left edge
                
            if game_ball.getCenter().getY() + game_ball.getRadius() >= paddle.getP1().getY() and game_ball.getCenter().getY() + game_ball.getRadius() <= paddle.getP2().getY() and game_ball.getCenter().getX() + game_ball.getRadius() >= paddle.getP1().getX() and game_ball.getCenter().getX() + game_ball.getRadius() <= paddle.getP1().getX() + 20:
                rand_y = -2.5
                rand_x = -5

            #left inner edge

            if game_ball.getCenter().getY() + game_ball.getRadius() >= paddle.getP1().getY() and game_ball.getCenter().getX() + game_ball.getRadius() >= paddle.getP1().getX() + 20 and game_ball.getCenter().getY() + game_ball.getRadius() <= paddle.getP2().getY() and game_ball.getCenter().getX() + game_ball.getRadius() <= paddle.getP1().getX() + 40:
                rand_y = -5
                rand_x = -5

            #middle

            if game_ball.getCenter().getY() + game_ball.getRadius() >= paddle.getP1().getY() and game_ball.getCenter().getY() + game_ball.getRadius() <= paddle.getP2().getY() and game_ball.getCenter().getX() + game_ball.getRadius() >= paddle.getP1().getX() + 40 and game_ball.getCenter().getX() + game_ball.getRadius() <= paddle.getP1().getX() + 60:
                rand_y = rand_y * -1

            #right inner edge    

            if game_ball.getCenter().getY() + game_ball.getRadius() >= paddle.getP1().getY() and game_ball.getCenter().getY() + game_ball.getRadius() <= paddle.getP2().getY() and game_ball.getCenter().getX() + game_ball.getRadius() >= paddle.getP1().getX() + 60 and game_ball.getCenter().getX() + game_ball.getRadius() <= paddle.getP1().getX() + 80:
                rand_y = -5
                rand_x = 5

            #right edge    

            if game_ball.getCenter().getY() + game_ball.getRadius() >= paddle.getP1().getY() and game_ball.getCenter().getY() + game_ball.getRadius() <= paddle.getP2().getY() and game_ball.getCenter().getX() + game_ball.getRadius() >= paddle.getP1().getX() + 80 and game_ball.getCenter().getX() + game_ball.getRadius() <= paddle.getP2().getX():
                rand_y = -2.5
                rand_x = 5

    
            for brick in self.bricks_list:   
                side_check = circleRectIntersect(game_ball, brick)
                if side_check == "left":
                    rand_x = rand_x * -1
                    self.bricks_list.remove(brick)
                    brick.undraw()
                    self.score_tally(bricks_remaining_text, game_ball, rand_y, self.win)
                if side_check == "right":
                    rand_x = rand_x * -1
                    self.bricks_list.remove(brick)
                    brick.undraw()
                    self.score_tally(bricks_remaining_text, game_ball, rand_y, self.win)
                if side_check == "top":
                    rand_y = rand_y * -1
                    self.bricks_list.remove(brick)
                    brick.undraw()
                    self.score_tally(bricks_remaining_text, game_ball, rand_y, self.win)
                if side_check == "bottom":
                    rand_y = rand_y * -1
                    self.bricks_list.remove(brick)
                    brick.undraw()
                    self.score_tally(bricks_remaining_text, game_ball, rand_y, self.win)

    def lives_tally(self, lives, ball, win):
        lives.undraw()
        lives_remaining = int(lives.getText())
        lives_remaining -= 1
        lives.setText(lives_remaining)
        lives.draw(win)

        if lives_remaining == 0:
            game_over_message = Text(Point(290, 350), "G A M E  O V E R")
            game_over_message.setFill("cyan")
            game_over_message.setSize(24)
            game_over_message.draw(win)
            ball.undraw()

            return False

        else:
            return True
           
            
        
                
    def score_tally(self, score, ball, rand_y, win):
        score.undraw()
        upd_score = int(score.getText())
        upd_score += 1
        score.setText(upd_score)
        score.draw(win)
        if upd_score == 32:
            level_completion = Text(Point(290, 350), "LEVEL COMPLETE!")
            level_completion.setFill("cyan")
            level_completion.setSize(24)
            level_completion.draw(win)
            self.levelTwo()
            dx = 300 - ball.getCenter().getX()
            dy = 400 - ball.getCenter().getY()
            ball.move(dx, dy)
            rand_y = rand_y * -1
            self.undrawMessage(level_completion)

        if upd_score == 72:
            level_completion = Text(Point(290, 350), "LEVEL COMPLETE!")
            level_completion.setFill("cyan")
            level_completion.setSize(24)
            level_completion.draw(win)
            self.undrawMessage(level_completion)
            

    def click(self, point):
        #Quit Button
        if point.getX() >= self.quit_button.getP1().getX() and point.getX() <= self.quit_button.getP2().getX() and point.getY() >= self.quit_button.getP1().getY() and point.getY() <= self.quit_button.getP2().getY():
            self.flag = False
            self.win.close()
        #Restart Button
        if point.getX() >= self.restart_button.getP1().getX() and point.getX() <= self.restart_button.getP2().getX() and point.getY() >= self.restart_button.getP1().getY() and point.getY() <= self.restart_button.getP2().getY():
            self.playBrickBreaker()            


    def levelTwo(self):
        x1 = 20
        y1 = 20
        x2 = 78
        y2 = 60
        self.bricks_list = []
        for i in range(4):            
            for j in range(10):
                brick = Brick(Point(x1, y1), Point(x2, y2), self.win)
                x1 += 58
                x2 += 58
                brick.color_brick()
                self.bricks_list.append(brick)
            x1 = 20
            x2 = 78
            y1 += 40
            y2 += 40
        

    def undrawMessage(self, text):
        sleep(2)
        text.undraw()
            
        
