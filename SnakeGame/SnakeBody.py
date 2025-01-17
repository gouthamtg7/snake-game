from turtle import Turtle

class CreateSnake():
    def __init__(self):
        self.segments = []
        self.create_a_snake_body()

    def create_a_snake_body(self):
        start_pos = [(0, 0), (-20, 0), (-40, 0)]
        for pos in start_pos:
            segment = Turtle("square")
            segment.penup()
            segment.color("white")
            segment.goto(pos)
            self.segments.append(segment)
        self.segments[0].color("red")

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)

    def move_the_snake(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.segments[0].forward(20)

    def gameover(self):
        head = self.segments[0]

        if head.xcor() < -290 or head.xcor() > 290 or head.ycor() < -290 or head.ycor() > 290:
            return True

        for segment in self.segments[1:]:
            if head.distance(segment) < 10:
                return True

        return False

    def add_body(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()

        last_segment = self.segments[-1]

        new_segment.goto(last_segment.xcor(), last_segment.ycor())

        self.segments.append(new_segment)
