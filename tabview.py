from tkinter import *
from customtkinter import *
from functools import partial

set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
set_default_color_theme("theme.json")  # Themes: "blue" (standard), "green", "dark-blue"

root = CTk()

root.title('tabs')
root.geometry('1200x700')

recyclable_mats = [
    ["paper towels", "tissues", "food waste"],
    ["1 plastics", "2 plastics", "4 plastics"],
    ["cans", "tins", "metals"]
]

root.grid_rowconfigure(0, weight=1)

def window (material):

    def bye():
        woof.destroy()
        woof.update()

    woof = CTkToplevel(root)
    woof.attributes("-topmost", True)
    woof.geometry("700x500")
    woof_bye = CTkButton(woof, text="Close", font = ('Ebrima', 30), command = bye)
    woof_bye.grid(row=0, column=0, pady=200)
    label = CTkLabel(woof, text=material.capitalize(), fg_color="transparent")
    label.grid(row=1, column=1, pady=10)
   
   
sidebar_frame = CTkFrame(root, width=140, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsw")
sidebar_frame.grid_rowconfigure(2, weight=1)
logo_label = CTkLabel(sidebar_frame, text="CustomTkinter", font=CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0)
buttontt = CTkButton(sidebar_frame, text="shsf")
buttontt.grid(row=1, column=0)




tabview = CTkTabview(root, width=700, height=500)
tabview.grid(row=2, column=2, padx=20, pady=20)

tabview.add("Recycling")  # add tab at the end
tabview.add("Transportation")  # add tab at the end
tabview.add("Power")
tabview.set("Recycling")  # set currently visible tab

mats_frame = CTkScrollableFrame(tabview.tab("Recycling"), label_text="Materials", width=700, height=400)

entry = CTkEntry(root, placeholder_text="Enter New Material Here", width=500)
entry.grid(row=3, column=3, pady=10)

new_material_requests = []

def newmats():
    new_material_requests.append(entry.get())
    print(new_material_requests)

new_material = CTkButton(root, text="Submit", command=newmats)
new_material.grid(row=4, column=4, pady=10)


print(entry.get())




for mats in range(len(recyclable_mats)):
    for line in range(len(recyclable_mats[mats])):
        label = recyclable_mats[mats][line].capitalize()
        material_type = partial(window, recyclable_mats[mats][line])


    
        button = CTkButton(master=mats_frame, text = label, width=500, height=50, command=material_type)
        button.pack(pady=10)
        

mats_frame.pack(pady=30)
mats_frame.pack(pady=5)

root.mainloop()