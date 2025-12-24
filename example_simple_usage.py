# Example usage for Physics-Calculator
# (Adapt to your package API)

def final_velocity(u: float, a: float, t: float) -> float:
    """v = u + a*t"""
    return u + a * t

if __name__ == "__main__":
    u = 0.0
    a = 9.81
    t = 2.0
    v = final_velocity(u, a, t)
    print(f"Initial velocity: {u} m/s")
    print(f"Acceleration: {a} m/s^2")
    print(f"Time: {t} s")
    print(f"Final velocity: {v:.2f} m/s")
