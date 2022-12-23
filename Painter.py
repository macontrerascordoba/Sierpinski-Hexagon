import turtle, random

class Painter():
    
    def __init__(self, dots, speed):
        self.dots = dots
        self.speed = speed


    def start(self):

        colors = {
                'bg' : '#201a1a',
                'turtle' : '#dbd2d2'
            }

        # Modifying the window name and color
        turtle.title("Sierpinski Hexagon")
        turtle.screensize(canvwidth=400, canvheight=400, bg=colors['bg'])

        s = turtle.Screen()	# Create and open the turtle screen

        t = turtle.Turtle()		# Asign the turtle to the variable t
        
        # Personalizing the turtle
        t.color(colors['turtle'], colors['turtle'])
        t.shapesize(1,1,1)
        t.speed(self.speed)


        # Drawing the hexagon apices

        t.setheading(0)

        apices = []

        t.penup()

        t.forward(240)
        apices.append(t.pos())
        t.backward(240)
        for i in range(5):
            t.right(60)
            t.forward(240)
            apices.append(t.pos())
            t.backward(240)

        for apex in apices:
            t.goto(apex)
            t.dot(2)

        # Drawing the first random point within the triangle
        t.penup()

        last_point = apices[0]

        t.goto(last_point)
        t.dot(2)

        for i in range(self.dots):

            # Choosing one of the apices

            apex = random.choice(apices)


            # Calculating point 2/3 between apex and last_point

            distanceApexLastPoint = t.distance(apex)
            thirdsOfDistance = (distanceApexLastPoint/3)

            t.setheading(t.towards(apex))
            t.forward(thirdsOfDistance*2)
            t.dot(2)

            last_point = t.pos()	# Asign the new point as the last_point
            
        t.goto(400, 400)	# Move the turtle outside of the triangle

        turtle.done()	#Keep the window from closing. If you delete this line the screen will close as soon as it finish