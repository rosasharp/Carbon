from tkinter import *
from customtkinter import *
from functools import partial
from PIL import Image

import json
import requests
import urllib.parse
import tomtom

class APIRouter:
    def __init__(self):
        self.kilometers=0
        self.minutes=0
    def route(self, location, destination, API_KEY):
        final = tomtom.route(
            API_KEY,
        tomtom.geocode(API_KEY, location),
            tomtom.geocode(API_KEY, destination),
            "combustion",
            "8.7438",
            "eco"
            )
        with open("route.json", "w") as f:
            json.dump(final, f)
            #uses information from json file to get information for API for transportation function

        self.kilometers = int(final["routes"][0]["summary"]["lengthInMeters"]) / 1000
        self.minutes = int(final["routes"][0]["summary"]["travelTimeInSeconds"]) / 60

API_KEY = "OHxATlRctIBu8dHAiRIggj3pzhPGGKhj"

map_placeholder =CTkImage(Image.open("116FBDD6-F6B9-4C9B-A5D3-F2B33760A688.jpg")
, size=(400,400))

set_appearance_mode("System")  #sets appearance mode same as system(doesn't matter much as I only have one mode, no light or dark mode)
set_default_color_theme("theme.json")  #json file storage for the colours of my GUI

root = CTk()
router = APIRouter()

root.title('CARBON')
root.geometry('1200x700')

recyclable_mats = [
    ["paper towels", "tissues", "food waste"],
    ["number 1 plastics", "number 2 plastics", "number 3 plastics", 
     "number 4 plastics", "number 5 plastics", "number 6 plastics", 
     "number 7 plastics"],
    ["cans", "tins", "metals"]
]#The list of materials for the scrollable frame of recycling materials

recyclable_mats_dictionary = { 
    "Paper towels": "paper towels can compost", 
    "Tissues": "tissues can compost",
    "Food waste": "food waste can compost",
    "Number 1 plastics": "Number 1 plastics can go in the regular council recycling bins that get collected by the kerbside recycling trucks.", 
    "Number 2 plastics":'Number 2 plastics can go in the regular council recycling bins that get collected by the kerbside recycling trucks.', 
    "Number 3 plastics": 'Number 3 plastics (PVC) aren’t recyclable and have to go into general waste.', 
     "Number 4 plastics": 
     '''Number 4 plastics that are hard/solid plastics are able to go in the kerbside recycling, 
     but soft plastics have to go in the general waste or soft plastic recycling. 
     Most supermarkets in New Zealand collect soft plastics for recycling''', 
     "Number 5 plastics" : 'All number 5 plastics can go in the regular council recycling bins that get collected by the kerbside recycling trucks', 
     "Number 6 plastics": 
     '''Number 6 plastics, or Polystyrene, are difficult to recycle. 
     Polystyrene is harder to recycle, as EXPOL only has 25 locations nationwide 
                         that collect and recycle polystyrene to turn into their products. ''', 
     "Number 7 plastics": "number 7 plastic stuff",
    "Cans" : "can stuff", 
    "Tins": 
    '''Tins can go in the regular council recycling bins 
    that get collected by the kerbside recycling trucks"''', 
    "Metals":
    '''New Zealand has great metal recycling systems, 
especially for metal, so just search up nearest place to recycle the metal type
near you. This or take to a waste transfer station.'''
}
#information about the materials

power_method_dictionary = {
    "Solar Power": '''Solar energy is very efficient as it works in all weather types, 
    and creates more than enough energy for heat, cooling, electricity and everything else. 
    It’s only slightly unreliable sometimes, depending on location.''',
    "Hydro Power": "Hydro power stuff"



}







def transportation_car_info(): #Changes text box on transportation tab to car information
    transportation_info.configure(text=(
    f"Your destination is {router.kilometers} kilometers away and it will take {router.minutes} minutes to get there."
    ))
    # transportation_info.configure = distance

