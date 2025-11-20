import turtle
import random

class Polygon:
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def draw_polygon(self, num_sides, size, orientation, location, color, border_size):
        turtle.penup()
        turtle.goto(location[0], location[1])
        turtle.setheading(orientation)
        turtle.color(color)
        turtle.pensize(border_size)
        turtle.pendown()
        for _ in range(num_sides):
            turtle.forward(size)
            turtle.left(360/num_sides)
        turtle.penup()

    def get_new_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def nested_polygon(self, num_sides, depth=1):
        # draw a polygon at a random location, orientation, color, and border line thickness
        size = random.randint(50, 150)
        orientation = random.randint(0, 90)
        location = [random.randint(-300, 300), random.randint(-200, 200)]
        color = self.get_new_color()
        border_size = random.randint(1, 10)
        for _ in range(depth):
            self.draw_polygon(num_sides, size, orientation, location, color, border_size)

            # specify a reduction ratio to draw a smaller polygon inside the one above
            reduction_ratio = 0.618

            # reposition the turtle and get a new location
            turtle.penup()
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.left(90)
            turtle.forward(size*(1-reduction_ratio)/2)
            turtle.right(90)
            location[0] = turtle.pos()[0]
            location[1] = turtle.pos()[1]

            # adjust the size according to the reduction ratio
            size *= reduction_ratio


    def random_art(self, choice):
            if choice == 1:
                for _ in range(20):
                    self.nested_polygon(3)
            elif choice == 2:
                for _ in range(20):
                    self.nested_polygon(4)
            elif choice == 3:
                for _ in range(20):
                    self.nested_polygon(5)
            elif choice == 4:
                for _ in range(20):
                    self.nested_polygon(random.randint(3, 5))  
            elif choice == 5:
                for _ in range(20):
                    self.nested_polygon(3,3) 
            elif choice == 6:
                for _ in range(20):
                    self.nested_polygon(4,3)
            elif choice == 7:
                for _ in range(20):
                    self.nested_polygon(5,3)
            elif choice == 8:
                for _ in range(20):
                    self.nested_polygon(random.randint(3,5), 3)
            elif choice == 9:
                for _ in range(20):
                    self.nested_polygon(random.randint(3,5), random.randint(1,4))   
            turtle.update()
            turtle.done()


choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
art = Polygon()
art.random_art(choice)