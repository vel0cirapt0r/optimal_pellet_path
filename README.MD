# Optimal Pellet Path

This repository contains a Python solution to transform a given number of quantum antimatter fuel pellets into a single pellet using the fewest possible operations. The operations allowed are:
- Add 1 fuel pellet
- Remove 1 fuel pellet
- Divide the entire group of fuel pellets by 2 (only if the number of pellets is even)

## How It Works

The main function `answer(n)` takes a positive integer `n` as a string and returns the minimum number of operations needed to reduce `n` to 1. The function uses a recursive approach to explore all possible sequences of operations and determines the optimal path.

### Example

For example, starting with `n = 29`, the sequence of operations would be:
```
29 -> 28 -> 14 -> 7 -> 8 -> 4 -> 2 -> 1
```
This sequence uses 7 operations.

### Validation

The function also includes a validation function `validate_answer(n, provided_steps)` to verify if a provided sequence of steps matches the calculated optimal steps for transforming `n` to 1.

## Usage

To use the functions:
1. Import the functions `answer` and `validate_answer` from the `optimal_pellet_path` module.
2. Call `answer(n)` with a positive integer `n` represented as a string to get the sequence of steps.
3. Optionally, use `validate_answer(n, provided_steps)` to check if a provided sequence of steps matches the calculated steps.

### Example Usage

```python
from optimal_pellet_path import answer, validate_answer

n = "29"
steps = answer(n)
print("Steps:", steps)

provided_steps = [29, 28, 14, 7, 8, 4, 2, 1]
print("Validation:", validate_answer(n, provided_steps))
```

## Installation

Clone the repository and import the `optimal_pellet_path` module to start using the functions.

```bash
git clone https://github.com/vel0cirapt0r/optimal_pellet_path.git
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
