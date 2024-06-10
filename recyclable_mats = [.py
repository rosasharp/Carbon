from tkinter import *
from customtkinter import *
from functools import partial


set_default_color_theme("theme.json")  # Themes: "blue" (standard), "green", "dark-blue"
set_appearance_mode("dark")
#root = Tk()
root = CTk()

root.title('Recycling Information')
root.geometry('800x600')

recyclable_mats = [
    ["paper towels", "tissues", "food waste"],
    ["1 plastics", "2 plastics", "4 plastics"],
    ["cans", "tins", "metals"]

]



def window (material):

    def bye():
        woof.destroy()
        woof.update()

    woof = CTkToplevel(root)
    woof.attributes("-topmost", True)
    woof.geometry("600x300")
    woof_bye = CTkButton(woof, text=material, font = ('Ebrima', 30), command = bye)
    woof_bye.pack(pady=80)


mats_frame = CTkScrollableFrame(root, label_text="Materials", width=700, height=400)

for mats in range(len(recyclable_mats)):
    for line in range(len(recyclable_mats[mats])):
        label = recyclable_mats[mats][line].capitalize()
        material_type = partial(window, recyclable_mats[mats][line])

        button = CTkButton(master=mats_frame, text = label, width=500, height=50, command=material_type)
        button.pack(pady=10)


mats_frame.pack(pady=30)


root.mainloop()