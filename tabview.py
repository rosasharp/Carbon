from tkinter import *
from customtkinter import *
from functools import partial
from PIL import Image

import json
import requests
import urllib.parse
import tomtom

API_KEY = "OHxATlRctIBu8dHAiRIggj3pzhPGGKhj"

map_placeholder = CTkImage(Image.open("116FBDD6-F6B9-4C9B-A5D3-F2B33760A688.jpg"), size=(400,400))

set_appearance_mode("System")  #sets appearance mode same as system(doesn't matter much as I only have one mode, no light or dark mode)
set_default_color_theme("theme.json")  #json file storage for the colours of my GUI

root = CTk()

root.title('CARBON')
root.geometry('1200x700')

recyclable_mats = [
    ["paper towels", "tissues", "food waste"],
    ["1 plastics", "2 plastics", "4 plastics"],
    ["cans", "tins", "metals"]
]#The list of materials for the scrollable frame of recycling materials

def transportation_car_info(): #Changes text box on transportation tab to car information
    transportation_info.configure(text="car stuff")

def transportation_walk_info(): #Changes text box on transportation tab to walking information
    transportation_info.configure(text=walkin)

def transportation_bike_info(): #Changes text box on transportation tab to biking information
    transportation_info.configure(text="bike stuff")

def transportation_bus_info():
    transportation_info.configure(text="bus stuff")

def display_distance(distance):
    transportation_info.configure(text= distance)

def window (material):  #Opens an information window of the different material buttons

    def bye():  #Closes window when close button pressed
        woof.destroy()
        woof.update()

    woof = CTkToplevel(root)
    woof.attributes("-topmost", True)
    woof.geometry("700x500")
    woof_bye = CTkButton(woof, text="Close", font = ('Ebrima', 30), command = bye)
    woof_bye.grid(row=1, column=3, pady=5)
    label = CTkLabel(woof, text=material.capitalize(), fg_color="transparent")
    label.grid(row=1, column=1, pady=10)

def newmats():  #Adds the new material requesrs to a list
    new_material_requests.append(entry.get())
    print(new_material_requests)

API_KEY = "OHxATlRctIBu8dHAiRIggj3pzhPGGKhj"

def api_router(location_entry, destination_entry ):
    final = tomtom.route(
        API_KEY,
       tomtom.geocode(API_KEY, location_entry.get()),
        tomtom.geocode(API_KEY, destination_entry.get()),
        "combustion",
        "8.7438",
        "eco"
        )
    with open("route.json", "w") as f:
        json.dump(final, f)

    kilometers = int(final["routes"][0]["summary"]["lengthInMeters"]) / 1000
    minutes = int(final["routes"][0]["summary"]["travelTimeInSeconds"]) / 60
    traffic = int(final["routes"][0]["summary"]["trafficDelayInSeconds"]) / 60

    def time_variables =
    


    distance_string = (
    f"Your destination is {kilometers} kilometers away and it will take {minutes} minutes to get there."
    )
    walking_time = (
    f"Your destination is {kilometers} kilometers away and it will take {kilometers/4.8} minutes to get there."
    )


    if traffic > 0:
        print(f"There is a traffic delay of {traffic} minutes.")

    

def locations():  #Adds the new material requesrs to a list
    locations_list.append(entry.get())
    print(location_entry.get())
    print(destination_entry.get())
    distance = api_router(location_entry, destination_entry)
    display_distance(distance)

root.grid_rowconfigure((0, 1, 2), weight=1)

#Sidebar for homepage
sidebar_frame = CTkFrame(root, width=140, height=200, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
sidebar_frame.grid_rowconfigure(2, weight=1)
logo_label = CTkLabel(sidebar_frame, text="CustomTkinter", font=CTkFont(size=20, weight="bold"))
logo_label.grid(row=0, column=0, pady=5)
buttontt = CTkButton(sidebar_frame, text="shsf")
buttontt.grid(row=1, column=0, pady=5)

#Creates the three different tabs
tabview = CTkTabview(root, width=700, height=700)
tabview.grid(row=2, column=3, padx=40, pady=20, )

tabview.add("Recycling")  # add tab at the end
tabview.add("Transportation")  # add tab at the end
tabview.add("Power")
tabview.set("Recycling")  # set currently visible tab

#Creates scrollable frame for buttons
mats_frame = CTkScrollableFrame(tabview.tab("Recycling"), label_text="Materials",  width=500, height=400, label_font=('Ebrima', 20))
mats_frame.pack(pady=5)
mats_frame.pack(pady=5)

#Where user can input materials not on list
entry = CTkEntry(tabview.tab("Recycling"), placeholder_text="Enter New Material Here", width=500)
entry.pack(pady=15)#grid(#row=3, column=2, pady=10)

new_material_requests = []

new_material = CTkButton(tabview.tab("Recycling"), text="Submit", command=newmats)
new_material.pack(pady=10)

print(entry.get())

transportation_info = CTkLabel(tabview.tab("Transportation"), text = "", width=500, height=100, corner_radius=10, font = ('Ebrima', 20))
transportation_info.grid(row=7, column=2, pady=5, padx=10)

location_entry = CTkEntry(tabview.tab("Transportation"), placeholder_text="Location:", width=500)
location_entry.grid(row=4, column=2, pady=5)

destination_entry = CTkEntry(tabview.tab("Transportation"), placeholder_text="Destination", width=500)
destination_entry.grid(row=5, column=2)

location_entry_button = CTkButton(tabview.tab("Transportation"), text="Submit", command=locations)
location_entry_button.grid(row=6, column=2)

locations_list = []


transportation_method_frame= CTkFrame(tabview.tab("Transportation"), width=50, height=50)
transportation_method_frame.grid(row=1, column=0, pady=5)

transportation_button_title = CTkLabel(transportation_method_frame, text = "Transportation Buttons", width=20, height=10, corner_radius=10, font = ('Ebrima', 15))
transportation_button_title.grid(row=0, column=0, pady=10)

car_button = CTkButton(transportation_method_frame, text="Car", width=100, height=50, command=transportation_car_info)
car_button.grid(row=1, column=0, pady=5, padx=10)
walk_button = CTkButton(transportation_method_frame, text="Walk", width=100, height=50, command=transportation_walk_info)
walk_button.grid(row=2, column=0, pady=5, padx=10)
bike_button = CTkButton(transportation_method_frame, text="Bike", width=100, height=50, command=transportation_bike_info)
bike_button.grid(row=3, column=0, pady=5, padx=10)
bus_button = CTkButton(transportation_method_frame, text="Bus", width=100, height=50, command=transportation_bus_info)

map_for_now = CTkLabel(tabview.tab("Transportation"), image= map_placeholder, width = 400, height = 400, corner_radius=10)
map_for_now.grid(row=1, column=2)

for mats in range(len(recyclable_mats)):
    for line in range(len(recyclable_mats[mats])):
        label = recyclable_mats[mats][line].capitalize()
        material_type = partial(window, recyclable_mats[mats][line])


    
        button = CTkButton(master=mats_frame, text = label, width=500, height=50, command=material_type)
        button.pack(pady=10)
        
mats_frame.pack(pady=5)
mats_frame.pack(pady=5)
#transportation_info.pack(pady=30)

root.mainloop()

