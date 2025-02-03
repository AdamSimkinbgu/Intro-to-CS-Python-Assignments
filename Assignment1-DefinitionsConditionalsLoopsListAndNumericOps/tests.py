import question1
import question2
import question3
import question4


def test_question1():
    radius = 2  # Change me!
    height = 4  # Change me!
    question1.question1(radius, height)


def test_question2():
    day = 'mon'  # Change me!
    is_rainy = True  # Change me!
    question2.question2(day, is_rainy)


def test_question3():
    input_num = 9  # Change me!
    question3.question3(input_num)


def test_question4():
    input_list = [7, 12 , -20 , -3, 4 ,15 , -2]  # Change me!
    question4.question4(input_list)


if __name__ == '__main__':
    test_question1()
    test_question2()
    test_question3()
    test_question4()
