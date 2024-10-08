
from tkinter import *
from customtkinter import *
from functools import partial

import json
import requests
import urllib.parse
import tomtom
import time     
import os

# Creates file for new materials
if not os.path.exists(os.path.expanduser("./Materials/Recycle")):
    os.mkdir(os.path.expanduser("./Materials/"))
    os.mkdir(os.path.expanduser("./Materials/Recycle"))


class APIRouter:
    '''Class takes in locations to output route json''' 

    def __init__(self):
        self.kilometers=0
        self.minutes=0

    def route(self, location, destination, API_KEY, validation_box):
        try:
            # Uses json file for API for transportation function
            final = tomtom.route(
                API_KEY,
            tomtom.geocode(API_KEY, location.get()),
                tomtom.geocode(API_KEY, destination.get()),
                "combustion",
                "8.7438",
                "eco"
                )
            with open("route.json", "w") as f:
                json.dump(final, f)
            self.kilometers = int(
                final["routes"][0]["summary"]["lengthInMeters"]
            ) / 1000
            self.minutes = int(
                final["routes"][0]["summary"]["travelTimeInSeconds"]
            ) / 60
            
            # Validation for location input
            validation_box.configure(text="Valid address, " +
            "please choose a transportation method.")
            car_button._state = 'normal'
            walk_button._state = 'normal'
            bike_button._state = 'normal'
            bus_button._state = 'normal'
        except:
            validation_box.configure(text="Invalid address. Input again.")
            car_button._state = 'disabled'
            walk_button._state = 'disabled'
            bike_button._state = 'disabled'
            bus_button._state = 'disabled'
            
           

API_KEY = "OHxATlRctIBu8dHAiRIggj3pzhPGGKhj"

# Sets appearance mode same as system(doesn't matter much as I only have one)
set_appearance_mode("System")  
# Json file storage for the colours of my GUI
set_default_color_theme("theme.json")  

root = CTk()
router = APIRouter()

root.title('CARBON')
root.geometry('1200x700')

recyclable_mats = [
    # The list of materials for the scrollable frame of recycling materials
    ["paper towels", "tissues", "food waste"],
    ["number 1 plastics", "number 2 plastics", "number 3 plastics", 
     "number 4 plastics", "number 5 plastics", "number 6 plastics", 
     "number 7 plastics"],
    ["cans", "tins", "metals"]
]

recyclable_mats_dictionary = { 
    # Information about the materials
    "Paper towels": 
    '''Paper towels can be composted. Compost bins are a great thing to have, 
    to put food scraps in. It reduces waste and can be useful for gardening.''', 
    "Tissues": 
    '''Tissues can be composted. Compost bins are a great thing to have, 
    to put food scraps in. It reduces waste and can be useful for gardening.''',
    "Food waste":
    '''Food waste can be composted. Compost bins are a great thing to have, 
    to put food scraps in. It reduces waste and can be useful for gardening.''',
    "Number 1 plastics": 
    '''Number 1 plastics can go in the regular council 
    recycling bins that get collected by the kerbside recycling trucks.''', 
    "Number 2 plastics":
    '''Number 2 plastics can go in the regular council 
    recycling bins that get collected by the kerbside recycling trucks.''', 
    "Number 3 plastics": 
    '''Number 3 plastics (PVC) aren’t recyclable 
        and have to go into general waste.''', 
     "Number 4 plastics": 
     '''Number 4 plastics that are hard/solid plastics are able to go in the 
     kerbside recycling, but soft plastics have to go in the general waste or 
     soft plastic recycling. Most supermarkets in New Zealand 
        collect soft plastics for recycling''', 
     "Number 5 plastics" : 
     '''All number 5 plastics can go in the regular council 
     recycling bins that get collected by the kerbside recycling trucks.''', 
     "Number 6 plastics": 
     '''Number 6 plastics, or Polystyrene, are difficult to recycle. 
     Polystyrene is harder to recycle, as EXPOL only has 25 locations nationwide 
        that collect and recycle polystyrene to turn into their products. ''', 
     "Number 7 plastics": "number 7 plastic stuff",
    "Cans" :   
    '''Cans can go in the regular council recycling bins 
    that get collected by the kerbside recycling trucks''', 
    "Tins": 
    '''Tins can go in the regular council recycling bins 
    that get collected by the kerbside recycling trucks''', 
    "Metals":
    '''New Zealand has great metal recycling systems, 
especially for metal, so just search up nearest place to recycle the metal type
near you. This or take to a waste transfer station.'''
}

