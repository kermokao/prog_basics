import math

def print_hello():
    print("hello")
    
def get_hello():
    return get_hello

def ask_name_and_greet_user():
    name = input("What is your name: ")
    name = name.capitalize()
    if name == "Thanos":
        print("Get out of here, Thanos! Nobody wants to play with you!")
    else:
        print(f"Hi, {capitalize_name}. Would you like to have a Hamburger?")
        
def calculate_hypotenuse_length(a: float, b: float) -> float:
    return math.sqrt(a ** 2 + b ** 2)
        
def calculate_cathetus_length(a: float, c: float) -> float:
    return math.sqrt(c ** 2 - a ** 2)
    
print_hello()
hello = get_hello()
ask_name_and_greet_user()
print(calculate_hypotenuse_length(3, 4))
print(calculate_cathetus_length(3, 5))