# def hello_func():
#     print("Hello, World!")
#     name = input("What is your name? ")
#     print(f"Nice to meet you, {name}!")

# hello_func()
def add(a, b):
    return a + b
add1 = add(2, 3)
print(add1)

# default parameter
def subtract(a, b=0):
    return a - b
subtract1 = subtract(5)
print(subtract1)

# multi add
def multi_add(*args):
    total = 0
    for num in args:
        total += num
    return total
multi_add1 = multi_add(1, 2, 3, 4, 5, 6)
print(multi_add1)