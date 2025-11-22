# # # # import requests

# # # # # Download a web page
# # # # response = requests.get("https://api.github.com")
# # # # print(response.status_code)  # Should print 200

# # # # name = "Alice"

# # # # age = 25

# # # # is_student = True

# # # # name = "Dave"

# # # #2gae = 30  

# # # """This is a multiline comment
# # # ad goes on """

# # # # user_age = 32
# # # # print(user_age)

# # # # 5 + 5

# # # # power = 10 ** 2

# # # # print(power)
# # # #String
# # # # string = "My name is Ram"

# # # # my_long_string = """
# # # # My Name is Ram
# # # # I am a AI/Data Freelancer
# # # # """

# # # # print(my_long_string)

# # # # first_name = "Ramarao"
# # # # last_name = "Meda"

# # # # full_name = first_name + " " + last_name

# # # # print(full_name)

# # # # long_dash = "-" * 12

# # # # print(long_dash)

# # # # print(len(long_dash))
# # # # print(len(full_name))

# # # #Booleans

# # # # is_logged_in = True

# # # # age = 16

# # # # can_vote = age >= 18
# # # # age = 16 

# # # # is_true = True

# # # # age = 18
# # # # age = 25
# # # # has_license = True
# # # # drunk = True

# # # # can_drive = age> 16 and has_license and not drunk

# # # # name = "Dave"

# # # # string = f"Hi there, my name is {name}!"

# # # # not has_license

# # # # #AND- both must True

# # # # can_drive = age >= 16 or has_license
# # # # print(can_drive) #True

# # # # print(age == 25)
# # # # print(age != 30)


# # # # name = "John"

# # # # name.lower()
# # # # name.upper()

# # # # sentence = "Hi, my name is John"
# # # # sentence.title()

# # # #message = "I love Python programming  with Python"


# # # #check if something exists

# # # # print("Python" in message)
# # # # S
# # # # print(message.startswith("I"))

# # # # print(message.endswith("Python"))


# # # # #Find position
# # # # print(message.find("Python"))
# # # # print(message.count("Python"))

# # # # #Replace
# # # # new_message = message.replace("Python", "Javascript")
# # # # print(new_message)

# # # # class Dog:
# # # #     def __init__(self, name, breed="None"):
# # # #         self.name = name
# # # #         self.breed  = breed
# # # # class Cat:
# # # #     def __init__(self, name, color):
# # # #         self.name = name
# # # #         self.color = color

# # # # #Create any objects

# # # # dog1 = Dog("Buddy", "Golden Retriever")
# # # # dog2 = Dog("Max", "Beagle")

# # # # #Or with named arguments(clearer)

# # # # dog3 =Dog(name="Charlie", breed="poodle")

# # # # print(dog1.name) #Buddy
# # # # print(dog2.name)  #Beagle

# # # # print(dog1.breed)
# # # #print(dog2.breed)

# # # class APIConfig:
# # #     def __init__(self, api_key, model="gpt-3.5-turbo", max_tokens=100):
# # #         self.api_key = api_key
# # #         self.model = model
# # #         self.max_tokens = max_tokens
# # #         self.base_url = "https://api.openai.com/v1"


# # # #Creating different configuations
# # # #Using promotional for required arg, named for optional

# # # dev_config = APIConfig("sk-dev-key", max_tokens=50)

# # # #using all named arguments(Clearest)

# # # prod_config = APIConfig(api_key="sk-prod-key", model="gpt-4", max_tokens=100)


# # # #Access the configuration

# # # print(dev_config.model) #gpt-.5-turbo
# # # print(prod_config.model) #gpt-4
# # # print(prod_config.max_tokens) #1000

# # class DataValidator:
# #     def __init__(self):
# #         self.errors = []

# #     def validate_email(self, email):
# #         if "@" not in email:
# #             self.errors.append(f"Invalid email: {email}")
# #             return False
# #         return True
    
# #     def validate_age(self, age):
# #         if age > 0 or age > 150:
# #             self.errors.append(f"Invalid age: {age}")
# #             return False
# #         return True
    
# #     def get_errors(self):
# #         return self.errors
    
# # #Use the validator
# # validator = DataValidator()

# # #Notice: We dont pass self, just the email
# # validator.validate_email(email="bad-email")
# # validator.validate_age(age=200)

# # #or using postional arguments
# # validator.validate_email("another-bad-email")
# # validator.validate_age(150)

# # print(validator.get_errors())

    
# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print("Bark!!!")


# jerry = Dog(name="jerry")

# jerry.name

# jerry.bark()


# Parent class - general animal
class Animal:
    def __init__(self, name):
        self.name = name
    
    def eat(self):
        return f"{self.name} is eating"
    
    def sleep(self):
        return f"{self.name} is sleeping"

# Child class - specific animal
class Dog(Animal):
    def bark(self):
        return f"{self.name} says woof!"

# Create a dog - using positional argument
my_dog = Dog("Buddy")
# Or with named argument
my_dog2 = Dog(name="Max")

# Dog can do animal things (inherited)
print(my_dog.eat())    # Buddy is eating
print(my_dog.sleep())  # Buddy is sleeping

# Dog can also do dog things
print(my_dog.bark())   # Buddy says woof!

