#import turtle
import turtle as pizza

#-----setup----- (create lists, variables, etc.)
toppings = ["arrow","pepperoni.gif","mushroom.gif","anchovie.gif","olive.gif","pineapple_slice.gif","sausage.gif","red_onion.gif","bell_pepper.gif","basil_leaf.gif"]
toppings1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
user_top = 10

#set up turtle screen and register images
wn = pizza.Screen()
wn.setup(width=1.0, height=1.0)
wn.register_shape("pizzaboard.gif")
wn.register_shape("slicer.gif")
for x in range(9):
    wn.register_shape(toppings[x+1])

#define function to move turtle
def move_turtle(xcor, ycor):
    pizza.penup()
    pizza.goto(xcor, ycor)
    pizza.pendown()
   
#define function to draw shapes
def draw_pizza(radius, color, sides=None):
    pizza.pencolor(color)
    pizza.fillcolor(color)
    pizza.begin_fill()
    pizza.circle(radius, 360, sides)
    pizza.end_fill()

#define function to stamp toppings on pizza
def stamp_topping(xcor,ycor):
    pizza.shape(toppings[user_top])
    if user_top != 0:
       pizza.goto(xcor,ycor)
       pizza.stamp()

#define function to stamp toppings in the form of a smiley face
def smiley_face():
   stamp_topping(-70,100)
   stamp_topping(70,100)
   stamp_topping(-120,-20)
   stamp_topping(-90,-40)
   stamp_topping(-60,-60)
   stamp_topping(-30,-80)
   stamp_topping(0,-100)
   stamp_topping(30,-80)
   stamp_topping(60,-60)
   stamp_topping(90,-40)
   stamp_topping(120,-20)

#define function to cut pizza
def cut_pizza(xcor,ycor,degree):
   move_turtle(xcor,ycor)
   pizza.setheading(degree)
   pizza.forward(495)

#set up turtle, stamp pizza board
pizza.speed(5)
pizza.shape("pizzaboard.gif")
pizza.goto(0,120)
pizza.stamp()
pizza.shape("arrow")
move_turtle(0,-230)

#make pizza (crust, sauce, cheese)
draw_pizza(250, "burlywood1")
move_turtle(0,-205)
draw_pizza(225, "red")
draw_pizza(225, "bisque", 10)

#ask for user's choice of topping
while user_top not in toppings1:
  user_top = int(input("What topping would you like?\n1 = pepperoni\n2 = mushrooms\n3 = anchovies\n4 = olives\n5 = pineapples\n6 = sausages\n7 = onions\n8 = bell peppers\n9 = basil leaves\n0 = none\n"))
  if user_top not in toppings1:
    print("That is not a valid option. Please try again.")

#print smiley face, then cut pizza
smiley_face()
pizza.shape("slicer.gif")
pizza.color("peru")
pizza.pensize(3)
cut_pizza(-250,20,0)
cut_pizza(0,270,270)
cut_pizza(-175,195,315)
cut_pizza(175,195,225)
move_turtle(-450,-200)

steam = pizza.Turtle()
steams = ["steam_smallest.gif","steam_small.gif","steam_medium.gif","steam_big.gif"]
for s in steams:
    pizza.register_shape(s)
steam.shape("steam_smallest.gif")
steam.penup()
steam.goto(0,200)

steam.left(90)

for s in steams:
    steam.forward(75)
    steam.shape(s)

#Enjoy!
print("Bon appetit!")

#loop turtle screen
wn.mainloop()