def create_set_from_numbers(a: int, b: int, c:int) -> set:
    return {a, b, c}

def add_one(set_a: set) -> set:
    return {num + 1 for num in set_a}

def remove_six(set_a: set) -> set:
    set_a.discard(6)
    return set_a

def convert_to_set(list_a: list) -> set:
    list_a = set(list_a)
    return list_a

def count_unique_elements(input_list: list) -> int:
    input_list = set(input_list)
    unique_number = len(input_list)
    return unique_number

def common_characters_in_words(word1: str, word2: str) -> set:
    a = set(word1)
    b = set(word2)
    return a.intersection(b)

def exam_conditions_not_met(names1: list, names2: list) -> set:
    a = set(names1)
    b = set(names2)
    return a.symmetric_difference(b)

def uninvited_friends_count(friends: list, invited: list) -> int:
    a = set(friends)
    b = set(invited)
    not_invited_friends = a.difference(b)
    return len(set(not_invited_friends))

def contains_duplicates(input_list: list) -> bool:
    a = set(input_list)
    b = set(input_list)
    if a.intersection(b):
        return True
    else:
        return False

        
#print(create_set_from_numbers(1, 2, 3))
#print(create_set_from_numbers(1, 2, 1))
#print(create_set_from_numbers(1, 1, 1))
#print(add_one({1, 2, 3}))
#print(remove_six({1, 2, 3, 4, 5, 6, 7, 8, 9}))
#print(convert_to_set([1, 2, 3, 1]))
#print(count_unique_elements([1, 2, 3]))
#print(common_characters_in_words("Hello","Hi"))
#print(exam_conditions_not_met(["Mati"], ["Mati", "Kati"]))
#print(uninvited_friends_count(["mati", "kati"], ["kati"]))
print(contains_duplicates([1, 2, 3]))
