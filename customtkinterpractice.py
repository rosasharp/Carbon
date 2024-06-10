from tkinter import *
from customtkinter import *
from PIL import Image
#themes and colors

set_default_color_theme("theme.json")  # Themes: "blue" (standard), "green", "dark-blue"
set_appearance_mode("dark")
#root = Tk()
root = CTk()

root.title('Tkinter.com - Custom Tkinter!')
root.geometry('800x600')

noah = CTkImage(Image.open("116FBDD6-F6B9-4C9B-A5D3-F2B33760A688.jpg"), size = (1000, 300))


def window ():

    def bye():
        woof.destroy()
        woof.update()

    woof = CTkToplevel(root)
    woof.attributes("-topmost", True)
    woof.geometry("600x300")
    woof_bye = CTkButton(woof, text='Go back', font = ('Ebrima', 30), command = bye)
    woof_bye.pack(pady=80)

def noah_window ():
    meow = CTkToplevel(root)
    meow.attributes("-topmost", True)
    meow.geometry('1500x1000')

    image = CTkLabel(meow, text="", image=noah, width=500, height=500)
    image.pack()


button_1 = CTkButton(root, text="hai :3", font = ('Ebrima', 30), command=window)
button_1.pack(pady=80)

button_2 = CTkButton(root, text="click for a surprise", font = ('Ebrima', 30), command=noah_window)
button_2.pack(pady = 80)





root.mainloop()