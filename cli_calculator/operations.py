def addition(numbers):
    addition = {sum(numbers)}

    if isinstance(addition, int):
        addition = int(addition)

    return addition

def operation(numbers, operation):
    number_list = list(numbers)

    try:
        result = number_list[0]
    except IndexError:
        return 0 

    if operation == '*' or operation =='/':
        number_list[0] = 1
    else:
        number_list[0] = 0

    for i in number_list:
        if operation == '*':
            result *= i
        elif operation == '-':
            result -= i
        elif operation == '/':
            result /= i

    return result


