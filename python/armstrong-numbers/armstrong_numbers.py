def is_armstrong(number):
    digit_count = len(str(number))
    return number == sum([int(digit)**digit_count for digit in str(number)])
