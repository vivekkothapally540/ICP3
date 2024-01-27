class Employee:
    """
    Represents an employee with basic information and salary.
    """

    # Class attribute to track total employees
    total_employees = 0

    def __init__(self, name, family, salary, department):
        """
        Initializes an Employee object with the given attributes.
        """
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.total_employees += 1

    def calculate_average_salary(self, employees):
        """
        Calculates the average salary of a list of employees.
        """
        total_salary = sum(employee.salary for employee in employees)
        return total_salary / len(employees)

    @classmethod
    def get_total_employees(cls):
        """
        Returns the total number of employees created.
        """
        return cls.total_employees

class FulltimeEmployee(Employee):
    """
    Represents a full-time employee inheriting from Employee and adding benefits.
    """

    def __init__(self, name, family, salary, department, benefits):
        """
        Initializes a FulltimeEmployee object with additional benefits.
        """
        super().__init__(name, family, salary, department)
        self.benefits = benefits

# Example usage
employee1 = Employee("Vivek", "Kothapally", 50000, "Marketing")
employee2 = Employee("Jyothi", "Perla", 60000, "Technical")
employee3 = FulltimeEmployee("Smruthi", "Siddemsetty", 70000, "Finance", ["Health insurance", "Dental insurance"])

# Accessing attributes and methods
print(f"Total employees: {Employee.get_total_employees()}")
print(f"Average salary: ${employee1.calculate_average_salary([employee1, employee2, employee3])}")
print(f"{employee3.name}'s benefits: {employee3.benefits}")
