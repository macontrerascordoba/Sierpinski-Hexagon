import turtle, random, time, os, math

##################################
#								 #
#			User Inputs	 		 #			More input value checks to be added to the while loops
#								 #
##################################

points = 5000
speed = 0

os.system('cls' if os.name == 'nt' else 'clear')

print('SIERPINSKI HEXAGON\n')


# Choosing number of dots

points = input("How many dots do you want me to draw: (Min = 1, Default = 5000)  ->  ")

while True:	

	if points == "":
			points = 5000
			break

	try:
		points = int(points)
	except:
		points = input("\nIt has to be a number. Please try again:  ->  ")
	else:
		if points < 1:
			points = 1
		break

print("\nPerfect, I'm going to draw ", points, " points\n\n")


# Choosing speed

speed = input("At what speed do you me want to move: (1 - Slowest, 10 - Fastest, 0 (default) - Instantly)  ->  ")

while True:

	if speed == "":
		speed = 0
		break

	try:
		speed = int(speed)
	except:
		speed = input("\nIt has to be a number. Please try again:  ->  ")
	else:
		if speed < 0 or speed > 10:
			speed = 0
		break

if speed == 0:
	print("\nOk, I'll go as fast as I can")
else:
	print("\nAwesome, I'm going to change my speed to ", speed, " units")


print("\n\nEverything set, I will start now")

time.sleep(3)


##############################################################################################################################


# Modifying the window name and color
turtle.title("Sierpinski Hexagon")
turtle.screensize(canvwidth=400, canvheight=400, bg="black")

s = turtle.getscreen()	# Create and open the turtle screen

t = turtle.Turtle()		# Asign the turtle to the variable t

# Personalizing the turtle
t.color("white", "white")
t.shapesize(1,1,1)
t.speed(speed)


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


for i in range(points):

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