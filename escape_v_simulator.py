import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import math 

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
  "Earth": 6378 * 1000,
  "Mars" : 3389.5 * 1000,
  "Jupiter" : 69911 * 1000,
  "Mercury" : 2439.7 * 1000,
  "Venus" : 6051.8 * 1000,
  "Uranus" : 25362 * 1000,
  "Saturn" : 58232 * 1000,
  "Neptune" : 24622 * 1000
}

# Window Set Up
root = tk.Tk()
root.resizable(False, False)
root.title("Escape Velocity Simulator")
root.geometry('500x385')
tk.Label(root, text="Escape Velocity Simulator", font=("Helvetica Bold", 16)).pack(pady=10)
tk.Label(root, text="This simulates whether a rocket escapes the planet or not.", font=("Helvetica Bold", 13)).pack(pady=5)

tk.Label(root, text="Select Planet", font=("Helvetica", 10)).pack()
combo = ttk.Combobox(root, values=list(planets_mass.keys()), state="readonly")
combo.current(0)
combo.pack(pady=10, fill="x")

tk.Label(root, text="Initial Velocity (km/s)", font=("Helvetica", 10)).pack()
input = tk.Entry(root, font=("Helvetica", 14))
input.pack(pady=5, fill="x")

result = tk.StringVar(value="Initial Velocity: —")
result2 = tk.StringVar(value="Escape Velocity: —")
tk.Label(root, textvariable=result, font=("Arial", 14)).pack(padx=10, pady=5)
tk.Label(root, textvariable=result2, font=("Arial", 14)).pack(padx=10, pady=5)

def simulate() :
  planet_name = combo.get() 
  # Read user input (km/s) and convert to m/s for SI calculations
  velocity = float(input.get())

  # Gravitational constant (SI)
  G = 6.67430e-11  # m^3 kg^-1 s^-2

  # Calculate escape velocity
  escape_v = math.sqrt((2 * G * planets_mass[planet_name]) / planets_raduis[planet_name]) / 1000  # m/s

  g = G * planets_mass[planet_name] / (planets_raduis[planet_name] ** 2)  # m/s^2

  # Simulate vertical motion from surface (h=0) using constant gravity approximation
  pos_x = []
  pos_y = []
  t = 0.0
  interval = 0.1  # time step in seconds
  h = 0.0
  initial_height = 0.0  # meters
  max_time = 1e6  # safety cap to avoid infinite loops

  while h >= 0 and t <= max_time:
      h = initial_height + velocity * t - 0.5 * g * t ** 2
      pos_x.append(t)
      pos_y.append(h / 1000)  # store height in km for plotting
      if h < 0:
        break
      if t >= max_time or h >= 100e2:  # arbitrary high limit to consider escape
        break
      t += interval

  result.set(f"Initial Velocity: {velocity:.2f} km/s")
  result2.set(f"Escape Velocity: {escape_v:.2f} km/s")

  if velocity >= escape_v:
    messagebox.showinfo("Result", "Rocket escapes the planet's gravity!")
  else :
    messagebox.showinfo("Result", "Rocket does not escape the planet's gravity.")

  plt.plot(pos_x, pos_y, marker='o', label='rocket trajectory')
  plt.xlabel("Time (s)")
  plt.ylabel("Height (km)")
  plt.title(f"Rocket Escaping {planet_name}")
  plt.legend()
  plt.grid()
  plt.show()

simulate_button = tk.Button(root, text="Start Simulation", font=("Helvetica", 14),
                            bg="lightblue", fg="black", command=simulate)
simulate_button.pack(pady=20)

root.mainloop()
