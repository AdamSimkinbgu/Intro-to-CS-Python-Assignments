# ************************ HOMEWORK 1 QUESTION 3 **************************
def question3(input_num):
    """
    The method is given a number, then builds a pyramid in which the first line starts with the given
    number one time. going forward, each line lowers said number by one and increasing the times printed by 1.

    @param: input_num - The given number
    @type: input_num - int
    @param: i - Managing both the line in which the method is correctly operating on, lowering the number each line
                and multiplying the times the number is printed.
    @type: i - int
    """
        
    for i in range(0, input_num):
        print(str(input_num-i) * (i+1))



"""
        Second solution I came up with. due to restrictions thought to be given,
        the solution was rewritten
    
    temp_cell = input_num
    iteration_of_program = 0
    while temp_cell > 0:
        iteration_of_program += 1
        counter = 1
        while counter <= iteration_of_program:
            print(temp_cell, end='')
            counter += 1
        print()
        temp_cell -= 1
"""
question3(5)