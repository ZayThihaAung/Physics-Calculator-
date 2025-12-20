import math
import tkinter as tk
from tkinter import messagebox  
from tkinter import ttk
import matplotlib.pyplot as plt

carliber = {
    '5.56': {'dia': 5.7, 'mass': 3.56 / 1000, 'vel': 993},
    '5.45': {'dia': 5.6, 'mass': 3.43 / 1000, 'vel': 880},
    '7.62': {'dia': 7.82, 'mass': 10 / 1000, 'vel': 850},
    '7.92': {'dia': 8.22, 'mass': 11.7 / 1000, 'vel': 820},
    '9': {'dia': 9.01, 'mass': 7.45 / 1000, 'vel': 360},
    '.50': {'dia': 12.98, 'mass': 42 / 1000, 'vel': 928},
    '6.8': {'dia': 7, 'mass': 7.45 / 1000, 'vel': 785},
}
# For wind direction radio buttons
options = [('left', 1), ('right', 2)]

# Window Set Up
root = tk.Tk()
root.resizable(False, False)
root.title("Ballistic Calculator")
root.geometry('600x600')
tk.Label(root, text="Ballistic Calculator", font=("Helvetica Bold", 16)).pack(pady=10)
tk.Label(root, text="This calculates bullet drop, wind drift, and final velocity based on user input.", font=("Helvetica Bold", 13)).pack(pady=5)

restult_var = tk.StringVar(value="Result: —")
tk.Label(root, textvariable=restult_var, font=("Arial", 14)).pack(padx=10, pady=12)

tk.Label(root, text="Enter Target Distance (m)", font=("Helvetica", 10)).pack()
distance_entry = tk.Entry(root, font=("Helvetica", 14))
distance_entry.pack(pady=10, fill="x")
tk.Label(root, text="Enter Wind Speed (m/s)", font=("Helvetica", 10)).pack()
wind_speed_entry = tk.Entry(root, font=("Helvetica", 14))
wind_speed_entry.pack(pady=10, fill="x")

var = tk.IntVar()
var.set(1)  # default value

def calculate():
    try:
      distance = float(distance_entry.get())
      windSpeed = float(wind_speed_entry.get())
      if var.get() == 1:
          wind_direction = "to the left"
      else:
          wind_direction = "to the right"
      bulletType = combo.get()
      gravity = 9.81
      bulletVelocity = carliber[bulletType]['vel']
      bulletMass = carliber[bulletType]['mass']
      bulletDiameter = carliber[bulletType]['dia']

      # Formulae for calculation
      time = distance / bulletVelocity # Time of flight
      dropY = 0.5 * gravity * (time ** 2)  # Bullet Drop due to gravity
      Vy = gravity * time  # downward V after time
      Vfinal = math.sqrt((Vy ** 2) + (bulletVelocity ** 2))
      # Wind Drift
      drift = windSpeed * time
      # Air resistance
      radius_m = (bulletDiameter / 1000.0) / 2.0
      area = math.pi * (radius_m ** 2)
      rho = 1.225  # air density at sea level (kg/m^3)
      Cd = 0.295  # approximate drag coefficient for pointed bullets

      # initial drag force (at muzzle velocity) and corresponding acceleration magnitude
      DragF0 = 0.5 * rho * Cd * area * (bulletVelocity ** 2)
      aDrag = DragF0 / bulletMass

      # Simulate velocity over flight time, updating drag each timestep (drag scales with v^2)
      vNext = []
      time_steps = []
      deltaT = 0.01
      t = 0.0
      v = bulletVelocity
      while t <= time:
        # instantaneous drag force based on current speed
        DragF = 0.5 * rho * Cd * area * (v ** 2)
        a_inst = DragF / bulletMass
        v -= a_inst * deltaT
        if v < 0:
          v = 0.0
        vNext.append(v)
        time_steps.append(t)
        t += deltaT

      # final horizontal speed after drag simulation
      Vx_final_after_drag = vNext[-1] if vNext else bulletVelocity
      Vfinal_after_drag = math.sqrt((Vy ** 2) + (Vx_final_after_drag ** 2))

      restult_var.set(
          f"Bullet Drop: {dropY:f} m\n"
          f"Wind Drift: {drift:.2f} m {wind_direction}\n"
          f"Final Velocity (no drag): {Vfinal:.2f} m/s\n"
          f"Final Velocity (with drag): {Vfinal_after_drag:.2f} m/s\n"
          f"Initial Air Drag Acceleration (mag): {aDrag:g} m/s²"
      )
      
      plt.plot(time_steps, vNext, color = 'blue', label = f'{bulletType} Caliber')
      plt.xlabel('Time (s)')
      plt.ylabel("Velocity (m/s)")
      plt.title('Bullet Velocity Over Time with Air Drag')
      plt.grid()
      plt.legend()
      plt.show()
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numeric values for distance and wind speed.")
    
tk.Label(root, text="Enter Wind Direction (left/right)", font=("Helvetica", 10)).pack()
for text, value in options:
    tk.Radiobutton(root, text=text, variable=var, value=value, command= lambda: None,
                   font=("Helvetica", 10)).pack(anchor=tk.W)
    
tk.Label(root, text="Select Bullet Type", font=("Helvetica", 10)).pack(pady=5)
combo = ttk.Combobox(root, values=list(carliber.keys()), state="readonly")
combo.current(0)
combo.pack(pady=10, fill="x")

calculate_button = tk.Button(root, text="Calculate Ballistics", font=("Helvetica Bold", 14), command=calculate,
                             bg="#0B706A", fg="white", padx=10, pady=5)
calculate_button.pack(pady=20)

root.mainloop()