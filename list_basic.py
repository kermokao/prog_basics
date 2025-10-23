# two elements
def create_list_of_two_elements(a: int, b: int) -> list:
    elements = [a , b]
    return elements

create_list_of_two_elements(3,5)

# two edge elements
def create_list_with_edge_elements(elements: list) -> list:
    if len(elements) == 1:
        return [elements[0], elements[0]]
    else:
        return elements[0], elements[-1]
    
create_list_with_edge_elements(["Audi", "BMW", "Tesla"])

# middle elements
def get_middle_element_of_list(elements: list) -> any:
    if len(elements) == 1:
        return [elements[0]]
    length = len(elements)
    middle = length // 2
    print(elements[middle:middle:])
    
    
get_middle_element_of_list([1, 2, 3, 4, 5])