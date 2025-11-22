# temperature = 31

# if temperature > 30:
#     print("It's very hot!")
# elif temperature > 25:
#     print("It's hot!")
# else:
#     print("It's nice weather!")
    
# score = 95

# if score >= 90:
#     print("A - Excellent!")
# elif score >= 80:
#     print("B - Good job!")
# elif score >= 70:
#     print("C - Keep it up!")
# else:
#     print("F - Need improvement")

# has_ticket = False
# age = 18

# if has_ticket:
#     if age >= 18:
#         print("Enjoy the movie!")        
#     else:
#         print("Needs supervision!")
        
# else:
#     print("Please buy a ticket!")
    
    
# for  i in range(5):
#         print("Hello World!")

# for i in range(1, 7):
#     print(i)
    
# for i in range(0,10,2):
#      print(i)

# age = 25
# has_license = False

# my_list = ["Alice", 25, age, True, has_license]

# name = my_list[0]
# age = my_list[1]


# has_license = my_list[-1]

# my_list[0] = "Rama"

# my_list.append("Dave")

# my_list.remove("Dave")


# my_list.insert(1, "Dave")

#Empty dictionary
# my_dict = {}
# person = {
    
#     "name" : "Alice",
#     "age" : 25,
#     "city": "New york"
    
# }

# # person["name"] = "Dave"

# # person["license"] = True

# # del  ["license"]
# # Different ways to create
# scores = dict(math=95, english=87, science=92)


# person = {"name": "Alice", "age": 30, "city": "New York"}

# # Get values by key
# print(person["name"])       # "Alice"
# print(person["age"])        # 30

# # Safer with get()
# print(person.get("job"))    # None (no error)
# print(person.get("job", "Unknown"))  # "Unknown" (default)

# person = {"name" : "Alice", "age" : 34}

# person["email"] = "alice@gmail.com"
# person["age"] = 31

# #Remove items

# del person["email"]
# age = person.pop("age")
# person.clear()

# person = {"name": "Alice", "age": 30, "city": "New York"}

# # Get all keys, values, or items
# print(person.keys())    # dict_keys(['name', 'age', 'city'])
# print(person.values())  # dict_values(['Alice', 30, 'New York'])
# print(person.items())   # dict_items([('name', 'Alice'), ...])

# # Check if key exists
# if "name" in person:
#     print("Name found!")

# # Update multiple values
# person.update({"age": 31, "job": "Engineer"})


# empty = ()

# point = (3,5)
# colors = ("red", "green", "blue")

# #get items
# print(point[0])
# print(colors[-1])

# #slicing
# print(colors[0:2])

# colors = {"red", "blue"}

# # Add items
# colors.add("green")
# print(colors)  # {'red', 'blue', 'green'}

# # Remove items
# colors.remove("blue")    # Error if not found
# colors.discard("yellow") # No error if not found

# # Check membership
# if "red" in colors:
#     print("Red is available")

# empty_set = set()

# #Set with values - both ways work

# numbers = {1,2,3,4,5}
# fruits = set(["apple", "banana", "orange", "banana"])

# #From a list
# scores = [85, 90, 85, 92, 90]
# unique_scores = set(scores)
def greet():
    print("Hello!")
    
greet()


