from turtle import Turtle

start_pos=(0,-200)
move_distance=10
finish_line_y=200

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")

        self.penup()
        self.go_to_start()
        self.goto(start_pos)
        self.setheading(90)
    def go_up(self):
        self.forward(move_distance)
    def go_down(self):
        self.backward(move_distance)
        # self.distance_travel+=10
    def go_to_start(self):
        self.goto(start_pos)
    def finish_line(self):
        if self.ycor()>=finish_line_y:
            return True
        else:
            return False