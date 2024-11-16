from typing import Final
from datetime import datetime

VERSION: Final[str] = '1.0.12'
PI: Final[float] = 3.1415

# How to use function
def show_date() -> None:
    print('This is th current time:')
    print(datetime.now())

show_date()

def greet(name: str) -> None:
    print(f'Hello, {name}!')

greet('Sharil')
greet('Nuha')

def add(a: float, b: float) -> float:
    return a + b

print(add(2.3, 1.8))