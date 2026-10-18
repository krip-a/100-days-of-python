import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """creates a snake (3 turtle segments)"""
        #create a snake w 3 segments
        for position in STARTING_POSITIONS:
            new_segment = t.Turtle(shape = "square")
            new_segment.penup()
            new_segment.color("white")
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move(self):
        """moves the snake forward 20 paces"""    
        #turning\
            #move 3rd to where 2 was
            #move 2 to where 1 was
            #move/turn 1st as needed
        
            #for seg_num in range(start=2, stop=0, step=-1): [close to this]
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    #if facing up, can't turn down and vice versa
    #if facing left, can't turn right and vice versa
    
    def up(self):
        """move snake up (90)"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """move snake down (270)"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """move snake left (180)"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """move snake right (0)"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)