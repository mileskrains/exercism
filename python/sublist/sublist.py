SUBLIST, SUPERLIST, EQUAL, UNEQUAL = 'sublist superlist equal unequal'.split()


def check_lists(first_list, second_list):
    len_first = len(first_list)
    len_second = len(second_list)
    if first_list == second_list:
         return EQUAL
    elif len_first > len_second and is_sublist_of(first_list, second_list):
        return SUPERLIST
    elif len_first < len_second and is_sublist_of(second_list, first_list):
        return SUBLIST
    else:
        return UNEQUAL


def is_sublist_of(first_list, second_list):
    second_len = len(second_list)
    for sp in range(len(first_list) - second_len + 1):
        if first_list[sp:sp + second_len] == second_list:
            return True
    return False
