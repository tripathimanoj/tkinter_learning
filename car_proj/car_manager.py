from turtle import Turtle
import random
color=["red","orange","yellow","green", "pink","blue"]
start_move_distance=5
move_inc=10
finish_line_y=200

class Car:
    def __init__(self):
        self.all_cars=[]
        self.car_speed=start_move_distance

    def create_cars(self):
        random_chance=random.randint(1,6)
        if random_chance==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(color))
            random_Y = random.randint(-250, 250)
            new_car.goto(300, random_Y)
            self.all_cars.append(new_car)


    def move_car(self):
        for car in self.all_cars:
            car.backward(start_move_distance)

    def level_up(self):
        self.car_speed+=move_inc

