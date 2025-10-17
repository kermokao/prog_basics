def sum_between(start: int, end: int) -> int:
    total = 0
    for number in range(start, end + 1):
        total = total + number
    return total
print(sum_between(3,5))
        

        