# ************************ HOMEWORK 1 QUESTION 2 **************************
def question2(day, is_rainy):
    """
    The method is in charge of informing stranded... lonely... and *HUNGRY* cats where their next meal
    takes plays

    @param day: The given day
    @type day: str
    @param is_rainy: Holds a boolean statement, indicating whether it's raining or not.
    @type is_rainy: bool
    """


    if day in ('mon', 'wed', 'fri') and is_rainy is True:  #Given day is only three first lower cased letters of weekday and is_rainy is boolean
        print('Center Student')
    elif day in ('sun', 'tue', 'thu') and is_rainy is True:
        print('Library')
    elif day in ('mon', 'wed', 'fri') and is_rainy is False:
        print('Swimming Pool')
    elif day in ('sun', 'tue', 'thu') and is_rainy is False:
        print('Rager Gate')
    elif day in 'sat':
        print('Building No. 96')
    else:
        print('Please check if inputs are valid!')

question2('tue', False)