power_method_dictionary = {
    # Information about power types
    "Solar Power": 
'''Solar energy is very efficient as it works in all weather types, and 
creates more than enough energy for heat, cooling, electricity and everything 
else. It’s only slightly unreliable sometimes, depending on location. 
A negative aspect of solar power is that it can be quite expensive to install, 
so for budgets lower than $12000, it mightn't be a possibility. 
The cost is reduced over time though as you pay the initial installation fee and
 then all the power is renewable. The initial cost for solar power is expensive,
but it is worth it due to how it is renewable. Solar power costs $0.10 per kWh. 
''',
    "Hydro Power": 
'''Hydro power already makes up 57 percent of power in New Zealand. 
Hydroelectric schemes use gravity to drive water through turbines, 
converting that energy into electricity. Water from streams, rivers or dams 
flows down steep pipes into turbines, which drive power generators. 
The water then flows back into a river or stream below the hydro plant. 
Research if your power comes from a hydro power plant, as it is much more 
environmentally friendly, while also being low-cost. 
Hydro power costs $0.05 per kWh. ''',
    "Wind Power": 
'''Wind power or wind energy is a form of renewable energy that harnesses the 
power of the wind to generate electricity. It involves using wind turbines to 
convert the turning motion of blades, pushed by moving air (kinetic energy) 
into electrical energy (electricity). Wind energy is typically more accessible 
in rural areas where wind farms are, but New Zealand is currently growing its 
wind farms. It is very efficient, while also only costing $0.04-0.06 per kWh.
''',
    "Geothermal Power": 
    '''New Zealand has a number of geothermal areas as it sits over 2 active 
    plates - the Indo-Australian and Pacific Plates. Geothermal energy has many 
    benefits such as being relatively cost effective, reliable, sustainable, 
    and relatively environmentally friendly. Geothermal energy is much better 
    for the environment than the burning of fossil fuels. It is relatively 
    easily accessible in New Zealand, and is very cost effective, as it 
    is $0.07 per kWh''',
    "Bio Power": 
    '''Biopower technologies convert renewable biomass fuels into heat and 
    electricity using processes similar to those used with fossil fuels. 
    There are three ways to release the energy stored in biomass to produce 
    biopower: burning, bacterial decay, and conversion to gas/liquid fuel. 
    The current use of biofuels in New Zealand is low, so it isn't very 
    accessible though, and it mainly used for industrial purposes and is 
    more expensive being between $0.8 to $0.15 kWh.'''
}

def transportation_car_info(): 
    '''Changes text box on transportation tab to car information'''

    # Finds distance and time for car journeys
    transportation_info.configure(text=(
    f"Your destination is {round(router.kilometers, 2)} kilometers away and " +
    f"it will take {round(router.minutes,2)} minutes to get there."
    ))
    # Makes walking recommendation because of short distances
    if router.kilometers < 3:
        transport_rec.configure(text= 
    '''Because this journey is less than 3km away, 
    walking would be the most carbon friendly mode of of transportation. 
    Select the walk option to see how long it will take.''')
    # Makes biking recommendation because of short/med distances
    elif router.kilometers <6: 
        transport_rec.configure(text= 
    '''Because this journey is less than 6km away, 
    biking would be the most carbon friendly mode of of transportation. 
    Select the bike option to see how long it will take.''')
    # Gives information about other methods for long journeys   
    else:
        transport_rec.configure(text='''
        Although driving is the most common form of transportation, 
        and is practical for longer journeys, it is the least carbon friendly 
        due to the emissions from cars. For shorter journeys, please consider 
        walking or biking. For longer journeys, public transportation 
        is another more carbon friendly option.''')

def transportation_walk_info():
    '''Changes text box on transportation tab to walking information'''

    # Finds time for walking using researched time calculation
    time_in_minutes=int(router.kilometers)*4.8 
    transportation_info.configure(text=(
    f"Your destination is {round(router.kilometers, 2)} kilometers away and" +
    f" it will take {round(time_in_minutes, 2)} minutes to get there."
    ))
    # Gives recommendation about why walking is a sustainable method
    transport_rec.configure(text=''' 
    Walking is a very carbon efficient mode of transportation, 
    producing no carbon footprint and allowing for excercise. 
    For journeys less than 3km, this is highly recommended.''')
  
