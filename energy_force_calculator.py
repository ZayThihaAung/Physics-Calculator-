import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Window Set Up
root = tk.Tk()
root.resizable(False, False)
root.title("Energy and Force Calculator")
root.geometry('440x620')

tk.Label(root, text="Energy and Force Calculator", font=("Helvetica Bold", 16)).pack(pady=10)
tk.Label(root, text="This calculates energy and force based on user input.", font=("Helvetica Bold", 13)).pack(pady=5)

result_var = tk.StringVar(value="Result: —")
tk.Label(root, textvariable=result_var, font=("Arial", 14)).pack(padx=10, pady=12)

# Frame that will hold the dynamic inputs for each calculation
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=False, padx=10, pady=5)
GRAVITY = 9.81  # Acceleration due to gravity (m/s²)
AIRDENSITY = 1.225  # Density of air at sea level (kg/m³)
LIGHTSPEED = 3 * (10 ** 8)  # Speed of light in vacuum (m/s)
GFORCE = 6.62 * (10 ** -11)

def clear_frame():
  result_var.set("Result: —")
  for widget in content_frame.winfo_children():
    widget.destroy()

def calculateBtn(calculate):
  calculate_btn = tk.Button(content_frame, text="Calculate", font=("Helvetica Bold", 14), command=calculate,
             bg="#0B706A", fg="white", padx=10, pady=5)
  calculate_btn.pack(pady=20)

