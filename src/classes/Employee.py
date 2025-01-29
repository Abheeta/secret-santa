import re

class Employee:

    def __init__(self, name="", email=""):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not isinstance(email, str):
            raise TypeError("Email must be a string")

        EMAIL_REGEX = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

        def is_valid_email(email):
            return re.match(EMAIL_REGEX, email) is not None

        if not is_valid_email(email):
            raise ValueError(f"Invalid email format: {email}")

        self.__name = name
        self.__email = email

    # Getter for name
    def get_name(self):
        return self.__name

    # Getter for email
    def get_email(self):
        return self.__email

    def __str__(self):
        """Returns a string representation of the Employee object."""
        return f"Employee(Name: {self.__name}, Email: {self.__email})"

    def __eq__(self, other):
        """Compare employees based on their email."""
        return isinstance(other, Employee) and self.__email == other.__email
    
    def __hash__(self):
        return hash(self.__email)
