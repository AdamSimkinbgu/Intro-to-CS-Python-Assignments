# ************************ HOMEWORK 1 QUESTION 1 **************************
def question1(radius, height):
    """
    This method is responsible to calculate the volume of a cylinder.

    @param: radius - A given radius of the cylinder.
    @param: height - A given height of the cylinder.
    @type: both are integers.
    """
    print('************ TO DO: Question 1 ************')
    Volume = 3.14 * radius**2 * height  #Given radius and height are positive
    print(round(Volume, 2))







"""

At first I thought I was suppose to provide everything to the program so I wrote this

rad = int(input('Please enter the radius: '))
h = int(input('Please enter the height: '))
while rad =< 0 or h =< 0:
    print('Please enter only whole positive numbers (including 0)')
    rad = int(input('Please enter the radius: '))
    h = int(input('Please enter the height: '))
question1(rad, h)

"""