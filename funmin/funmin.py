

def fun_min(arr: list[int]) -> int:
    array_length = len(arr)
    if array_length == 0:
        raise EmptyArray
    initial_element = 0
    last_element = array_length - 1
    middle_element = 0
    while initial_element < last_element:
        middle_element = (initial_element + last_element) // 2

        if arr[middle_element] < arr[middle_element + 1]:
            last_element = middle_element
        else:
            initial_element = middle_element

        if middle_element == last_element - 1:
            middle_element = last_element
            break
    return arr[middle_element]


class EmptyArray(Exception):
    ...
