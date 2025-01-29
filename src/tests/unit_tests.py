import unittest
from classes.Employee import Employee
from classes.SecretSanta import SecretSanta
import random

class TestEmployee(unittest.TestCase):

    def test_valid_employee(self):
        emp = Employee("Alice", "alice@example.com")
        self.assertEqual(emp.get_name(), "Alice")
        self.assertEqual(emp.get_email(), "alice@example.com")

    def test_invalid_email(self):
        """Ensure ValueError is raised for invalid email formats"""
        invalid_emails = ["alice@com", "bob@@example.com", "charlie.example.com", "user@.com"]
        for email in invalid_emails:
            with self.assertRaises(ValueError):
                Employee("Bob", email)

    def test_invalid_name_type(self):
        """Ensure TypeError is raised for non-string names"""
        with self.assertRaises(TypeError):
            Employee(123, "valid@example.com")

    def test_invalid_email_type(self):
        """Ensure TypeError is raised for non-string emails"""
        with self.assertRaises(TypeError):
            Employee("Alice", 12345)

    def test_employee_equality(self):
        """Employees with the same email should be equal"""
        emp1 = Employee("Alice", "alice@example.com")
        emp2 = Employee("Bob", "alice@example.com")  # Different name, same email
        self.assertEqual(emp1, emp2)

    def test_employee_inequality(self):
        """Employees with different emails should not be equal"""
        emp1 = Employee("Alice", "alice@example.com")
        emp2 = Employee("Bob", "bob@example.com")
        self.assertNotEqual(emp1, emp2)


class TestSecretSanta(unittest.TestCase):

    def setUp(self):
        """Set up a basic list of employees and previous assignments"""
        self.employees = [
            Employee("Alice", "alice@example.com"),
            Employee("Bob", "bob@example.com"),
            Employee("Charlie", "charlie@example.com"),
            Employee("David", "david@example.com"),
        ]
        self.previous_assignments = {
            "alice@example.com": "bob@example.com",
            "bob@example.com": "charlie@example.com",
            "charlie@example.com": "david@example.com",
            "david@example.com": "alice@example.com"
        }

    def test_valid_secret_santa_assignment(self):
        """Test if a valid assignment is generated"""
        secret_santa = SecretSanta(self.employees, self.previous_assignments)
        assignments = secret_santa.assign_secret_children()

        self.assertEqual(len(assignments), len(self.employees))  # Each employee gets one secret child

        assigned_emails = set()
        for giver, receiver in assignments.items():
            self.assertNotEqual(giver, receiver)  # No self-assignments
            self.assertNotIn(receiver.get_email(), assigned_emails)  # Each child is assigned only once
            assigned_emails.add(receiver.get_email())

    def test_no_repeated_assignments(self):
        """Ensure that employees are not assigned the same secret child as last year"""
        secret_santa = SecretSanta(self.employees, self.previous_assignments)
        assignments = secret_santa.assign_secret_children()

        for giver, receiver in assignments.items():
            self.assertNotEqual(self.previous_assignments.get(giver.get_email()), receiver.get_email())

    def test_edge_case_single_employee(self):
        """Test edge case where only one employee exists"""
        single_employee = [Employee("Eve", "eve@example.com")]
        secret_santa = SecretSanta(single_employee, {})

        with self.assertRaises(RuntimeError):
            secret_santa.assign_secret_children()  # Should fail since there's no one to assign

    def test_edge_case_two_employees(self):
        """Test with just two employees (they should swap assignments)"""
        two_employees = [
            Employee("Xavier", "xavier@example.com"),
            Employee("Yasmine", "yasmine@example.com")
        ]
        secret_santa = SecretSanta(two_employees, {})

        assignments = secret_santa.assign_secret_children()
        self.assertEqual(assignments[two_employees[0]], two_employees[1])
        self.assertEqual(assignments[two_employees[1]], two_employees[0])

    def test_stress_test_large_employee_list(self):
        """Test with a large number of employees (1000)"""
        large_employees = [Employee(f"Emp{i}", f"emp{i}@example.com") for i in range(1000)]
        secret_santa = SecretSanta(large_employees, {})

        assignments = secret_santa.assign_secret_children()
        self.assertEqual(len(assignments), len(large_employees))

        assigned_emails = set()
        for giver, receiver in assignments.items():
            self.assertNotEqual(giver, receiver)  # No self-assignments
            self.assertNotIn(receiver.get_email(), assigned_emails)  # Unique assignment check
            assigned_emails.add(receiver.get_email())

if __name__ == "__main__":
    unittest.main()
