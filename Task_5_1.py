#Task_1#
def caching_fibonacci():
    cache = {}
    
    def fibonacci(n):
        if n in cache:
            return cache[n]
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        else:
            result = fibonacci(n-1) + fibonacci(n-2)
            cache[n] = result
            return result
    
    return fibonacci

#Task_2#
import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    pattern = r'\b\d+(\.\d+)?\b'
    matches = re.findall(pattern, text)
    for match in matches:
        yield float(match)

def sum_profit(text: str, func: Callable[[str], Generator[float, None, None]]) -> float:
    return sum(func(text))

#Task_3#
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Give me name and phone please."
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} added with phone {phone}."

def main():
    contacts = {}
    while True:
        user_input = input("Enter command: ").strip()
        if user_input == "exit":
            print("Goodbye!")
            break
        command, *args = user_input.split()
        if command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(get_contact(args, contacts))
        elif command == "delete":
            print(delete_contact(args, contacts))
        else:
            print("Unknown command. Available commands: add, change, phone, delete.")