@@ -1,29 +1,9 @@
"""Function examples."""


def func():
    """123."""
    print("I´m inside the function")


def my_name_is(name) -> str:
    """123."""
    print("My name is " + (name))


def sum_six(num) -> int:
    """123."""
    return 6 + num


def sum_numbers(num_a: int, num_b: int):
    """123."""
    return num_a + num_b


def usd_to_eur(usd: int):
    """123."""
    return usd * 0.8
    
    
    
def sum_between(start: int, end: int) -> int:
    total = 0
    for number in range(start, end + 1):
        total = total + number
    return total
print(sum_between(3,5))
        