def transportation_bike_info(): 
    '''Changes text box on transportation tab to biking information'''

    # Finds time for biking using researched time calculation
    time_in_minutes=int(router.kilometers)*1.7
    transportation_info.configure(text=(
    f"Your destination is {router.kilometers} kilometers away and it will" +
    f" take {time_in_minutes} minutes to get there."
    ))
    # Gives recommendation about why biking is a sustainable method
    transport_rec.configure(text=''' 
    Biking is a very carbon efficient mode of transportation, 
    producing no carbon footprint and allowing for excercise. 
    For journeys less than 6km, this is highly recommended. 
    Because you can take shortcuts, sometimes biking can be even faster 
    than driving!''')

def transportation_bus_info():
    '''Changes text box on transportation to bus information'''
    
    # Finds time for busing using researched time calculation
    time_in_minutes = int(router.kilometers) * 2
    transportation_info.configure(text=(
    f"Your destination is {round(router.kilometers, 2)} kilometers away and " +
    f"it will take {round(time_in_minutes,2)} minutes to get there."))
    # Gives recommendation about why busing is better than driving
    transport_rec.configure(text = ''' 
    Busing is more efficient than driving, as you are sharing the 
    carbon emissions amongst many people when on public transportation. 
    If you live by bus stops, and it is an option, 
    busing instead of taking one car is highly recommended.''')

def display_distance(distance):
    '''Displays the distance between locations to user'''

    transportation_info.configure(text= distance)

def window (material):  
    '''Opens an information window of the different material buttons'''

    def close_window():  
        '''Closes window when close button pressed'''

        mat_window.destroy()
        mat_window.update()

    mat_window = CTkToplevel(root)
    mat_window.grid_columnconfigure(0, weight=1)
    mat_window.grid_rowconfigure(0, weight=1)
    mat_window.attributes("-topmost", True)
    mat_window.geometry("700x500")
    mat_window_close = CTkButton(mat_window, text="Close", 
    font = ('Ebrima', 30), command = close_window, width = 20, height = 20)
    mat_window_close.grid(row = 1, column = 0, pady = 5, sticky = "s")
    label = CTkLabel(mat_window, text = material, text_color = "#DCE4EE", 
    corner_radius=10,
    font = ('Ebrima', 20), width = 50)
    label.grid(row = 0, column = 0, pady = 10, )
    label.configure(text = recyclable_mats_dictionary[material])

def newmats():  
    '''Adds the new material requesrs to a list anf then adds it to a file'''
    
    if entry.get() == "":
        #Won't submit an empty entry
        mat_validation.configure(text = "Invalid, field is empty")
    elif not entry.get().isnumeric():
        #Submits entry if it isn't numeric
        new_material_requests.append(entry.get())
        with open(
        f"{os.path.expanduser('./Materials/Recycle')}/newmats.json", "w"
        ) as w:
            json.dump(new_material_requests, w)
        print(new_material_requests)
        mat_validation.configure(text = "Submitted. Thank you.")
    else: 
        #Doesn't allow other (numeric) values to be submitted
        mat_validation.configure(text = "Numeric only inputs are invalid.")

def power_budget(budget): 
    '''Makes sure the budget input is numeric and presents this to the user'''

    if budget.isnumeric():
        #Allows numeric entries to be valid and enable buttons
        budget_list.append(budget)
        print(budget_list)
        validation_info.configure(text = 
        f"Your budget has been set as ${budget_list[-1]}NZD")
        budget = budget_list[-1]
        solar_button._state = "normal"
        hydro_button._state = "normal"
        wind_power_button._state = "normal"
        geothermal_button._state = "normal"
        bioenergy_button._state = "normal"
    else:
        #Doesn't allow non numbers, and disables buttons
        validation_info.configure(text = "Invalid input, try again", 
        font = ('Ebrima', 13))
        solar_button._state = "disabled"
        hydro_button._state = "disabled"
        wind_power_button._state = "disabled"
        geothermal_button._state = "disabled"
        bioenergy_button._state = "disabled"
        power_information.configure(text="")

    if int(budget_list[-1]) <= 60:
        solar_button._state = "disabled"
  
    else: 
        solar_button._state = "normal"
        power_availablility.configure(text="")
    
    if int(budget_list[-1]) <= 30:
        hydro_button._state = "disabled"
        wind_power_button._state = "disabled"
       
    else:
        hydro_button._state = "normal"
        wind_power_button._state = "normal"
        power_availablility.configure(text="")

    if int(budget_list[-1]) <= 45:
        geothermal_button._state = "disabled"

    else:
        geothermal_button._state = "normal"
        power_availablility.configure(text="")

    if int(budget_list[-1]) <= 85:
        bioenergy_button._state = "disabled"

    else:
        bioenergy_button._state = "normal"
        power_availablility.configure(text="")





