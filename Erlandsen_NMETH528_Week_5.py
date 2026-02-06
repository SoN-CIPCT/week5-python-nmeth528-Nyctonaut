fruit = ["apple", "banana", "cherry", "date", "elderberry", "grape"]

first_two = fruit[:2]
print(f"The first two items in the list are: {first_two[0]}, {first_two[1]}")

middle_two = fruit[2:4]
print(f"The middle two items in the list are: {middle_two[0]}, {middle_two[1]}")

print(f"The first and last items in the list are: {fruit[0]}, {fruit[-1]}")

# Original menu (tuple with five foods)
menu = ("Burger", "Pizza", "Salad", "Pasta", "Soup")

# Print each item using a for loop
print("Original Menu:")
for item in menu:
    print(item)

# Updated menu (replace two items by creating a new tuple)
revised_menu = ("Burger", "Sushi", "Salad", "Tacos", "Soup")

# Print each item on the revised menu
print("\nRevised Menu:")
for item in revised_menu:
    print(item)
