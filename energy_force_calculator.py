import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Window Set Up
root = tk.Tk()
root.resizable(False, False)
root.title("Energy and Force Calculator")
root.geometry('440x600')

tk.Label(root, text="Energy and Force Calculator", font=("Helvetica Bold", 16)).pack(pady=10)
tk.Label(root, text="This calculates energy and force based on user input.", font=("Helvetica Bold", 13)).pack(pady=5)

result_var = tk.StringVar(value="Result: —")
tk.Label(root, textvariable=result_var, font=("Arial", 14)).pack(padx=10, pady=12)

# Frame that will hold the dynamic inputs for each calculation
content_frame = tk.Frame(root)
content_frame.pack(fill="both", expand=False, padx=10, pady=5)

def clear_frame():
  result_var.set("Result: —")
  for widget in content_frame.winfo_children():
    widget.destroy()

def potentialEnergy():
  clear_frame()
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
      gravity = 9.81
      energy = mass * height * gravity
      result_var.set(f"Potential Energy: {energy:.6g} J")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for mass and height.")

  calculate_btn = tk.Button(content_frame, text="Calculate", font=("Helvetica Bold", 14), command=calculate,
             bg="#0B706A", fg="white", padx=10, pady=5)
  calculate_btn.pack(pady=20)

def kineticEnergy():
  clear_frame()
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

  calculate_btn = tk.Button(content_frame, text="Calculate", font=("Helvetica Bold", 14), command=calculate,
             bg="#0B706A", fg="white", padx=10, pady=5)
  calculate_btn.pack(pady=20)
  
def secondLaw():
  clear_frame()
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

  calculate_btn = tk.Button(content_frame, text="Calculate", font=("Helvetica Bold", 14), command=calculate,
                       bg="#0B706A", fg="white", padx=10, pady=5)
  calculate_btn.pack(pady=20)

def gravitationalForce():
  clear_frame()
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
      gForce = 6.62 * (10 ** -11)
      force = gForce * ((mass_1 * mass_2) / radius ** 2)
      result_var.set(f"Force: {force:g} N")
    except ValueError:
      messagebox.showerror("Input Error", "Please enter valid numerical values for mass and radius.")

  calculate_btn = tk.Button(content_frame, text="Calculate", font=("Helvetica Bold", 14), command=calculate,
                       bg="#0B706A", fg="white", padx=10, pady=5)
  calculate_btn.pack(pady=20)

typeOfCalculation = {
  'Potential Energy' : potentialEnergy,
  'Kinetic Energy' : kineticEnergy,
  "Newton's Second Law" : secondLaw,
  'Gravitational Force' : gravitationalForce
}

tk.Label(root, text="Select Calculation Type", font=("Helvetica", 10)).pack()
calc_type_combo = ttk.Combobox(root, values=list(typeOfCalculation.keys()), state="readonly")
calc_type_combo.current(0)
calc_type_combo.bind("<<ComboboxSelected>>", lambda event: typeOfCalculation[calc_type_combo.get()]())
calc_type_combo.pack(pady=10, fill="x")

# show initial UI for the default selection
typeOfCalculation[calc_type_combo.get()]()

root.mainloop()
