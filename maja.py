from tkinter import *

windows = Tk()
windows.geometry("800x600")
windows.resizable(False,False)
windows.title("Maja")

canva = Canvas(windows, width=800, height=600, bg="white")
canva.pack()

maja_core = canva.create_rectangle(250, 300, 550, 600, fill="#EDDA58")

maja_katuse_cords = [250, 300, #left corner x1 y1
                     550, 300, #right corner x2 y2
                     400, 100, #Top x3 y3 
                    ]

maja_korsteni_kolmnurk_cords = [468, 190, #left x1 y1
                          520, 260, #bottom x2 y2
                          520, 190, #top x3 y3  
                         ]

maja_katus = canva.create_polygon(maja_katuse_cords, fill="#ED5142", outline="black")
maja_uks = canva.create_rectangle(380, 600, 420, 550, fill="black")
maja_ukse_link = canva.create_oval(410, 585, 420, 575, fill="yellow")

maja_korsten = canva.create_rectangle(467, 110, 519, 190, fill="#AB9F9F")
maja_korsteni_kolmnurk = canva.create_polygon(maja_korsteni_kolmnurk_cords, fill="#AB9F9F", outline="black")

def draw_window(x, y):
    w = 80 
    h = 80 

    
    canva.create_rectangle(x, y, x+w, y+h, fill="#6FA8FF", outline="black")

    
    canva.create_line(x + w/2, y, x + w/2, y + h, width=3)

    
    canva.create_line(x, y + h/2, x + w, y + h/2, width=3)


draw_window(280, 360)  
draw_window(440, 360)  

windows.mainloop()
