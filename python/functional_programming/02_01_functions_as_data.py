from collections.abc import Callable
from typing import TypedDict

""" TypedDict is a
 simple typed namespace. At runtime it is equivalent to a plain dict.
TypedDict creates a dictionary type such that a type checker will expect all
instances to have a certain set of keys, where each key is
associated with a value of a consistent type. This expectation
is not checked at runtime. """


# 1. Simple function aliasing
def say_hello(name: str) -> None:
    print(f"Hello {name}")


say_hello_2: Callable[[str], None] = say_hello
say_hello_2("Johnny")


# 2. Typed dict for fake data structure
class PersonData(TypedDict):
    name: str
    age: int


# 3. Environment setting
ENVIRONMENT: str = "prod"


# 4. Real data fetch (side-effect only)
def fetch_data_real() -> None:
    print("Doing some very time intensive operations...")


# 5. Fake data fetch (returns mock)
def fetch_data_fake() -> PersonData:
    print("Returning fake data")
    return {"name": "Jane Doe", "age": 34}


# 6. Conditional function assignment
fetch_data: Callable[[], None | PersonData] = (
    fetch_data_real if ENVIRONMENT == "prod" else fetch_data_fake
)

# 7. Call the selected function
data = fetch_data()
