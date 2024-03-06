def fourdigit_number_operations(num):
    if type(num) == int and 999 < num <= 9999:
        print("Initial number: "+str(num))
        list_num = [int(i) for i in str(num)]
        print("The product of digits is: " + str(find_digit_product(list_num)))
        list_num.reverse()
        print("The number with its digits in reverse order: "+str(make_number_from_num_arr(list_num)))
        print("The number with digits sorted in ascending order: " + str(make_number_from_num_arr(sorted(list_num))))
    else:
        raise ValueError("Invalid input")
    pass


def find_digit_product(num_arr):
    result = 1
    for num in num_arr:
        result *= num
    return result


def make_number_from_num_arr(arr):
    result = ""
    for num in arr:
        result += str(num)
    return int(result)


fourdigit_number_operations(3128)