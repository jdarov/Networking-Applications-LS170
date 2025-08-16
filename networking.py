def print_something(greeting):
    def inner(person):
        return f"{greeting} {person}"
    return inner

hello = print_something("Hello")

print(hello("Josh"))