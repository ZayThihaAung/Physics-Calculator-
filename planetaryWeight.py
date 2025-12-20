# Formula : W = m * g
# Ask user's mass and planet
# Let the user choose multiple planets in one run.
# Add a loop to allow repeated calculations.
# Use matplotlib to plot weight on all planets for comparison.
from matplotlib import pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

planets_gravity = {
  "Earth" : 9.81,
  "Jupiter" : 24.79,
  "Mars" : 3.7,
  "Venus" : 8.87,
  "Saturn" : 10.44,
  "Uranus" : 8.69,
  "Neptune" : 11.15,
  "Mercury" : 3.7
}

obj_weight = []
obj_weight2 = []
planet_names = []

# Window Set Up
root = tk.Tk()
root.resizable(False, False)
root.title("Planetary Weight Calculator")
root.geometry('450x400')
tk.Label(root, text="Planetary Weight Calculator", font=("Helvetica Bold", 16)).pack(pady=10)
tk.Label(root, text="This calculates the weight of an object on different planets.", font=("Helvetica Bold", 13)).pack(pady=5)

tk.Label(root, text="Enter Mass of Object (kg)", font=("Helvetica", 10)).pack()
entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack(pady=10, fill="x")

tk.Label(root, text="Enter Mass of Second Object (kg)", font=("Helvetica", 10)).pack()
entry2 = tk.Entry(root, font=("Helvetica", 14))
entry2.pack(pady=10, fill="x")

combo = ttk.Combobox(root, values=list(planets_gravity.keys()), state="readonly")
combo.current(0)
combo.pack(pady=10, fill="x")

def caculator() :
  try:
    mass = float(entry.get())
    mass2 = float(entry2.get())
    planets_name = combo.get()
    weight = mass * planets_gravity[f"{planets_name}"]
    weight2 = mass2 * planets_gravity[f"{planets_name}"]
    messagebox.showinfo("Weight Calculation", f"The weight of the first object on {planets_name} is: {weight} N\nThe weight of the second object on {planets_name} is: {weight2} N")

    for items in planets_gravity:
      calculation = mass * planets_gravity[items]
      calculation2 = mass2 * planets_gravity[items]
      planet_names.append(items.capitalize())
      obj_weight.append(calculation)
      obj_weight2.append(calculation2)

    plt.scatter(planet_names, obj_weight, color='green', label = "First Body")
    plt.scatter(planet_names, obj_weight2, color='red', label = "Second Body")
    plt.legend() # Crucial for labels
    plt.xlabel("Planets (Solar System)")
    plt.ylabel("Bodys' weights (N)")
    plt.title("Weight Comparison Across Planets")
    plt.grid()
    plt.show()

    obj_weight.clear()
    obj_weight2.clear()
    planet_names.clear()
  except ValueError:
    messagebox.showerror("Input Error", "Please enter valid numerical values for mass and a valid planet name.")
    caculator()

caculate_button = tk.Button(root, text="Calculate Weights", font=("Helvetica Bold", 14), command=caculator,
                            bg="#0B706A", fg="white", padx=10, pady=5)
caculate_button.pack(pady=20)

root.mainloop()
