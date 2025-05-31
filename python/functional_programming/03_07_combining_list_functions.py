from functools import reduce
from typing import TypedDict


class Employee(TypedDict):
    name: str
    salary: int
    job_title: str


employees: list[Employee] = [
    {"name": "Jane", "salary": 90000, "job_title": "developer"},
    {"name": "Bill", "salary": 50000, "job_title": "writer"},
    {"name": "Kathy", "salary": 120000, "job_title": "executive"},
    {"name": "Anna", "salary": 100000, "job_title": "developer"},
    {"name": "Dennis", "salary": 95000, "job_title": "developer"},
    {"name": "Albert", "salary": 70000, "job_title": "marketing specialist"},
]


def is_developer(employee: Employee) -> bool:
    return employee["job_title"] == "developer"


def is_not_developer(employee: Employee) -> bool:
    return employee["job_title"] != "developer"


def get_salary(employee: Employee) -> int:
    return employee["salary"]


developer_salaries: list[int] = [get_salary(x) for x in employees if is_developer(x)]
non_developer_salaries: list[int] = [
    get_salary(x) for x in employees if is_not_developer(x)
]


def get_sum(acc: int, x: int) -> int:
    return acc + x


total_developer_salaries: int = reduce(get_sum, developer_salaries)
average_developer_salary: float = total_developer_salaries / len(developer_salaries)

total_non_developer_salaries: int = reduce(get_sum, non_developer_salaries)
average_non_developer_salary: float = total_non_developer_salaries / len(
    non_developer_salaries
)

print(average_developer_salary)
print(average_non_developer_salary)
