from tkinter import *

windows = Tk()
windows.geometry("1000x500")
windows.title("liiklusmärk")
windows.resizable(width=False, height=False)
canva = Canvas(width=1000, height= 500)
canva.pack()

kolmnurk_cords = [500, 50, #top
                  250, 400, #left
                  750, 400, #right
                 ]

canva.create_polygon(kolmnurk_cords, outline="red", fill="", width=25)

i = 0
while i < 5:
    post = canva.create_rectangle(380+i*50, 260, 410+i*50, 375, fill="black")
    posti_triangle = canva.create_polygon(380+i*50, 260, 410+i*50, 260, 395+i*50, 235, fill="black")
    i += 1

ulemine_cross_post = canva.create_rectangle(370, 265, 620, 285, fill="black")
alumine_cross_post = canva.create_rectangle(370, 340, 620, 360, fill="black")


windows.mainloop()