def potentialEnergy():
  clear_frame()
  tk.Label(content_frame, text="Formula: PE = mgh", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter the object's mass (kg)", font=("Helvetica", 10)).pack()
  mass_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  mass_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the height (m)", font=("Helvetica", 10)).pack()
  height_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  height_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      mass = float(mass_entry.get().strip())
      height = float(height_entry.get().strip())
      if mass < 0 or height < 0:
        messagebox.showerror("Input Error", "Mass and height cannot be negative.")
        return
      energy = mass * height * GRAVITY
      result_var.set(f"Potential Energy: {energy:.6g} J")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for mass and height.")
  calculateBtn(calculate)

def kineticEnergy():
  clear_frame()
  tk.Label(content_frame, text="Formula: KE = (1/2)mv²", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter the object's mass (kg)", font=("Helvetica", 10)).pack()
  mass_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  mass_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the velocity (m/s)", font=("Helvetica", 10)).pack()
  velocity_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  velocity_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      mass = float(mass_entry.get().strip())
      velocity = float(velocity_entry.get().strip())
      if mass < 0 or velocity < 0:
        messagebox.showerror("Input Error", "Mass and velocity cannot be negative.")
        return
      energy = (mass * velocity ** 2) / 2
      result_var.set(f"Kinetic Energy: {energy:.6g} J")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for mass and velocity.")
  calculateBtn(calculate)

def elasticEnergy():
  clear_frame()
  tk.Label(content_frame, text="Formula: EPE = (1/2)kx²", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter the spring constant (N/m)", font=("Helvetica", 10)).pack()
  spring_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  spring_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the displacement (m)", font=("Helvetica", 10)).pack()
  displacement_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  displacement_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      spring_constant = float(spring_entry.get().strip())
      displacement = float(displacement_entry.get().strip())
      if spring_constant < 0 or displacement < 0:
        messagebox.showerror("Input Error", "Spring constant and displacement cannot be negative.")
        return
      energy = (spring_constant * displacement ** 2) / 2
      result_var.set(f"Elastic Potential Energy: {energy:.6g} J")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for spring constant and displacement.")
  calculateBtn(calculate)

def thermalEnergy():
  clear_frame()
  tk.Label(content_frame, text="Formula: Q = mcΔT", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter the mass (kg)", font=("Helvetica", 10)).pack()
  mass_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  mass_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the initial temperature (K)", font=("Helvetica", 10)).pack()
  temp_entry1 = tk.Entry(content_frame, font=("Helvetica", 14))
  temp_entry1.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the final temperature (K)", font=("Helvetica", 10)).pack()
  temp_entry2 = tk.Entry(content_frame, font=("Helvetica", 14))
  temp_entry2.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the specific heat capacity (J/kg·K)", font=("Helvetica", 8)).pack(pady=5)
  specific_heat_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  specific_heat_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      mass = float(mass_entry.get().strip())
      temp1 = float(temp_entry1.get().strip())
      temp2 = float(temp_entry2.get().strip())
      specific_heat = float(specific_heat_entry.get().strip())
      if mass < 0 or temp1 < 0 or temp2 < 0 or specific_heat < 0:
        messagebox.showerror("Input Error", "All values cannot be negative.")
        return
      energy = mass * specific_heat * (temp2 - temp1)
      result_var.set(f"Thermal Energy: {energy:.6g} J")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for mass and temperature.")
  calculateBtn(calculate)

def electricalEnergy():
  clear_frame()
  tk.Label(content_frame, text="Formula: E = IVt", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter the Voltage (V)", font=("Helvetica", 10)).pack()
  current_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  current_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the current (A)", font=("Helvetica", 10)).pack()
  voltage_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  voltage_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the time (s)", font=("Helvetica", 10)).pack()
  time_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  time_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      current = float(current_entry.get().strip())
      voltage = float(voltage_entry.get().strip())
      time = float(time_entry.get().strip())
      if current < 0 or voltage < 0 or time < 0:
        messagebox.showerror("Input Error", "Current, voltage, and time cannot be negative.")
        return
      energy = current * voltage * time
      result_var.set(f"Electrical Energy: {energy:.6g} J")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for current, voltage, and time.")
  calculateBtn(calculate)

def relativeEnergy():
  clear_frame()
  tk.Label(content_frame, text="Formula: E = mc²", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter the object's mass (kg)", font=("Helvetica", 10)).pack()
  mass_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  mass_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      mass = float(mass_entry.get().strip())
      if mass < 0:
        messagebox.showerror("Input Error", "Mass cannot be negative.")
        return
      energy = mass * LIGHTSPEED ** 2
      result_var.set(f"Relative Energy: {energy:.6g} J")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter a valid numerical value for mass.")
  calculateBtn(calculate)

def orbitalEnergy():
  clear_frame()
  tk.Label(content_frame, text="Formula: E = -G(m1*m2)/r", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter the object's mass (kg)", font=("Helvetica", 10)).pack()
  mass_entry1 = tk.Entry(content_frame, font=("Helvetica", 14))
  mass_entry1.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the central body's mass (kg)", font=("Helvetica", 10)).pack()
  mass_entry2 = tk.Entry(content_frame, font=("Helvetica", 14))
  mass_entry2.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the orbital radius (m)", font=("Helvetica", 10)).pack()
  radius_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  radius_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      mass1 = float(mass_entry1.get().strip())
      mass2 = float(mass_entry2.get().strip())
      radius = float(radius_entry.get().strip())
      if mass1 < 0 or mass2 < 0 or radius <= 0:
        messagebox.showerror("Input Error", "Masses cannot be negative and radius must be positive.")
        return
      energy = -GFORCE * (mass1 * mass2) / radius
      result_var.set(f"Orbital Energy: {energy:.6g} J")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for masses and radius.")
  calculateBtn(calculate)

def secondLaw():
  clear_frame()
  tk.Label(content_frame, text="Formula: F = ma", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter mass (kg)", font=("Helvetica", 10)).pack()
  mass_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  mass_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter acceleration (m/s²)", font=("Helvetica", 10)).pack()
  acceleration_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  acceleration_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      mass = float(mass_entry.get().strip())
      acceleration = float(acceleration_entry.get().strip())
      if mass < 0 or acceleration < 0:
        messagebox.showerror("Input Error", "Mass and acceleration cannot be negative.")
        return
      force = mass * acceleration
      result_var.set(f"Force: {force:.6g} N")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for mass and acceleration.")
  calculateBtn(calculate)

def gravitationalForce():
  clear_frame()
  tk.Label(content_frame, text="Formula: F = G(m1*m2)/r²", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter mass of first object (kg)", font=("Helvetica", 10)).pack()
  mass1_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  mass1_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter mass of second object (kg)", font=("Helvetica", 10)).pack()
  mass2_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  mass2_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the distance(radius) between two object (m)", font=("Helvetica", 10)).pack()
  radius_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  radius_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      mass_1 = float(mass1_entry.get().strip())
      mass_2 = float(mass2_entry.get().strip())
      radius = float(radius_entry.get().strip())
      if mass_1 < 0 or mass_2 < 0 or radius < 0:
        messagebox.showerror("Input Error", "Masses and radius cannot be negative.")
        return
      force = GFORCE * ((mass_1 * mass_2) / radius ** 2)
      result_var.set(f"Force: {force:g} N")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for mass and radius.")
  calculateBtn(calculate)

def centripetalForce(): # F = (m * v^2) / r
  clear_frame()
  tk.Label(content_frame, text="Formula: F = (m * v²) / r", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter mass (kg)", font=("Helvetica", 10)).pack()
  mass_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  mass_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter velocity (m/s)", font=("Helvetica", 10)).pack()
  velocity_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  velocity_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter radius (m)", font=("Helvetica", 10)).pack()
  radius_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  radius_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      mass = float(mass_entry.get().strip())
      velocity = float(velocity_entry.get().strip())
      radius = float(radius_entry.get().strip())
      if mass < 0 or velocity < 0 or radius <= 0:
        messagebox.showerror("Input Error", "Mass, velocity, and radius must be positive.")
        return
      force = (mass * velocity ** 2) / radius
      result_var.set(f"Force: {force:.6g} N")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")
  calculateBtn(calculate)

def frictionalForce():
  clear_frame()
  tk.Label(content_frame, text="Formula: F = μN", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter the coefficient of friction", font=("Helvetica", 10)).pack()
  coefficient_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  coefficient_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the mass (kg)", font=("Helvetica", 10)).pack()
  mass_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  mass_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      coefficient = float(coefficient_entry.get().strip())
      mass = float(mass_entry.get().strip())
      if coefficient < 0 or mass < 0:
        messagebox.showerror("Input Error", "Coefficient of friction and mass cannot be negative.")
        return
      frictionForce = coefficient * mass * GRAVITY
      result_var.set(f"Frictional Force: {frictionForce:.6g} N")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")
  calculateBtn(calculate)

def dragForce():
  clear_frame()
  tk.Label(content_frame, text="Formula: FD = (1/2) * CD * ρ * v² * A", font=("Helvetica", 10)).pack(pady=5)
  tk.Label(content_frame, text="Enter the drag coefficient", font=("Helvetica", 10)).pack()
  drag_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  drag_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the velocity (m/s)", font=("Helvetica", 10)).pack()
  velocity_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  velocity_entry.pack(pady=10, fill="x")
  tk.Label(content_frame, text="Enter the reference area (m²)", font=("Helvetica", 10)).pack()
  area_entry = tk.Entry(content_frame, font=("Helvetica", 14))
  area_entry.pack(pady=10, fill="x")

  def calculate():
    try:
      drag = float(drag_entry.get().strip())
      density = AIRDENSITY
      velocity = float(velocity_entry.get().strip())
      area = float(area_entry.get().strip())
      if drag < 0 or density < 0 or velocity < 0 or area <= 0:
        messagebox.showerror("Input Error", "All values must be positive.")
        return
      dragForce = 0.5 * drag * density * velocity ** 2 * area
      result_var.set(f"Drag Force: {dragForce:.6g} N")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for all fields.")
  calculateBtn(calculate)

typeOfCalculation = {
  'Potential Energy' : potentialEnergy,
  'Kinetic Energy' : kineticEnergy,
  'Elastic Potential Energy' : elasticEnergy,
  'Thermal Energy' : thermalEnergy,
  'Electrical Energy' : electricalEnergy,
  'Relative Energy' : relativeEnergy,
  'Orbital Energy' : orbitalEnergy,
  "Newton's Second Law" : secondLaw,
  'Gravitational Force' : gravitationalForce,
  'Centripetal Force' : centripetalForce,
  'Frictional Force' : frictionalForce,
  "Air Resistance Force" : dragForce
}

tk.Label(root, text="Select Calculation Type", font=("Helvetica", 10)).pack()
calc_type_combo = ttk.Combobox(root, values=list(typeOfCalculation.keys()), state="readonly")
calc_type_combo.current(0)
calc_type_combo.bind("<<ComboboxSelected>>", lambda event: typeOfCalculation[calc_type_combo.get()]())
calc_type_combo.pack(pady=10, fill="x")

# show initial UI for the default selection
typeOfCalculation[calc_type_combo.get()]()

root.mainloop()
