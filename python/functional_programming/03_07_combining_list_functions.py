from functools import reduce
from typing import TypedDict


# Define a TypedDict to represent the structure of an employee dictionary
class Employee(TypedDict):
    name: str
    salary: int
    job_title: str


# list of employee dictionaries
employees: list[Employee] = [
    {"name": "Jane", "salary": 90000, "job_title": "developer"},
    {"name": "Bill", "salary": 50000, "job_title": "writer"},
    {"name": "Kathy", "salary": 120000, "job_title": "executive"},
    {"name": "Anna", "salary": 100000, "job_title": "developer"},
    {"name": "Dennis", "salary": 95000, "job_title": "developer"},
    {"name": "Albert", "salary": 70000, "job_title": "marketing specialist"},
]


# Function to check if an employee is a developer
def is_developer(employee: Employee) -> bool:
    return employee["job_title"] == "developer"


# Function to check if an employee is NOT a developer
def is_not_developer(employee: Employee) -> bool:
    return employee["job_title"] != "developer"


# Filter out developers and non-developers from the list
developers: list[Employee] = list(filter(is_developer, employees))
non_developers: list[Employee] = list(filter(is_not_developer, employees))


# Function to extract the salary from an employee record
def get_salary(employee: Employee) -> int:
    return employee["salary"]


# Use map to extract a list of salaries from both groups
developer_salaries: list[int] = list(map(get_salary, developers))
non_developer_salaries: list[int] = list(map(get_salary, non_developers))


# Function to sum two numbers – used with reduce
def get_sum(acc: int, x: int) -> int:
    return acc + x


# Reduce developer salaries list to get the total sum
total_developer_salaries: int = reduce(get_sum, developer_salaries)

# Divide by count to get average developer salary
average_developer_salary: float = total_developer_salaries / len(developer_salaries)

# Do the same for non-developer salaries
total_non_developer_salaries: int = reduce(get_sum, non_developer_salaries)
average_non_developer_salary: float = total_non_developer_salaries / len(
    non_developer_salaries
)

# Print the average salaries
print(average_developer_salary)
print(average_non_developer_salary)
