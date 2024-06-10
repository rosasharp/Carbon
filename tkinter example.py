import tkinter as tk

window = tk.Tk()

label = tk.Label(window,
    text="Hello, Tkinter",
    foreground="white",  # Set the text color to white
    background="black" , # Set the background color to black
    width=40,
    height=40
)

button = tk.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)

label.pack()
button.pack()

window.mainloop()