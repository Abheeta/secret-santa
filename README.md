# Secret Santa Assignment Script

## Overview

The Secret Santa Script automates the process of assigning Secret Children (gift recipients) to employees based on provided employee and previous year's assignment data. It ensures that employees do not assign themselves or repeat previous assignments.

This Python script allows you to:
- Input a list of employees with their details.
- Avoid previous year's assignments by referencing a CSV of last year's pairings.
- Output new Secret Santa assignments into a CSV file.

## Features
- **Input Files**: Read employee list and previous year's assignments from CSV files.
- **Backtracking**: The algorithm ensures valid assignments by adhering to constraints like no self-assignments and avoiding previous year’s pairings.
- **Output File**: Generates a new CSV with employees and their assigned Secret Children.
- **Flexible CLI Arguments**: Allows specifying input, output, and constraint files via command-line arguments.

## Requirements

- Python 3.x
- `argparse` module (standard Python library)

## Setup

### 1. Clone the repository and install dependencies (if applicable)

```bash
git clone <repository_url>
cd secret-santa-assignment/src
pip install -r requirements.txt
```

### 2. Run the script with the necessary arguments.

#### The following options are available:

- `-i` or `--input`: Path to the employee CSV file.
- `-c` or `--constraint`: Path to the previous year’s assignment CSV file.
- `-o` or `--output`: Path to the output CSV file where the assignments will be saved.

#### Example usage:

```bash
python main.py -i ../data/employees.csv -c ../data/previous.csv -o ../output/output.csv
```

#### Help:

To view the help screen for command-line options:

```bash
python main.py -h
```

## File Structure

- `main.py`: The main script that handles the Secret Santa logic.
- `csv_utils.py`: Utility functions for reading and writing CSV files.
- `classes/`: Contains the Employee and SecretSanta classes for the logic.
- `requirements.txt`: The list of required Python dependencies.
- `README.md`: Documentation for the project.

## How It Works

1. **Employee Data**: The script reads a CSV file that contains employee names and email addresses.
2. **Previous Assignments**: The script checks previous Secret Santa assignments to ensure no employee is assigned to the same person two years in a row.
3. **Secret Santa Assignment**: Using a backtracking algorithm, the script ensures each employee is assigned a unique "secret child" while adhering to the given constraints.
4. **Output**: The final assignments are saved to a new CSV file.

## Testing

You can run tests using `unittest` to verify the functionality:

```bash
python -m unittest ./tests/unit_tests.py
```
