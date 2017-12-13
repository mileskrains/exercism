def binary_search(list_of_numbers, number):
    start_index = 0
    end_index = len(list_of_numbers) - 1
    while end_index >= start_index:
        middle_index = (start_index + end_index)//2
        middle_number = list_of_numbers[middle_index]
        if middle_number == number:
            return middle_index
        elif middle_number > number:
            end_index = middle_index - 1
        elif middle_number < number:
            start_index = middle_index + 1
    raise ValueError
