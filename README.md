# Bacterial Competition Growth Simulator
![bacedgespng](https://user-images.githubusercontent.com/63346219/189453169-be416bf5-8d8b-4c07-87b0-6209c54f5107.png)


A Python program to simulate the competition between two bacterial species, inspired by the research study on E. Coli bacteria growth patterns. The model treats bacteria as self-avoiding random walkers on a grid, illustrating the competition for space.

**Research Paper:** [Link](https://arxiv.org/pdf/0912.2241.pdf)

## Code Structure
- `Walker` class: Represents bacteria as self-avoiding random walkers on a grid.
- `main` function: Controls the simulation and the animation.

## Dependencies
- matplotlib
- numpy
- typer

## Running the Simulation
```bash
python3 script_name.py --gridsize 100
```

