# Knapsack problem solver
This is a simple project created in a rush (:P) for my Algorithms and Data Structures class at PUT University solving a knapsack problem using dynamic programming or brute-force method.
![Banner](https://github.com/suseldev/algorithms-playground-knapsack/blob/master/banner.png?raw=true)

## Usage
```bash
python3 main.py [--dynamic | --bruteforce ]
```
- `--dynamic` - solves the problem using dynamic programming method (efficient)
- `--bruteforce` - solves the problem using brute force search
### Input
You will be prompted to enter:
- the number of items,
- for each item: its value and weight,
- the knapsack capacity
## Testing
Run unit tests with `pytest`:
```bash
python3 -m pytest tests/
```
