# Example file for Advanced Python: Language Features by Joe Marini
# Use special methods to compare objects to each other


# Define a class to represent an employee
class Employee:
    def __init__(self, fname, lname, level, years_service):
        # Initialize the employee's first name, last name, job level, and years of service
        self.fname = fname
        self.lname = lname
        self.level = level
        self.seniority = years_service

    # Define "greater than or equal to" comparison based on level, then seniority
    def __ge__(self, other):
        if self.level == other.level:
            return self.seniority >= other.seniority
        return self.level >= other.level

    # Define "greater than" comparison based on level, then seniority
    def __gt__(self, other):
        if self.level == other.level:
            return self.seniority > other.seniority
        return self.level > other.level

    # Define "less than" comparison based on level, then seniority
    def __lt__(self, other):
        if self.level == other.level:
            return self.seniority < other.seniority
        return self.level < other.level

    # Define "less than or equal to" comparison based on level, then seniority
    def __le__(self, other):
        if self.level == other.level:
            return self.seniority <= other.seniority
        return self.level <= other.level

    # Define "equal to" comparison based only on level (not seniority)
    def __eq__(self, other):
        return self.level == other.level


# Create a list to hold employee objects
dept = []

# Add some employees to the department list
dept.append(Employee("Tim", "Sims", 5, 9))  # Index 0
dept.append(Employee("John", "Doe", 4, 12))  # Index 1
dept.append(Employee("Jane", "Smith", 6, 6))  # Index 2
dept.append(Employee("Rebecca", "Robinson", 5, 13))  # Index 3
dept.append(Employee("Tyler", "Durden", 5, 12))  # Index 4

# Compare two employees using the custom "greater than" operator
# Tim (5,9) > Jane (6,6) => False because 5 < 6
print(bool(dept[0] > dept[2]))

# Compare two employees using the custom "less than" operator
# Tyler (5,12) < Rebecca (5,13) => True because same level, but 12 < 13
print(bool(dept[4] < dept[3]))

# Sort the employees using the custom comparison logic
# Sorting by level first, then by years of service
emps = sorted(dept)

# Print last names of sorted employees
for emp in emps:
    print(emp.lname)
