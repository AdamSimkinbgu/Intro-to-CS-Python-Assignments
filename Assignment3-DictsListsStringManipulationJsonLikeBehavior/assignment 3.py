# dict1 = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}
# for i in range(4, 11):
#     dict1[f'key{i}'] = f'value{i}'
# print(dict1)

def cinema_to_dict(lst):
    lst_of_dicts = {}
    row = 0
    for i in range(len(lst)):
        for j in range(len(lst[row])):
            if lst[row][j] == 0:
                continue
            lst_of_dicts[(row+1, j+1)] = lst[row][j]
        row += 1
    return lst_of_dicts



def verify_seating_arrangment(cinema):
    dict_of_cinema = cinema_to_dict(cinema)
    row = 0
    for seat_to_check in dict_of_cinema.keys():
        row += 1
        for i in range(1, 3):
            if dict_of_cinema.get(seat_to_check) == 1:
                if (dict_of_cinema.get((seat_to_check[0], seat_to_check[1]-i)) == (1 or 2)) or (dict_of_cinema.get((seat_to_check[0], seat_to_check[1]+i)) == (1 or 2)):
                    return False
                if (dict_of_cinema.get((seat_to_check[0] - i, seat_to_check[1])) == (1 or 2)) or (dict_of_cinema.get((seat_to_check[0] + i, seat_to_check[1])) == (1 or 2)):
                    return False
            elif dict_of_cinema.get(seat_to_check) == 2:
                if ((dict_of_cinema.get((seat_to_check[0], seat_to_check[1] - 1)) == 2) and (dict_of_cinema.get((seat_to_check[0], seat_to_check[1] + 1)) == None)) or ((dict_of_cinema.get((seat_to_check[0], seat_to_check[1] - 1)) == None) and (dict_of_cinema.get((seat_to_check[0], seat_to_check[1] + 1)) == 2)): # Checks both sides and both cases of couples sitting together
                    if ((dict_of_cinema.get((seat_to_check[0], seat_to_check[1] - 2)) == (1 or 2)) or (dict_of_cinema.get((seat_to_check[0], seat_to_check[1] + 2)) == (1 or 2))):
                        return False
                    elif (dict_of_cinema.get((seat_to_check[0] - i, seat_to_check[1])) == (1 or 2)) or (dict_of_cinema.get((seat_to_check[0] + i, seat_to_check[1])) == (1 or 2)):
                        return False
                else:
                    return False
                if (dict_of_cinema.get((seat_to_check[0] - i, seat_to_check[1])) == 2) or (dict_of_cinema.get((seat_to_check[0] + i, seat_to_check[1])) == 2):
                    return False

    return True

cinema1 = [[0, 0, 0, 1, 0, 0, 1],
           [1, 0, 0, 0, 0, 0 ,0],
           [0, 0, 0, 0, 0, 1 ,0],
           [0, 0, 0, 1, 0, 0, 1],
           [2, 2, 0, 0, 0, 0, 0]]

cinema2 = [[1, 0, 0, 1, 0, 0, 1],
           [0, 0, 1, 0, 0, 1, 0],
           [0, 1, 0, 0, 0, 1, 0],
           [1, 0, 0, 1, 0, 0, 1],
           [0, 0, 0, 0, 0, 0, 1]]

test1 = [[0, 0, 2, 2, 0, 0, 1],
         [1, 0, 0, 0, 1, 0, 0],
         [0, 1, 0, 0, 0, 1, 0]]

test2 = [[1, 0, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0, 0]]

test3 = [[1, 0, 0, 1, 0, 0, 1],
         [0, 0, 0, 2, 2, 1, 0],
         [0, 1, 0, 0, 1, 0, 0]]

test4 = [[2, 0, 0, 1, 0, 0, 1],
         [0, 0, 1, 0, 0, 1, 0],
         [0, 1, 0, 0, 1, 0, 0]]


# print(cinema_to_dict(cinema1))

# print(verify_seating_arrangment(test1),'test')
# print(verify_seating_arrangment(test2))
# print(verify_seating_arrangment(test3))
# print(verify_seating_arrangment(test4))

# if dict_of_cinema.get(seat_to_check) == dict_of_cinema.get(
#         (seat_to_check[0], seat_to_check[1] - i)) or dict_of_cinema.get(seat_to_check) == dict_of_cinema.get(
#         (seat_to_check[0], seat_to_check[1] + i)):
#     if (dict_of_cinema.get(seat_to_check) == 1 and dict_of_cinema.get((i, seat_to_check[1] - i)) == 1) or (
#             dict_of_cinema.get(seat_to_check) == 1 and dict_of_cinema.get((i, seat_to_check[1] + i)) == 1):
#         return False
#     if (dict_of_cinema.get(seat_to_check) and dict_of_cinema.get((seat_to_check[0], seat_to_check[1] - 1)) == 2) or (
#             dict_of_cinema.get(seat_to_check) and dict_of_cinema.get((seat_to_check[0], seat_to_check[1] + 1)) == 2):
#         continue
# if dict_of_cinema.get(seat_to_check) == dict_of_cinema.get(
#         (seat_to_check[0] - i, seat_to_check[1])) or dict_of_cinema.get(seat_to_check) == dict_of_cinema.get(
#         (seat_to_check[0] + i, seat_to_check[1])):
#     return False


def is_DNA (DNA_seq):
    place_in_DNA = 0
    allowed_letters = ['A', 'C', 'G', 'T']
    for DNA_letter in DNA_seq:
        place_in_DNA += 1
        if place_in_DNA % 4 == 0:
            if DNA_letter != (' '):
                return False
        elif DNA_letter not in allowed_letters:
            return False
    return True

dnatest = 'ATG ATT TTA GCA CGA TGC TGC TTA TAA'

print(is_DNA(dnatest))

