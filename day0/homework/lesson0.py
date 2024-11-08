from turtle import*

# we want to paint a house 

#draw a square 
speed (4)

width(7)


color("green")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

#end of the square

#drawing a door 
begin_fill()

forward(70)
color("purple")
left(90)
forward(120)
right(90)
forward(60)
right(90)
forward(120)
end_fill()


penup ()
goto (200, 200)
pendown ()

color("black")
begin_fill()
right (150)
forward (200)
left (120)
forward(200)
end_fill()

# draw a window 
penup ()
color ("black")
begin_fill()
goto (20,145)
left (210)
pendown()
forward(40)
right(90)
forward(40)
right(90)
forward(40)
right (90)
forward(40)
right (90)
end_fill()








# draw a window 
penup()
color("black")
begin_fill()
goto(180, 185)
left (90)
pendown()
forward(40)
left (90)
forward(40)
left(90)
forward(40)
left(90)
forward(40)
end_fill ()








exitonclick() 