import csv
from classes.Employee import Employee

def parse_employee_list(file_path):
    employees = []
    try:
        with open(file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                employees.append(Employee(row['Employee_Name'], row['Employee_EmailID']))
    except Exception as e:
        raise RuntimeError(f"Error reading employee list: {e}")
    return employees

def parse_previous_assignments(file_path):
    previous_assignments = {}
    try:
        with open(file_path, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                previous_assignments[row['Employee_EmailID']] = row['Secret_Child_EmailID']
    except Exception as e:
        raise RuntimeError(f"Error reading previous assignments: {e}")
    return previous_assignments

def write_assignments_to_csv(assignments, output_file):
    try:
        with open(output_file, "w", newline="") as csvfile:
            fieldnames = ['Employee_Name', 'Employee_EmailID', 'Secret_Child_Name', 'Secret_Child_EmailID']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for emp, child in assignments.items():
                writer.writerow({
                    'Employee_Name': emp.get_name(),
                    'Employee_EmailID': emp.get_email(),
                    'Secret_Child_Name': child.get_name(),
                    'Secret_Child_EmailID': child.get_email()
                })
    except Exception as e:
        raise RuntimeError(f"Error writing assignments to CSV: {e}")
