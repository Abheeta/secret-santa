import random

class SecretSanta:
    def __init__(self, employees, previous_assignments):
        self.employees = employees
        self.previous_assignments = previous_assignments
        self.assignments = {}

    def build_graph(self):
        """
        Create a graph where each employee is connected to possible secret children
        based on the constraints.
        """
        graph = {}

        for employee in self.employees:
            possible_children = [
                child for child in self.employees
                if child != employee and self.previous_assignments.get(employee.get_email()) != child.get_email()
            ]

            random.shuffle(possible_children)  # Randomize to reduce bias
            graph[employee] = possible_children

        return graph

    def assign_secret_children(self):
        """
        Assign secret children using an **iterative** backtracking approach, with safeguards to prevent infinite loops.
        """
        graph = self.build_graph()
        assigned_children = {}
        used_children = set()
        stack = []  # Stack for iterative backtracking
        failed_attempts = {employee: set() for employee in self.employees}  # Track failed assignments

        employee_index = 0
        while employee_index < len(self.employees):
            employee = self.employees[employee_index]

            # If this employee was previously assigned, backtrack
            if employee in assigned_children:
                used_children.remove(assigned_children[employee])  # Free the child
                failed_attempts[employee].add(assigned_children[employee])  # Mark this child as failed
                del assigned_children[employee]

            # Get available children excluding those that already failed
            possible_children = [
                child for child in graph[employee] if child not in used_children and child not in failed_attempts[employee]
            ]

            if possible_children:
                # Assign the first valid child
                secret_child = possible_children.pop()
                assigned_children[employee] = secret_child
                used_children.add(secret_child)
                stack.append((employee, secret_child))  # Save to stack
                employee_index += 1  # Move to next employee
            else:
                # No valid assignments left for this employee -> backtrack
                if not stack:
                    raise RuntimeError("Failed to create valid assignments due to constraints.")

                # Backtrack: undo last assignment and retry
                prev_employee, prev_child = stack.pop()
                del assigned_children[prev_employee]
                used_children.remove(prev_child)
                failed_attempts[prev_employee].add(prev_child)  # Mark this child as failed
                employee_index -= 1  # Go back to previous employee

        return assigned_children
