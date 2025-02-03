class InvalidInputException(Exception):
    def __init__(self, message):
        self.__message = message


    # def __str__(self):
    #     return f'ERROR: {self.__message}'


class OccupiedTableException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return f'ERROR: {self.__message}'


class TooSmallTableException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return f'ERROR: {self.__message}'


class EmptyTableException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return f'ERROR: {self.__message}'


class AccessDeniedException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return f'ERROR: {self.__message}'
