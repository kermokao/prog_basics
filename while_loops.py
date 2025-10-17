import random 

# make hola string
def make_hola_string(count: int) -> str:
    while count != 0:
        a = "hola"
        print(a, end="")
        count -= 1
        
# string with random length
def generate_string_with_random_length(threshold: float) -> str:
    result_string = ""
    while random.random() < threshold:
        result_string += "-"
    return result_string

# kasutaja vanuse küsimine
def ask_user_age(age_limit: int) -> int:
    while True:
        age = int(input("What is your age?: ")) 
        if age < age_limit:
            print("Too young!")
            break
        elif age > 100:
            print("Too old!")
            break
        elif age <= 100 and age >= 1:
            return age
        else:
            print("Wrong input!")
            
    
make_hola_string(None)
print(generate_string_with_random_length(0.9))
ask_user_age(10)
    