def power_info(power, power_information):
    '''Shows the information about the power type selected'''

    power_information.configure(text=power_method_dictionary[power], 
    font=('Ebrima', 20))

root.grid_rowconfigure((0, 1, 2), weight=1)

# Creates the three different tabs
tabview = CTkTabview(root, width=900, height=700)
tabview.grid_rowconfigure(0, weight=1)
tabview.grid_columnconfigure((0,1), weight=1)
tabview.grid(row=0, column=0, padx=200, pady=50, sticky="NSEW")

tabview.add("Home") # Add tab at the end
tabview.add("Recycling")  # Add tab at the end
tabview.add("Transportation")  # Add tab at the end
tabview.add("Power") # Add tab at the end
tabview.set("Home")  # Set currently visible tab

# Introductory information on home tab
home_information = CTkLabel(tabview.tab("Home"), 
text='''Hello! Welcome to my Carbon program. 

The goal of this is to provide people with information on how they can reduce
their carbon footprint in their day to day life. It tells you how to recycle 
different materials, how to be more mindful with transportation options, 
and how sustainable energy sources can help reduce your carbon emissions. 
Together we can help the environment. Thank you :)''', 
font=('Ebrima', 20), width=500, height=500)
home_information.grid(row=0 , column=3, padx=100)

# Creates scrollable frame for buttons
mats_frame = CTkScrollableFrame(tabview.tab("Recycling"), 
label_text="Materials", width=500, height=300, 
label_font=('Ebrima', 20))
mats_frame.pack(pady=5)
mats_frame.pack(pady=5)

# Where user can input materials not on list
entry = CTkEntry(tabview.tab("Recycling"), 
placeholder_text="Enter New Material Here", width=500)
entry.pack(pady=15)

new_material_requests = []

# Button to submit the new material to a list
new_material = CTkButton(tabview.tab("Recycling"), text="Submit", 
command=newmats)
new_material.pack(pady=10)

# Displays text to inform the user on if their material is valid
mat_validation = CTkLabel(tabview.tab("Recycling"), text="", 
text_color="#DCE4EE")
mat_validation.pack(pady=10)

print(entry.get())

# Creates frame for widgets to sit in
transportation_method_frame= CTkFrame(tabview.tab("Transportation"), 
width=50, height=50)
transportation_method_frame.grid(row=1, column=0, pady=5)
transportation_method_frame.grid_columnconfigure(0, weight=1)
transportation_method_frame.grid_rowconfigure(0, weight=1)

# Transportation label with information about it
transportation_info = CTkLabel(transportation_method_frame, text="", 
width=500, height=100, corner_radius=10, font=('Ebrima', 20), 
text_color="#DCE4EE")
transportation_info.grid(row=7, column=2, pady=5, padx=10, sticky="s")

# User inputs location
location_entry = CTkEntry(transportation_method_frame, 
placeholder_text="Location:", width=500)
location_entry.grid(row=4, column=2, pady=5, sticky="s")

# User inputs destination
destination_entry = CTkEntry(transportation_method_frame, 
placeholder_text="Destination", width=500)
destination_entry.grid(row=5, column=2, sticky="s")

# User submits location and destination
location_entry_button = CTkButton(transportation_method_frame, 
text="Submit", command=lambda: router.route(
location_entry, destination_entry, API_KEY, validation_box))
location_entry_button.grid(row=6, column=2, sticky="s")

locations_list = []

# Frame for the transportation methods to be displayed
input_info = CTkLabel(transportation_method_frame, 
width=200, height=50, text= 
"Please input the addresses as 'number street name, suburb, city'." +
" Otherwise it won't be valid", 
text_color="#DCE4EE")
input_info.grid(row=2, column=2, sticky="s")

