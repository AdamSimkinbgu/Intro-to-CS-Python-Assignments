#############################################################################################################

def matrix_explorer(n, m):
    """
    This method is given a rectangle, divided to squares with n lines and m rows. The shortest distance any route
    in a rectangle of any size can be the number of ( n + m - 1 ). Any point in the rectangle can lead to an
    ever-increasing number of possible lanes. by adding both vertical and horizontal possibilities,
    the program can check how many possible lanes are left from any position in the rectangle.
    :param n [int] - The number of given lines.
    :param m [int] - The number of given rows.
    :return Returns [int] the number of possible routes in the rectangle.
    """
    if n == 1 or m == 1:
        return 1

    return matrix_explorer(n - 1, m) + matrix_explorer(n, m - 1)



def matrix_explorer_memo_recursive(n, m, memo):
    """
    This method is an upgrade to @maze_explorer, using memoization to decrease the amount of calculations during
    the process. each recursive call checks whether the tuple (representing a cell in the rectangle) has a calculated
    value of possible lanes from it to the end, shortening the amount of processing power required and the amount of
    space used.
    :param n [int] - The number of given lines.
    :param m [int] - The number of given rows.
    :param memo [dict] - A dictionary used to record reached lanes.
    :return: [int] The amount of possible lanes to a given input.
    """
    if n == 1 or m == 1:
        return 1

    if (n, m) in memo:
        return memo[(n, m)]

    else:
        memo[(n, m)] = matrix_explorer_memo_recursive(n - 1, m, memo) + matrix_explorer_memo_recursive(n, m - 1, memo)
        return memo[(n, m)]


def matrix_explorer_memo(n, m):
    """
    This method passes the input to @matrix_explorer_memo_recursive, a dictionary is used to enhance efficiency.
    :param n [int] - The number of given lines.
    :param m [int] - The number of given rows.
    :return [int] The amount of possible lanes to a given input.
    """
    memo = {}
    return matrix_explorer_memo_recursive(n, m, memo)


########################################## Question 2 #########################################################


def count_coin_sets_recursive(value, coins, memo):
    """
    This method is the helping recursion of the @count_coin_sets that calls it. The method looks for all possible
    combinations to represent a given value with a list of "coins", it does so by summing split cases. the first part
    deducts a coin from the value until its no longer possible, the other drops the coin as a possible "deducter" to
    the value. combining all possible cases results with the number of combinations possible. While calculating each
    possible case, the method creates a dict to follow results and shorten the time spent calculating.
    :param value [int] - A given value to represent with coins.
    :param coins [list of ints] - A given list of "coins" to try and represent the value with. renamed for comfort.
    :param memo [dict] - An auto generated dictionary of calculated values.
                         dictionary info: key = (value, tuple(coins left)) value = number of possible cases
    :return: An int of the number of possible representation cases.
    """
    if value < 0 or len(coins) == 0:
        return 0
    if value == 0:
        return 1

    if memo.get((value, tuple(coins))):
        return memo.get((value, tuple(coins)))

    memo[(value, tuple(coins))] = count_coin_sets_recursive(value - coins[0], coins, memo) + count_coin_sets_recursive(value, coins[1:], memo)
    return memo[(value, tuple(coins))]


def count_coin_sets(value, list_of_coins):
    """
    This method is the main calling function of the recursion, receiving the value and list of coins from the user,
    passing it to the recursive method to process its values.
    :param value [int] - A given value to represent with coins.
    :param list_of_coins [list of ints] - A given list of "coins" to try and represent the value with.
    :return: An int returned from the @count_coin_sets_recursive function, An int of the number of possible
             representation cases.
    """
    memo = {}
    return count_coin_sets_recursive(value, list_of_coins, memo)


############################################## Question 3 ############################################################

def rosh_zanav_rec(word, memory, lihiscore, naftulscore, step_counter):
    """
    This method is the driving side of the algorithm, checking all possible outcomes of the players choices and returns
    a bool statement whether the word is safe for player 2 (Naftul).
    :param word [str] - A given word.
    :param memory [dict] - A dictionary to keep score to be given.
    :param lihiscore [int] - Value to keep Lihi's score.
    :param naftulscore [int] - Value to keep Naftul's score.
    :param step_counter [int] - Value to keep count of turns.
    :return [bool] A bool statement whether a word is safe and Naftul is going to win no matter what.
    """
    if len(word) == 0:
        if naftulscore > lihiscore:
            return True
        return False

    if word[0] == word[len(word) - 1] and len(word) == 4:
        if step_counter % 2 == 0:
            return False

    if step_counter % 2 == 0:
        if word[0] >= word[len(word) - 1]:
            return rosh_zanav_rec(word[1:], memory, lihiscore, naftulscore + memory.get(str(word[0]), 0), step_counter + 1)
        return rosh_zanav_rec(word[:len(word) - 1], memory, lihiscore, naftulscore + memory.get(str(word[len(word) - 1]), 0), step_counter + 1)

    if word[0] > word[len(word) - 1]:
        return rosh_zanav_rec(word[1:], memory, lihiscore + memory.get(str(word[0]), 0), naftulscore, step_counter + 1)
    return rosh_zanav_rec(word[:len(word) - 1], memory, lihiscore + memory.get(str(word[len(word) - 1]), 0), naftulscore,step_counter + 1)


def rosh_zanav(word):
    """
    This method calls @rosh_zanav_rec to return whether a given word is safe for player 2 (meaning he always means
    no matter what player 1 does) as a bool statement.
    :param word [str] - A given word.
    :return [bool] A bool statement whether a word is safe and Naftul is going to win no matter what.
    """
    memory2 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12,
               'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23,
               'x': 24, 'y': 25, 'z': 26}
    return rosh_zanav_rec(word, memory2, 0, 0, 1)

print(rosh_zanav("breakfast"))
####################################### ADDED YOAV'S RECURSION PROBLEM ######################################




def da_real_rec_sums(array_rec, sum1, sum2, i):
    if i == len(array_rec):
        return sum1 == sum2
    return da_real_rec_sums(array_rec, sum1 + array_rec[i], sum2, i + 1) or da_real_rec_sums(array_rec, sum1, sum2 + array_rec[i], i + 1)

def rec_sums(array):
    sum1 = 0
    sum2 = 0
    i = 0
    return da_real_rec_sums(array, sum1, sum2, i)



def da_real_rec_sums_yoav(array_rec, sum1=0, sum2=0, i=0):
    if i == len(array_rec):
        return sum1 == sum2
    if da_real_rec_sums_yoav(array_rec, sum1 + array_rec[i], sum2, i + 1):
        return true
    if da_real_rec_sums_yoav(array_rec, sum1, sum2 + array_rec[i], i + 1):
        return true
    return False



def rec_sums_yoav(array):
    return da_real_rec_sums(array)

