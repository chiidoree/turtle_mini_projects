import turtle
 
def flower():
    # object1
    flower1_turtle = turtle.Turtle()
    
    # turtle speed
    flower1_turtle.speed(20) #speed remains same for all objects
 
    # turtle color
    flower1_turtle.color("white") #hiding turtle color that displays upon setting turtle position
    flower1_turtle.setpos(0, 0)
    flower1_turtle.color("sandybrown")
    flower1_turtle.fillcolor("yellow")
    flower1_turtle.begin_fill()

    # flower pattern
    for _ in range(36):
        flower1_turtle.width(2)
        flower1_turtle.circle(20,360)
        flower1_turtle.circle(50,220)
    flower1_turtle.end_fill()

    # stem
    flower1_turtle.width(3)
    flower1_turtle.color("green")
    flower1_turtle.right(90)
    flower1_turtle.forward(80)

    flower1_turtle.fillcolor("green")
    flower1_turtle.begin_fill()

    # left leaf
    flower1_turtle.right(90)
    flower1_turtle.circle(-55, 90)
    flower1_turtle.right(90)
    flower1_turtle.circle(-55, 90)
  

    #right leaf
    flower1_turtle.forward(60)
    flower1_turtle.left(180)
    flower1_turtle.circle(-55, 90)
    flower1_turtle.right(90)
    flower1_turtle.circle(-55, 90)
    
    flower1_turtle.end_fill()

    # hiding the turtle
    flower1_turtle.hideturtle()

    #turtle object2 (right side)
    flower2_turtle = turtle.Turtle()
    
    # turtle color
    flower2_turtle.color("white")  #hiding turtle color that displays upon setting turtle position
    flower2_turtle.setpos(120, -50)
    flower2_turtle.speed(20)
    flower2_turtle.color("sandybrown")
    flower2_turtle.fillcolor("yellow")
    flower2_turtle.begin_fill()

    # flower pattern
    for _ in range(36):
        flower2_turtle.width(2)
        flower2_turtle.circle(20,360)
        flower2_turtle.circle(50,220)
    flower2_turtle.end_fill()

    # stem
    flower2_turtle.width(3)
    flower2_turtle.color("green")
    flower2_turtle.right(90)
    flower2_turtle.forward(80)

    flower2_turtle.fillcolor("green")
    flower2_turtle.begin_fill()

    # left leaf
    flower2_turtle.right(90)
    flower2_turtle.circle(-55, 90)
    flower2_turtle.right(90)
    flower2_turtle.circle(-55, 90)
  

    #right leaf
    flower2_turtle.forward(60)
    flower2_turtle.left(180)
    flower2_turtle.circle(-55, 90)
    flower2_turtle.right(90)
    flower2_turtle.circle(-55, 90)
    
    flower2_turtle.end_fill()
    
    #turtle object 3 (left side)
    flower3_turtle = turtle.Turtle()
    
    #turtle color
    flower3_turtle.color("white")  #hiding turtle color that displays upon setting turtle position
    flower3_turtle.setpos(-120, -50)
    flower3_turtle.speed(20)
    flower3_turtle.color("sandybrown")
    flower3_turtle.fillcolor("yellow")
    flower3_turtle.begin_fill()

    # flower pattern
    for _ in range(36):
        flower3_turtle.width(2)
        flower3_turtle.circle(20,360)
        flower3_turtle.circle(50,220)
    flower3_turtle.end_fill()

    # stem
    flower3_turtle.width(3)
    flower3_turtle.color("green")
    flower3_turtle.right(90)
    flower3_turtle.forward(80)

    flower3_turtle.fillcolor("green")
    flower3_turtle.begin_fill()

    # left leaf
    flower3_turtle.right(90)
    flower3_turtle.circle(-55, 90)
    flower3_turtle.right(90)
    flower3_turtle.circle(-55, 90)
  
    #right leaf
    flower3_turtle.forward(60)
    flower3_turtle.left(180)
    flower3_turtle.circle(-55, 90)
    flower3_turtle.right(90)
    flower3_turtle.circle(-55, 90)
    
    flower3_turtle.end_fill()

    # hiding turtle
    flower3_turtle.hideturtle()
    
    # pausing turtle graphics window
    turtle.done()

flower()

