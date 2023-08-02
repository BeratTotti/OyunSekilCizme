import turtle
drawing_board = turtle.Screen()
drawing_board.bgcolor("light green")
drawing_board.title("İnteraktif2")

turtle_instance = turtle.Turtle()

def turtle_forward():
    turtle_instance.forward(100)

def rota_right():
    #turtle_instance.setheading(turtle_instance.heading() - 10)
    # bu yukarıdaki kod instance hangi açıda ise ondan 10 çıkar ve o yöne doğru doğrult instance ' ı demektir
    turtle_instance.right(90)

def rota_left():
    #turtle_instance.setheading(turtle_instance.heading()-10)
    # bu yukarıdaki kod instance hangi açıda ise ondan 10 çıkar ve o yöne doğru doğrult instance ' ı demektir
    turtle_instance.left(90)

def clear():
    turtle_instance.clear()

def turtle_return_home():
    turtle_instance.penup()
    turtle_instance.home()
    turtle_instance.pendown()


def pen_up():
    turtle_instance.penup()

def pen_down():
    turtle_instance.pendown()


drawing_board.listen()
drawing_board.onkey(fun=turtle_forward,key="space")
drawing_board.onkey(fun=rota_right,key="D")
drawing_board.onkey(fun=rota_left,key="A")
drawing_board.onkey(fun=clear,key="Q")
drawing_board.onkey(fun=turtle_return_home,key="E")
drawing_board.onkey(fun=pen_up,key="K")
drawing_board.onkey(fun=pen_down,key="W")





turtle.mainloop()
