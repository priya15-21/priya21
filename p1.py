items = ["apple", "banana", "cherry"]
print("List=", items)
items[0] = "mango"
del items[1]
print("List output", items)

values = (10, 20, 30)
print("Tuple=", values)
values = (10, 25, 30)
values = values[:2]
print("Tuple output:", values)

numbers = {1, 2, 3}
print("Set=", numbers)
numbers = numbers | {5, 6}
numbers = numbers - {3}                      
print("Set output:", numbers)
