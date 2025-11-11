def loop_reverse(s: str) -> str:
    reversed_string = ""
    for i in s:
        reversed_string = i + reversed_string
    return reversed_string

def recursive_reverse(s: str) -> str:
    if s == "":
        return ""
    else:
        return recursive_reverse(s[1:]) + s[0]

def loop_sum(n: int) -> int:
    total = 0
    for num in range(0, n + 1):
        total += num
    return total

def recursive_sum(n: int) -> int:
    if n == 0:
        return 0
    return n + recursive_sum(n - 1)

def sum_digits_recursive(number: int) -> int:
    if number < 10:
        return number
    return number % 10 + sum_digits_recursive(number // 10)

def pair_star_recursive(s: str) -> str:
    if len(s) <= 1:
        return s
    if s[0] == s[1]:
        return s[0] + "*" + pair_star_recursive(s[1:])
    else:
        return s[0] + add_star(s[1:])
    
