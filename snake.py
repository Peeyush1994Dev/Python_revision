
SNAKE_SEGMENT_INITIAL_POSITIONS=[(0,0),(-20,0),(-40,0)]
from turtle import Turtle

up= 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):

        self.Snake_segment = []
        self.snake_body()
        self.head = self.Snake_segment[0]


    def snake_body(self):

        for position in SNAKE_SEGMENT_INITIAL_POSITIONS:
            self. add_position(position)


    def add_position(self,Position):
            new_segment = Turtle()
            new_segment.shape("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(Position)
            self. Snake_segment.append(new_segment)

    def extend(self):
        self.add_position(self.Snake_segment[-1].position)

    def move(self):
        for i in range((len(self.Snake_segment)-1),0,-1):
            new_xcor = self.Snake_segment[i-1].xcor()
            new_ycor = self.Snake_segment[i-1].ycor()
            self.Snake_segment[i].goto(new_xcor, new_ycor)

        self.head.forward(10)

    def down(self):
        self.head.setheading(down)
    def up(self):
        self.head.setheading(up)
    def left(self):
        self.head.setheading(left)
    def right(self):
        self.head.setheading(right)





