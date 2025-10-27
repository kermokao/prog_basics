def get_sum_and_diff(a: int, b: int) -> tuple:
    sum_and_diff = (a + b, a - b)
    return sum_and_diff

def create_tuple_from_two_numbers(a: int, b: int) -> tuple:
    if a == b:
        return (a,)
    else:
        return (a, b)

def create_tuple_up_to_n(n: int) -> tuple:
    result = ()
    if n < 0:
        return result
    for num in range(0, n + 1,):
        result += (num,)
    return result

def merge_tuples(a: tuple, b: tuple) -> tuple:
    tuple_merge = a + b
    return tuple_merge

def remove_odd_numbers(numbers: tuple) -> tuple:
    numbers_process = []
    numbers = list(numbers)
    for i in range(len(numbers)):
        if numbers[i] % 2 == 0:
            numbers_process.append(numbers[i])
    return tuple(numbers_process)

def insert_tuple_inside_tuple(outer_tuple: tuple, position: int, inner_tuple: tuple) -> tuple:
    new_tuple = outer_tuple[:position] + inner_tuple + outer_tuple[position:]
    return new_tuple

print(remove_odd_numbers((2, 4, 6)))





        
