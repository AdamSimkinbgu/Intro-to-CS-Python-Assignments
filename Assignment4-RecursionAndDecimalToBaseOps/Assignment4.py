def semi_factorial(num):
    """
    This method is calculating the value for a new operator ('$'). The operator takes each odd number and recursively
    multiplies it with the number before it, summing the odd sequence and adding one at the end. If an even number
    is given, sum its value to the next recursive value of the odd number before it.
    for example: even number: 2k$ = 2k + (2k-1) * (2k-2) + (2k-3) * (2k-4) + ..... + 3 * 2 + 1
                 odd number: n$ = n * (n-1) + (n-2) * (n-3) + ..... + 3 * 2 + 1
    :param num [int] - a given number to be evaluated
    :return the value of the calculation
    """
    if num == 1:
        return 1
    if num == 2:
        return 3
    if num % 2 == 0:
        return num + semi_factorial(num - 1)
    return num * (num - 1) + semi_factorial(num - 2)


def string_overlap_detector(core, rep, repetition):
    """
    This method is taking two strings and compares for overlapping subsequences, depending on the required repetition,
    returns true or false.
    :param core [str] - first string (to be checked on)
    :param rep [str] - second string (to be checked with)
    :param repetition [int] - number of repetition required of rep in core
    :return bool value
    """
    if len(core) == 0:
        if repetition == 0:
            return True
        return False
    if core[:len(rep)] == rep:
        repetition -= 1
        return string_overlap_detector(core[1:], rep, repetition)
    return string_overlap_detector(core[1:], rep, repetition)


def string_overlap_dual(string_1, string_2, repetition):
    """
    This method enhances the functionality of @string_overlap_detector, allowing the function to check whether
    the strings could be switched during the evaluation to find the first string in the second as well as second string
    in the first string
    :param string_1 [str] - first string
    :param string_2 [str] - second string
    :param repetition [int] - number of repetition required of rep in core (or other way around)
    :return bool value
    """
    if len(string_1) >= len(string_2):
        if string_overlap_detector(string_1, string_2, repetition):
            return True
        return False
    if len(string_2) == 0:
        if repetition == 0:
            return True
        return False
    if string_2[:len(string_1)] == string_1:
        repetition -= 1
        return string_overlap_dual(string_2[1:], string_1, repetition)
    return string_overlap_dual(string_2[1:], string_1, repetition)


def longest_super_subsequence(input_list):
    """
    This method is used as a starter for the recursion, receiving the list from the user and passing it over to
    the driver method (@helper) for the process of the recursion itself.
    :param input_list [list] - A given list
    :return The value passed from the @helper function, which is the max length of the subset encountered during
            the recursion.
    """
    if not input_list or input_list[0] < 0 and len(input_list) == 1:
        return 0
    return helper(input_list, input_list[0], 0, 1, 0, 0)

def helper(num_list, prev_sum, index, cnt, maxi, checker):
    """
    This is the main driver method of the recursion. The recursion follows the sum of the previous numbers to the
    current index, keeps track of the index it's in, counting the length of the subset and comparing the subsets
    during the recursion to follow the longest subset.
    :param num_list [list] - The given list, past over each recursion to follow the original list.
    :param prev_sum [int] - Follows the sum of numbers after each recursion step.
    :param index [int] - Follows the current index the recursion is looking at.
    :param cnt [int] - Keeps track of the current subset length
    :param maxi [int] - Keeps the longest subset under itself.
    :param checker [int] - Used as a flag to represent if the subset is counted from the start of the list or is shorter.
    :return The longest subset length encountered during the process of the recursion
    """
    if index == len(num_list):
        if checker == 0:
            return maxi - 1
        return maxi
    if num_list[index] >= prev_sum and index != len(num_list) - 1:
        cnt += 1
    elif index == len(num_list) - 1:
        if num_list[index] >= prev_sum:
            cnt += 1
            if cnt > maxi:
                maxi = cnt
        else:
            if cnt > maxi:
                maxi = cnt
    else:
        checker = 1
        if cnt > maxi:
            maxi = cnt
        cnt = 1
    return helper(num_list, prev_sum + num_list[index], index + 1, cnt, maxi, checker)

print(longest_super_subsequence([-2, -1]))
print(longest_super_subsequence([0, 5, 10, 14, 30, 60 ,120, 240, 230]))
print(longest_super_subsequence([0, 3, 2]))
print(longest_super_subsequence([22, 23, 24, 25, 26, 27]))



def base_to_decimal(string_to_convert, base_num):
    """
    This method translates a base number representation to a decimal one based on a demanded base [set between 2-10]
    :param string_to_convert [str] - string to be converted (base of any size)
    :param base_num [int] - a required base for translation
    :return the translated base to decimal in int form.
    """
    if len(string_to_convert) == 0:
        return 0
    power_multiplier = len(string_to_convert) - 1
    return int(string_to_convert[0]) * (base_num ** power_multiplier) + base_to_decimal(string_to_convert[1:], base_num)


def decimal_to_base(string_to_convert, base_num):
    """
    This method does the opposite of @base_to_decimal, taking a decimal number and translating it to a set base number
    [set between 2-10]
    :param string_to_convert [str] - string to be converted (base of any size)
    :param base_num [int] - a required base for translation
    :return the translated decimal to base in int form.
    """
    if len(string_to_convert) == 0:
        return 0
    power_multiplier = len(string_to_convert) - 1
    return int(string_to_convert[0]) * (base_num ** power_multiplier) + decimal_to_base(string_to_convert[1:], base_num)

word = 'noa'
print(word[1])

