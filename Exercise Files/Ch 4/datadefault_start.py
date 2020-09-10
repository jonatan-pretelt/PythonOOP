# Python Object Oriented Programming by Joe Marini course example
# implementing default values in data classes

from dataclasses import dataclass, field


@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str  = "No Title"
    author: str = "No Author"
    pages: int  = 0
    price: float = field(default=10.0)


b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)

print(b1)
print(b2)