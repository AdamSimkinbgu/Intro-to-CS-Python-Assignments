# ************************ HOMEWORK 1 QUESTION 4 **************************
def question4(input_list):
    """
    The method is given a list of numbers and runs through it, summing all and evaluating whether they sum
    to zero.
    If a sum of zero is found, the method returns the avg of the highest and lowest integers.
    The method will output a print of "error" if:
        1) The list is of a length of 0, meaning its empty.
        2) The list does not sum to 0 at the end.

    @param: sum_of_list - Follows the sum of the list.
    @param: input_list - The list given to the program.
    @param: lowest_num - Holds the lowest value number of the list.
    @param: highest_num - Holds the highest value number of the list.
    @param: i & j - 2 loop parameters. 'i' moves the pointer of the object evaluated during the algorithm.
                                       'j' is responsible to find the highest and lowest numbers of the list.
    @type: input_list - list
           sum_of_list & lowest_num & highest_num & i & j - int
    """
    if len(input_list) == 0:
        print('error')
    sum_of_list = 0
    for i in range(len(input_list)):
        sum_of_list += input_list[i]
        if sum_of_list == 0:
            highest_num = 0
            lowest_num = 0
            for j in range(i):
                if len(input_list) > 0 and j == 0:
                    highest_num = input_list[j]
                    lowest_num = input_list[j]
                elif int(input_list[j]) > highest_num:
                    highest_num = input_list[j]
                elif int(input_list[j]) < lowest_num:
                    lowest_num = input_list[j]
            if (highest_num + lowest_num) % 2 == 0:
                print(int((highest_num + lowest_num) / 2))  # average of numbers which sum to zero in int form
                break
            else:
                print((highest_num + lowest_num) / 2)  # average of numbers which sum to zero in float form
                break
        elif sum_of_list != 0 and i == len(input_list)-1:
            print('error')







    """
    Because of miss understanding during the assignment progress, I was preparing a version to comply with
    the limitations thought to be mandatory. (losing the functionality to convert float to int)
    
    if len(input_list) == 0:
        print('error')
    sum_of_list = 0
    list_index_sum_tracker = 0
    counter = 0
    for number_in_index in input_list:
        sum_of_list += input_list[counter]
        counter += 1
        if sum_of_list == 0:
            highest_num = 0
            lowest_num = 0
            counter = 0
            while counter <= list_index_sum_tracker:
                    if len(input_list) > 0 and counter == 0:
                        highest_num = input_list[counter]
                        lowest_num = input_list[counter]
                    elif int(input_list[counter]) > highest_num:
                        highest_num = input_list[counter]
                    elif int(input_list[counter]) < lowest_num:
                        lowest_num = input_list[counter]
                    counter += 1
            temp = (highest_num + lowest_num) / 2
            print(round(temp, 2))
            return

        elif sum_of_list != 0 and counter == len(input_list) - 1:
            print('error')
        list_index_sum_tracker += 1
            
            """