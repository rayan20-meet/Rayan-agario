import turtle
import time
import random
import math
from ball import Ball
turtle.colormode(1)





turtle.tracer(0)
turtle.ht()
running= True
screen_width = turtle.getcanvas().winfo_width()/2
screen_height = turtle.getcanvas().winfo_height()/2
my_ball= Ball(0,0,0,0,60, "black")
number_of_balls= 5
min_ball_radius = 20
max_ball_radius = 100
min_ball_dx = -5
max_ball_dx = 5
min_ball_dy = -5
max_ball_dy = 5
BALLS=[]


for i in range (number_of_balls):
	x = random.randint(-screen_width + max_ball_radius , screen_width - max_ball_radius)
	y = random.randint(-screen_height + max_ball_radius, screen_height - max_ball_radius)
	
	dx =0
	while dx==0:
		dx = random.randint(min_ball_dx , max_ball_dx)

	dy = 0
	while dy==0:
		dy = random.randint(min_ball_dy, max_ball_dy)

	r = random.randint(min_ball_radius, max_ball_radius)
	color = (random.random(), random.random(), random.random())
	new_ball = Ball(x,y,dx,dy,r,color)
	BALLS.append(new_ball)


def move_all_balls():
	for ball in BALLS:
		ball.move(screen_width,screen_height)


def collide(ball_a, ball_b):
	if ball_a is ball_b:
		return False
	d= math.sqrt(math.pow(ball_a.pos()[0]-ball_b.pos()[0],2)+math.pow(ball_a.pos()[1]-ball_b.pos()[1],2))
	if ball_a.r+ball_b.r>= d:
		return True 
	else:
		return False


def check_all_ball_collision():
	global running
	all_balls=[]
	all_balls.append(my_ball)
	for ball in BALLS:
		all_balls.append(ball)
	for ball_a in all_balls:
		for ball_b in all_balls:
			if collide(ball_b,ball_a):
				r1=ball_a.r 
				r2=ball_b.r
				x=random.randint(-screen_width + max_ball_radius , screen_width - max_ball_radius)
				y = random.randint(-screen_height + max_ball_radius, screen_height - max_ball_radius)
	
				dx =0
				while dx==0:
					dx = random.randint(min_ball_dx , max_ball_dx)

				dy = 0
				while dy==0:
					dy = random.randint(min_ball_dy, max_ball_dy)

				r = random.randint(min_ball_radius, max_ball_radius)
				color =( random.random(), random.random(), random.random())
				if r1>r2:
					if ball_b== my_ball:
						running= False
					else:
						ball_b.new_ball(x,y,dx,dy,r,color)
						ball_a.r=ball_a.r+4
						ball_a.shapesize(ball_a.r/10)
				else:
					if ball_a==my_ball:
						running = False
					else:
						ball_a.new_ball(x,y,dx,dy,r,color)
						ball_b.r=ball_b.r+4
						ball_b.shapesize(ball_b.r/10)


def movearound():
	my_ball.goto(turtle.getcanvas().winfo_pointerx() - screen_width*2, screen_height*2 - turtle.getcanvas().winfo_pointery())



while running:
	screen_width = turtle.getcanvas().winfo_width()/2
	screen_height = turtle.getcanvas().winfo_height()/2
	movearound()
	move_all_balls()
	check_all_ball_collision()
	turtle.update()
	time.sleep(.1)




turtle.mainloop()





