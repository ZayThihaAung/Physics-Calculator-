# Physics Calculator

[![GitHub stars](https://img.shields.io/github/stars/ZayThihaAung/Physics-Calculator-.svg?style=social)](https://github.com/ZayThihaAung/Physics-Calculator-/stargazers)
[![Build Status](https://github.com/ZayThihaAung/Physics-Calculator-/actions/workflows/python-package.yml/badge.svg)](https://github.com/ZayThihaAung/Physics-Calculator-/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Python](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)

A small, easy-to-use set of physics calculation utilities aimed at students and teachers. These programs help students quickly compute common physics problems (kinematics, energy, forces, circuits, optics). The project is lightweight, well-documented, and designed to be a teaching aid.

Why this repo?
- Simple API and command-line examples for common physics formulas
- Ready-to-run examples for classroom demonstrations
- Suitable for learning and quick verification of homework/assignments

Demo
![demo placeholder](docs/assets/demo.gif)  
(Replace with a short GIF or image showing the calculator in action.)

Features
- Kinematics: displacement, velocity, acceleration
- Energy and work: kinetic/potential energy computations
- Forces: net force, friction computations
- Circuits: simple resistance and Ohm's law helpers
- Unit-aware outputs (planned — see roadmap)

Quick start

1. Clone
```
git clone https://github.com/ZayThihaAung/Physics-Calculator-.git
cd Physics-Calculator-
```

2. Install (if packaged)
```
pip install physics-calculator
```
or run the example directly:
```
python examples/simple_usage.py
```

Example usage (Python)
```py
from physics_calculator import kinematics

# compute final velocity given u, a, t
v = kinematics.final_velocity(u=0, a=9.81, t=2)
print(f"Final velocity: {v:.2f} m/s")
```

CLI (example)
```
# future: python -m physics_calculator kinematics --u 0 --a 9.81 --t 2
```

Installation & development
```
python -m venv .venv
source .venv/bin/activate      # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
pip install -e .
pytest
```

Contributing
Contributions are very welcome! Please read [CONTRIBUTING.md](CONTRIBUTING.md) for how to file issues and PRs.

Roadmap (short)
- Add unit support (pint)
- Published package on PyPI
- Interactive web demo (GitHub Pages)
- More worked examples for each topic

Support / License
MIT — see [LICENSE](LICENSE).

Useful links
- Issues: https://github.com/ZayThihaAung/Physics-Calculator-/issues
- Pull requests: https://github.com/ZayThihaAung/Physics-Calculator-/pulls