# Title above where transportation methods are
transportation_button_title = CTkLabel(transportation_method_frame, 
text="Transportation Buttons", width=20, height=10, corner_radius=10, 
font=('Ebrima', 15))
transportation_button_title.grid(row=0, column=0, pady=10, sticky="n")

# Transportation method buttons
car_button = CTkButton(transportation_method_frame, text="Car", width=100, 
height=50, command=transportation_car_info, state='disabled')
car_button.grid(row=1, column=0, pady=5, padx=10, sticky="w")
walk_button = CTkButton(transportation_method_frame, text="Walk", width=100, 
height=50, 
command=transportation_walk_info, state='disabled')
walk_button.grid(row=2, column=0, pady=5, padx=10, sticky="w")
bike_button = CTkButton(transportation_method_frame, text="Bike", width=100, 
height=50, command=transportation_bike_info, state='disabled')
bike_button.grid(row=3, column=0, pady=5, padx=10, sticky="w")
bus_button = CTkButton(transportation_method_frame, text="Bus", width=100, 
height=50, command=transportation_bus_info, state='disabled')
bus_button.grid(row=4, column=0, pady=5, padx=10, sticky="w")

# Informs user if their input is valid or not
validation_box = CTkLabel(transportation_method_frame, text="", 
text_color="#DCE4EE", font=('Ebrima', 15))
validation_box.grid(row=3, column=2, sticky="n")

# Provides information to user
transport_rec = CTkLabel(tabview.tab("Transportation"), text="", 
text_color="#DCE4EE", font=('Ebrima', 15), width=400, height=100)
transport_rec.grid(row=5, column=0, sticky="s")

# Opens a window when the user presses a material button
for mats in range(len(recyclable_mats)): 
    for line in range(len(recyclable_mats[mats])):
        label = recyclable_mats[mats][line].capitalize()
        
        button = CTkButton(master=mats_frame, text=label, width=500, 
        height=50)
        button.configure(command=lambda l=label: window(l))
        button.pack(pady=10)
        
mats_frame.pack(pady=5)
mats_frame.pack(pady=5)

# Where user can input their power budget
budget_input=CTkEntry(tabview.tab("Power"), 
placeholder_text="Power budget Per Month:", width=200)
budget_input.grid(row=1, column=1)

budget_list=[]

# User submits budget and it's validated
budget_submit = CTkButton(tabview.tab("Power"), text="Submit", 
command=lambda: power_budget(budget_input.get()))
budget_submit.grid(row=2, column=1)

# Displays to the user if their data is valid
validation_info = CTkLabel(tabview.tab("Power"), text="", 
text_color="#DCE4EE")
validation_info.grid(row=3, column=1, pady=20)

# Information about that power type
power_information = CTkLabel(tabview.tab("Power"), text="", 
text_color="#DCE4EE")
power_information.grid(row=5, column=2)

# Power type buttons to display the information about them
solar_button = CTkButton(tabview.tab("Power"), text="Solar Power", 
command=lambda: power_info("Solar Power", power_information), state='disabled')
solar_button.grid(row=4, column=1, pady=20)

hydro_button = CTkButton(tabview.tab("Power"), text = "Hydro Power", 
command=lambda: power_info("Hydro Power", power_information),state='disabled')
hydro_button.grid(row=5, column=1, pady=20)

wind_power_button = CTkButton(tabview.tab("Power"), text="Wind Power", 
command=lambda: power_info("Wind Power", power_information),state='disabled')
wind_power_button.grid(row=6, column=1, pady=20)

geothermal_button = CTkButton(tabview.tab("Power"), text="Geothermal Power", 
command=lambda: power_info("Geothermal Power", power_information),
state='disabled')
geothermal_button.grid(row=7, column=1, pady=20)

bioenergy_button = CTkButton(tabview.tab("Power"), text="Bio Power", 
command=lambda: power_info("Bio Power", power_information),state='disabled')
bioenergy_button.grid(row=8, column=1, pady=20)
power_availablility = CTkLabel(tabview.tab("Power"), 
text='''Buttons will be disabled if your budget doesn't meet the minimum 
requirements. Solar power costs more than $60 per month. Hydro and Wind power 
cost more than $30 per month. Geothermal energy costs more than $45 per month. 
Bio power costs more than $85 per month.''', 
text_color="#DCE4EE")
power_availablility.grid(row=2, column=2)

root.mainloop()
