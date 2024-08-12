# Python Object Oriented Programming by Joe Marini course example
# Creating immutable data classes

from dataclasses import dataclass

# very useful for class which argument won't change, you can only set arguments when construction class, but it cannot be change later
@dataclass(frozen=True)  # TODO: "The "frozen" parameter makes the class immutable
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def some_func(self, newval):
        self.value2 = newval


obj = ImmutableClass("Another String", 20)
print(obj.value1)

# TODO: attempting to change the value of an immutable class throws an exception
# obj.value1 = "Another string"

# TODO: even functions within the class can't change anything
# obj.some_func(20)