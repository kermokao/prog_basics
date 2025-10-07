# Are equal
def are_equal(num_a: int, num_b: int) -> str:
    if num_a == num_b:
        return "equal"
    else:
        return "not equal"
    
# Positive or negative

def positive_or_negative(num_a: int) -> str:
    if positive_or_negative > 0:
        return "positive"
    if positive_or_negative == 0:
        return "zero"
    if positive_or_negative < 0:
        return "negative"
    
# Is in string

def is_in_string(letter: str, word: str) -> bool:
    if letter in word:
        return True
    else:
        return False
    
# Are same length

def are_same_length(str_a: str, str_b: str) -> bool:
    if len(str_a) == len(str_b):
        return True
    else:
        return False
    
# Is letter or digit

def is_letter_or_digit(symbol: str) -> str:
    if symbol.isalpha()
        return "letter"
    if symbol.isdigit() 
        return "digit"
    else:
        return "other"
    
# last symbols

def are_last_symbols_same(str_a: str, str_b: str) -> bool:
    if str_a[-1] == str_b[-1]:
        return True
    else:
        return False
    
# Hundred

def hundred(num_a: int) -> int:
    if num_a <= 100:
        return 100 - num_a
    else:
        return num_a % 100
    
    
