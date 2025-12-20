import math
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

planets_mass = {
  "Earth": 5.9e24,
  "Mars" : 6.4e23,
  "Jupiter" : 1.8e27,
  "Mercury" : 3.3e23,
  "Venus" : 4.8e24,
  "Uranus" : 2.6e25,
  "Saturn" : 5.6e26,
  "Neptune" : 1e26
}
planets_raduis = {
  "Earth": 6378,
  "Mars" : 3389.5,
  "Jupiter" : 69911,
  "Mercury" : 2439.7,
  "Venus" : 6051.8,
  "Uranus" : 25362,
  "Saturn" : 58232,
  "Neptune" : 24622
}

# Window setup
root = tk.Tk()
root.resizable(False, False)
root.title("Escape Velocity Calculator")
root.geometry('500x300')

tk.Label(root, text="Escape Velocity Calculator", font=("Helvetica", 16)).pack(pady=10)
tk.Label(root, text="Select the name of the planet to calculate its escape velocity.", font=("Helvetica", 10)).pack(pady=5)

def calculate():
  try :    
    pos_x = []
    pos_y = []

    name = entry.get()
    G = 6.77e-11
    escape_v = math.sqrt(2 * G * planets_mass[f"{name}"] / planets_raduis[f"{name}"])
    last_convert = escape_v / 3600
    messagebox.showinfo("Result", f"The Velocity needed to escape {name} : {last_convert} km/h")

    for i in planets_mass:
      calculation = math.sqrt(2 * G * planets_mass[i] / planets_raduis[i])
      convertion = calculation / 3600
      pos_x.append(i.capitalize())
      pos_y.append(convertion)

    plt.scatter(pos_x, pos_y, color="green", label='escape velocity')
    plt.xlabel("Planets names")
    plt.ylabel("Velocity needed to escape (km/h)")
    plt.title("Escape Velocity Across Solar System")
    plt.legend()
    plt.grid()
    plt.show()
  except ValueError:
    messagebox.showerror("Error", "Please enter a valid planet name.")
    calculate()

entry = ttk.Combobox(root, values=list(planets_mass.keys()), state="readonly")
entry.current(0)
entry.bind("<<ComboboxSelected>>", lambda event: calculate())
entry.pack(pady=10, fill="x")
root.mainloop()
