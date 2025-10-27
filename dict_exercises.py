def get_hobbies(hobbies_dict: dict, name: str) -> list:
    if name not in hobbies_dict:
        return "name not in dictionary"
    else:
        return hobbies_dict[name]
    
get_hobbies(hobbies_dict, "Tom")

def find_tallest(height_dict: dict) -> str:
    tallest = max(height_dict, key=height_dict.get)
    return tallest

def remove_sixes(six_dict: dict) -> dict:
    return {keys: value for key, value in six_dict.items() if value % 6 != 0}
    
def exchange_keys_and_values(exchange_dict: dict) ->:
   swap_list = {value: key for key, value in exchange_dict.items()}
   return swap_list

def count_symbol_appearances(stringy:str) -> dict:
    result = {}
    for word in stringy:
        letter = word
        if letter not in result:
            result[letter] = 1
        else:
            result[letter] += 1
    return result

def organise_by_first_symbol(strings: list) -> dict:
    result = {}
    for word in strings:
        first_symbol = word[0]
        if first_symbol not in result:
            result[first_symbol] = [word]
        else:
            result[first_symbol].append(word)
    return result

print(count_symbol_appearances("hello hi"))
print(organise_by_first_symbol(["hello", "word", "world", "welcome", "yes"]))

