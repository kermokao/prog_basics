def students_study(time: int, coffee_needed: bool) -> bool:
    if time >= 18 and time <= 24:
        return True
    elif time <= 17 and time >= 5 and coffee_needed == True:
        return True
    else:
        return False
    
def lottery(a: int, b: int, c: int) -> int:
    if a == 5 and b == 5 and c == 5:
        return 10
    elif a == b and a == c:
        return 5
    elif a != b and a != c:
        return 1
    else:
        return 0
    
def fruit_order(small_baskets: int, big_baskets: int, ordered_amount: int) -> int:
    small_baskets = 1 * small_baskets
    big_baskets = 5 * big_baskets
    if ordered_amount != small_baskets + big_baskets:
        return -1
    else:
        return small_baskets
    
print(fruit_order(3,1,10))
print(fruit_order(4,1,9))    
