import argparse
import os
from csv_utils import parse_employee_list, parse_previous_assignments, write_assignments_to_csv
from classes.SecretSanta import SecretSanta

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Secret Santa Assignment Script",
        epilog="Example: python main.py -i ../data/employees.csv -c ../data/previous.csv -o ../output/output.csv"
    )

    parser.add_argument(
        "-i", "--input", required=True,
        help="CSV file containing the employee list"
    )
    parser.add_argument(
        "-c", "--constraint", required=True,
        help="CSV file containing previous year's assignments"
    )
    parser.add_argument(
        "-o", "--output", required=True,
        help="CSV file to save the new Secret Santa assignments"
    )

    return parser.parse_args()

def main():
    args = parse_arguments()

    # Validate input files exist
    if not os.path.isfile(args.input):
        print(f"Error: Employee file '{args.input}' not found.")
        return

    if not os.path.isfile(args.constraint):
        print(f"Error: Previous assignments file '{args.constraint}' not found.")
        return

    # Parse input data
    employees = parse_employee_list(args.input)
    previous_assignments = parse_previous_assignments(args.constraint)

    # Assign secret children
    santa = SecretSanta(employees, previous_assignments)
    try:
        assignments = santa.assign_secret_children()
        write_assignments_to_csv(assignments, args.output)
        print(f"Secret Santa assignments saved to {args.output}")
    except RuntimeError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
