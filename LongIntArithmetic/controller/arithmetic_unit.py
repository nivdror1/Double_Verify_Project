

def add(num_arr1, num_arr2):
    """
    Sum the two numbers
    :param num_arr1: A number represented by an array
    :param num_arr2: A number represented by an array
    :return: The result of the addition
    """
    remainder = 0
    result_arr = [0] * len(num_arr1)

    for i in range(len(num_arr1) - 1, -1, -1):

        cur_result = num_arr1[i] + num_arr2[i] + remainder
        # if the current result is bigger then 10 then assign remainder=1 and subtract 10 from the result
        if cur_result >= 10:
            remainder = 1
            cur_result -= 10
        else:
            remainder = 0

        result_arr[i] = cur_result

    # Extend the array if the remainder is 1
    if remainder == 1:
        result_arr.insert(0, remainder)

    return result_arr


def find_the_smaller_num(num_arr1, num_arr2):
    """
    Find the smaller num by checking the length of the array
    :param num_arr1: A number represented by an array
    :param num_arr2: A number represented by an array
    :return: The smaller array and the bigger array
    """
    smaller_num = bigger_num = []

    # Find out which number is the smaller in length
    if len(num_arr1) <= len(num_arr2):
        smaller_num = num_arr1
        bigger_num = num_arr2
    else:
        smaller_num = num_arr2
        bigger_num = num_arr1
    return smaller_num, bigger_num


def long_int_addition(num_arr1, num_arr2):
    """
    Extend the array of the smaller number (if exists) and then Sum the two numbers by long addition method.
    :param num_arr1: A number represented by an array
    :param num_arr2: A number represented by an array
    :return: The result of the addition
    """

    smaller_num, bigger_num = find_the_smaller_num(num_arr1, num_arr2)

    # Extend the length of the array of smaller number so it will match the length of the bigger number
    while len(smaller_num) != len(bigger_num):
        smaller_num.insert(0, 0)

    # Perform long addition
    return add(smaller_num, bigger_num)


def long_int_multiplication(num_arr1, num_arr2):
    if num_arr1[0] == 0 or num_arr2[0] == 0:
        return [0]

    smaller_num, bigger_num = find_the_smaller_num(num_arr1, num_arr2)

    result_arr = []

    for i in range(len(smaller_num) - 1, -1, -1):
        temp_result = [0] * (len(smaller_num) - 1 - i)
        remainder = 0

        for j in range(len(bigger_num) - 1, -1 , -1):
            cur_result = (smaller_num[i] * bigger_num[j]) + remainder

            if cur_result > 10:
                remainder = cur_result // 10
                cur_result %= 10
            else:
                remainder = 0

            temp_result.insert(0, cur_result)

        while remainder >= 1:
            temp_result.insert(0,remainder % 10)
            remainder /= 10

        result_arr.append(temp_result)

    cur_addition_result = result_arr[0]
    for i in range(1, len(result_arr)):
        cur_addition_result = long_int_addition(cur_addition_result, result_arr[i])

    return cur_addition_result
