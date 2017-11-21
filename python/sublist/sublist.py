def check_lists(first_list, second_list):
    second_len = len(second_list)
    for sp in range(len(first_list) - second_len + 1):
        if first_list[sp:sp + second_len] == second_list:
            return True
    return False
