from collections.abc import Iterator, Callable


# Basic function with input and output type annotations
def square(number: int) -> int:
    return number * number


# Function with multiple typed arguments
def multiply(a: float, b: float) -> float:
    return a * b


# Function with a default argument and no return value
def greet(name: str, excitement: int = 3) -> None:
    print(f"Hello, {name}" + "!" * excitement)


# Function without any type annotations (discouraged)
def untyped_function(x):
    return x + 1  # No static type checking


# Callable type: function that takes int and float, returns float
def add_and_scale(a: int, scale: float) -> float:
    return a * scale


operation: Callable[[int, float], float] = add_and_scale
print(operation(3, 2.5))  # 7.5


# Register a callback function that takes a string and returns an int
def length_of_string(s: str) -> int:
    return len(s)


def register_callback(callback: Callable[[str], int]) -> None:
    result = callback("Hello!")
    print(f"Callback returned: {result}")


register_callback(length_of_string)


# Generator function that yields integers
def countdown(start: int) -> Iterator[int]:
    while start > 0:
        yield start
        start -= 1


for num in countdown(3):
    print(num)


# Function with complex parameter types and defaults
def send_email(
    to: str | list[str],
    sender: str,
    cc: list[str] | None = None,
    bcc: list[str] | None = None,
    subject: str = "No Subject",
    body: list[str] | None = None,
) -> bool:
    print(f"Sending email to: {to}")
    return True


# Function with positional-only and keyword-only arguments
def log_event(event_type: str, /, *, timestamp: str) -> None:
    print(f"[{timestamp}] Event: {event_type}")


log_event("ERROR", timestamp="2025-05-31")
# log_event("ERROR", "2025-05-31")  # ❌ Too many positional arguments
# log_event(event_type="ERROR", timestamp="2025-05-31")  # ❌ 'event_type' is positional-only


# Function with *args and **kwargs
def make_request(endpoint: str, *args: str, **options: str) -> str:
    print(f"Args: {args}")
    print(f"Options: {options}")
    return f"Request to {endpoint} with {args} and options {options}"


make_request("/api/data", "param1", "param2", timeout="30", retries="3")