def transportation_walk_info():
    time_in_minutes=int(int(router.kilometers))/4.8 #Changes text box on transportation tab to walking information
    transportation_info.configure(text=(
    f"Your destination is {router.kilometers} kilometers away and it will take {time_in_minutes} minutes to get there."
    ))
    # transportation_info.configure = distance

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
    woof_bye = CTkButton(woof, text="Close", font = ('Ebrima', 30), 
    command = bye, width=20, height=20)
    woof_bye.grid(row=2, column=1, pady=5)
    label = CTkLabel(woof, text=material, text_color="#DCE4EE",
    font = ('Ebrima', 15), width = 50)
    label.grid(row=1, column=1, pady=10)

    # if material == 'Tissues':
    #     label.configure(text = "Tissues can compost")

    # if material == 'Paper towels':
    #     label.configure(text='Paper towels can compost')

    # if material == 'Food waste':
    #     label.configure(text = 'Food waste can compost')

    # if material == 'Metals':
    #     label.configure(text = '''New Zealand has great metal recycling systems, 
    #     especially for metal, so just search up nearest place to recycle the metal type near you. 
    #     This or take to a waste transfer station.''')

    # if material == 'Tins':
    #     label.configure(text = "Tins can go in the regular council recycling bins that get collected by the kerbside recycling trucks")

    # if material == 'Number 1 plastics':
    #     label.configure(text = 'Number 1 plastics can go in the regular council recycling bins that get collected by the kerbside recycling trucks')

    # if material == 'Number 2 plastics':
    #     label.configure(text = 'Number 2 plastics can go in the regular council recycling bins that get collected by the kerbside recycling trucks')

    # if material == 'Number 3 plstics':
    #     label.configure(text = 'Number 3 plastics (PVC) aren’t recyclable and have to go into general waste. ')

    # if material == 'Number 4 plastics':
    #     label.configure(text = '''Number 4 plastics that are hard/solid plastics are able to go in the kerbside recycling, 
    # but soft plastics have to go in the general waste or soft plastic recycling. 
    # Most supermarkets in New Zealand collect soft plastics for recycling''')
        
    # if material == 'Number 5 plastics':
    #     label.configure(text = 'All number 5 plastics can go in the regular council recycling bins that get collected by the kerbside recycling trucks')

    # if material == 'Number 6 plastics':
    #     label.configure(text = '''Number 6 plastics, or Polystyrene, are difficult to recycle. 
    # Polystyrene is harder to recycle, as EXPOL only has 25 locations nationwide 
    #                     that collect and recycle polystyrene to turn into their products. ''')
        
    label.configure(text = recyclable_mats_dictionary[material])

def newmats():  #Adds the new material requesrs to a list
    new_material_requests.append(entry.get())
    print(new_material_requests)

# def locations():  #Finds the distance and gets the locations user inputs
#     locations_list.append(entry.get())
#     print(location_entry.get())
#     print(destination_entry.get())
#     distance = api_router(location_entry, destination_entry)
#     display_distance(distance)
    

def power_budget(budget):  #Makes sure the budget input is numeric and presents this to the user
    if budget.isnumeric():
        budget_list.append(budget)
        print(budget_list)
        validation_info.configure(text = f"Your budget has been set as ${budget_list[-1]}NZD")
        budget = budget_list[-1]
    else:
        validation_info.configure(text="incorrect input try again")
        solar_button.state = "disabled"
        hydro_button.state = "disabled"

    if int(budget_list[-1]) < 12000:
        power_availablility.configure(text = "Solar Power costs more than 12000 to install")
        power_information.configure(text="")
        solar_button._state = "disabled"

    else:
        power_availablility.configure(text="")
        solar_button._state = "normal"


       

    

def power_info(power, power_information):
    

    power_information.configure(text = power_method_dictionary[power])







root.grid_rowconfigure((0, 1, 2), weight=1)

#Sidebar for homepage
sidebar_frame = CTkFrame(root, width=140, height=200, corner_radius=0)
sidebar_frame.grid(row=0, column=0, rowspan=2, sticky="nsew")
sidebar_frame.grid_rowconfigure(2, weight=1)
logo_label = CTkLabel(sidebar_frame, text="CustomTkinter", 
font=CTkFont(size=20, weight="bold"))
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
mats_frame = CTkScrollableFrame(tabview.tab("Recycling"), 
label_text="Materials", width=500, height=400, label_font=('Ebrima', 20))
mats_frame.pack(pady=5)
mats_frame.pack(pady=5)

#Where user can input materials not on list
entry = CTkEntry(tabview.tab("Recycling"), 
placeholder_text="Enter New Material Here", width=500)
entry.pack(pady=15)#grid(#row=3, column=2, pady=10)

new_material_requests = []

new_material = CTkButton(tabview.tab("Recycling"), text="Submit", 
command=newmats)
new_material.pack(pady=10)
#Button to submit the new material to a list

