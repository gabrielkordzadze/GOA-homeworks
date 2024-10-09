from turtle import*

#we want to paint house

#step 1:  draw a square
shape("classic")
#speed(30)
width(7)
color("black")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
color("blue")
begin_fill()
left(90)
forward(120)  #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200,200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()


color("black")
left(30)
forward(74)
color("brown")
begin_fill()
left(90)
forward(74)
left(90)
forward(74)
left(90)
forward(74)
end_fill()
color("black")
right(180)
forward(200)
color("brown")
begin_fill()
right(90)
forward(70)
right(90)
forward(70)
right(90)
forward(70)
end_fill()
exitonclick()
#end of the house















