from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 20
MOVE_DISTANCE_RIGHT = 90
FINISH_LINE_Y = 280
MOVE_RIGHT = 360

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def go_right(self):
        self.right(MOVE_DISTANCE_RIGHT)

    def go_left(self):
        self.left(MOVE_DISTANCE_RIGHT)

    def go_to_start(self):
        self.goto(STARTING_POSITION)


    def  is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False