print(entry.get())

transportation_info = CTkLabel(tabview.tab("Transportation"), text = "", 
width=500, height=100, corner_radius=10, font = ('Ebrima', 20), text_color= "#DCE4EE")
transportation_info.grid(row=7, column=2, pady=5, padx=10)
#Transportation label with information about it

location_entry = CTkEntry(tabview.tab("Transportation"), 
placeholder_text="Location:", width=500)
location_entry.grid(row=4, column=2, pady=5)
#User inputs location

destination_entry = CTkEntry(tabview.tab("Transportation"), 
placeholder_text="Destination", width=500)
destination_entry.grid(row=5, column=2)
#User inputs destination

location_entry_button = CTkButton(tabview.tab("Transportation"), 
text="Submit", command= lambda: router.route(location_entry.get(), destination_entry.get(), API_KEY))
location_entry_button.grid(row=6, column=2)
#User submits location and destination

locations_list = []


transportation_method_frame= CTkFrame(tabview.tab("Transportation"), 
width=50, height=50)
transportation_method_frame.grid(row=1, column=0, pady=5)
#Frame for the transportation methods to be displatyed

input_info = CTkLabel(tabview.tab("Transportation"), width=200, height=50, text = 
"Please input the addresses as 'number street name, suburb, city'. Otherwise it won't be valid", text_color= "#DCE4EE")
input_info.grid(row=2, column=2)

transportation_button_title = CTkLabel(transportation_method_frame, 
text = "Transportation Buttons", width=20, height=10, corner_radius=10, 
font = ('Ebrima', 15))
transportation_button_title.grid(row=0, column=0, pady=10)
#Title above where transportation methods are

car_button = CTkButton(transportation_method_frame, text="Car", width=100, 
height=50, 
command=transportation_car_info)
car_button.grid(row=1, column=0, pady=5, padx=10)
walk_button = CTkButton(transportation_method_frame, text="Walk", width=100, 
height=50, 
command=transportation_walk_info)
walk_button.grid(row=2, column=0, pady=5, padx=10)
bike_button = CTkButton(transportation_method_frame, text="Bike", width=100, 
height=50, command=transportation_bike_info)
bike_button.grid(row=3, column=0, pady=5, padx=10)
bus_button = CTkButton(transportation_method_frame, text="Bus", width=100, 
height=50, command=transportation_bus_info)
#Transportation method buttons

#map_for_now = CTkLabel(tabview.tab("Transportation"), image= map_placeholder, 
#width = 400, height = 400, corner_radius=10)
#map_for_now.grid(row=1, column=2)

for mats in range(len(recyclable_mats)): #Opens a window when the user presses a material button
    for line in range(len(recyclable_mats[mats])):
        label = recyclable_mats[mats][line].capitalize()
        


    
        button = CTkButton(master=mats_frame, text = label, width=500, 
        height=50)
        button.configure(command = lambda l=label: window(l))
        button.pack(pady=10)
        
mats_frame.pack(pady=5)
mats_frame.pack(pady=5)
#transportation_info.pack(pady=30)

budget_input=CTkEntry(tabview.tab("Power"), placeholder_text="Power budget:", 
width=150)
budget_input.grid(row=1, column=1)
#Where user can input their power budget

budget_list=[]

budget_submit = CTkButton(tabview.tab("Power"), text="Submit", 
command=lambda: power_budget(budget_input.get()))
budget_submit.grid(row=1, column=2)
#User submits budget and it's validated

validation_info= CTkLabel(tabview.tab("Power"), text = "", text_color= "#DCE4EE")
validation_info.grid(row=2, column=1, pady=20)
#Displays to the user if their data is valid

power_information = CTkLabel(tabview.tab("Power"), text = "", text_color="#DCE4EE")
power_information.grid(row = 2, column=3)

solar_button= CTkButton(tabview.tab("Power"), text = "Solar Power", command= lambda: power_info("Solar Power", power_information))
solar_button.grid(row=3, column=1, pady=20)

hydro_button = CTkButton(tabview.tab("Power"), text = "Hydro Power", command = lambda: power_info("Hydro Power", power_information))
hydro_button. grid(row=4, column=1, pady=20)

#Power type buttons to display the information about them

power_availablility = CTkLabel(tabview.tab("Power"), text = "", text_color="#DCE4EE")
power_availablility.grid(row=4, column=2)









root.mainloop()
