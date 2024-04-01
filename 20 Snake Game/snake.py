from turtle import Turtle

starting_positions = [(0, 0), (-20, 0), (-40, 0)]

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def add_segment(self, starting_x, starting_y):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fastest")
        new_segment.goto(x=starting_x, y=starting_y)
        self.segments.append(new_segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(20)

    def create_snake(self):
        for position in starting_positions:
            x_pos = position[0]
            y_pos = position[1]
            print(f"{x_pos} {y_pos}")
            self.add_segment(starting_x=x_pos, starting_y=y_pos)

    def extend(self):
        self.add_segment(self.segments[-1].xcor(), self.segments[-1].ycor())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
