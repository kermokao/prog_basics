from tkinter import *

windows = Tk()
windows.resizable(False, False)
windows.geometry("1000x500")
windows.title("Eesti haldusüksuste lipp")

canva = Canvas(width=1000, height=500, bg="white")
canva.pack()



rec = canva.create_rectangle(0, 250, 1000, 500, fill="#2A8F43", outline="green")

vapp_red_rectangle = canva.create_rectangle(420, 100, 470, 30, fill="red", outline="black")
vapp_yellow_rectangle = canva.create_rectangle(500, 100, 550, 30, fill="yellow", outline="black")

vapp_blue_rectangle = canva.create_rectangle(420, 121, 470, 190, fill="blue", outline="black")
vapp_red2_rectangle = canva.create_rectangle(500, 121, 550, 190, fill="red", outline="black")

vapp_blue_laine = canva.create_arc(420, 143, 520, 240, start=180, extent=90, fill="blue", outline="black")
vapp_red2_laine = canva.create_arc(451, 142, 550, 240, start=270, extent=90, fill="red", outline="black")

üleval_valge_ristkülik = canva.create_rectangle(470, 100, 500, 30, fill="white", outline="")
all_valge_ristkülik = canva.create_rectangle(470, 121, 500, 240, fill="white", outline="")
vasak_valge_ristkülik = canva.create_rectangle(420, 100, 485, 120, fill="white", outline="")
parem_valge_ristkülik = canva.create_rectangle(485, 100, 550, 120, fill="white", outline="")

kollane_kasti_line = canva.create_line(550, 100, 500, 100)
punane_kasti_line = canva.create_line(420, 100, 470, 100)


up_line = canva.create_line(470, 30, 500, 30)
left_line = canva.create_line(420, 100, 420, 122)
right_line = canva.create_line(550, 100, 550, 122)

left_tipp = canva.create_line(470, 240, 485, 248, width=1.5)
right_tipp = canva.create_line(500, 240, 485, 248, width=1.5)



windows.mainloop()