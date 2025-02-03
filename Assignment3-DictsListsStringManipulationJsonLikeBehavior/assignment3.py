############################# Q1 #############################
def cinema_to_dict(lst):
    """
    This method is responsible to produce a dictionary out of a given list of lists, containing cinema seating info.
    @param: lst [list] - A given list of lists, each index is a list of row seats
    @return: lst_of_dicts [dict] - A dict with keys representing seat and row (row, seat) and the value
    is the seating info.
    """
    lst_of_dicts = {}
    for row in range(len(lst)):
        for seat in range(len(lst[row])):
            if lst[row][seat] == 0:
                continue
            lst_of_dicts[(row + 1, seat + 1)] = lst[row][seat]  # Key is a tuple containing (row, seat), value is the seating info
    return lst_of_dicts


def seat_case_for_1(dict_of_cinema, space_to_check, seat_to_check):
    """
    This is a supportive method implemented to check if seat is occupied with a 1 case.
    @param: space_to_check [int] - Number of seats to check over each side.
    @param: dict_of_cinema [dict] - Dict of seats, keys represent seat numbers, values the seat info.
    @param: seat_to_check [tuple] - Given seat in dict to check.
    @return: A bool statement regarding the invalidity of the seating. Bad seating would return True,
             otherwise returns False.
    """
    if dict_of_cinema.get(seat_to_check) == 1:
        if (dict_of_cinema.get((seat_to_check[0], seat_to_check[1] - space_to_check)) == (1 or 2)) \
        or (dict_of_cinema.get((seat_to_check[0], seat_to_check[1] + space_to_check)) == (1 or 2)) \
        or (dict_of_cinema.get((seat_to_check[0] - space_to_check, seat_to_check[1])) == (1 or 2)) \
        or (dict_of_cinema.get((seat_to_check[0] + space_to_check, seat_to_check[1])) == (1 or 2)):
            return True
    return False


def seat_case_for_2(dict_of_cinema, space_to_check, seat_to_check):
    """
    This is a supportive method implemented to check if seat is occupied with a 2 case.
    @param: space_to_check [int] - Number of seats to check over each side.
    @param: dict_of_cinema [dict] - Dict of seats, keys represent seat numbers, values the seat info.
    @param: seat_to_check [tuple] - Given seat in dict to check.
    @return: A bool statement regarding the invalidity of the seating. Bad seating would return True,
             otherwise returns False.
    """
    if dict_of_cinema.get(seat_to_check) == 2:
        if ((dict_of_cinema.get((seat_to_check[0], seat_to_check[1] - 1)) == 2) \
        and (dict_of_cinema.get((seat_to_check[0], seat_to_check[1] + 1)) == None)) \
        or ((dict_of_cinema.get((seat_to_check[0], seat_to_check[1] - 1)) == None) \
        and (dict_of_cinema.get((seat_to_check[0], seat_to_check[1] + 1)) == 2)):  # Checks both sides and both cases of couples sitting together
            if ((dict_of_cinema.get((seat_to_check[0], seat_to_check[1] - 2)) == (1 or 2)) \
            or (dict_of_cinema.get((seat_to_check[0], seat_to_check[1] + 2)) == (1 or 2))) \
            or (dict_of_cinema.get((seat_to_check[0] - space_to_check, seat_to_check[1])) == (1 or 2)) \
            or (dict_of_cinema.get((seat_to_check[0] + space_to_check, seat_to_check[1])) == (1 or 2)):  # Checks both sides for occupied seats
                return True
        else:
            return True
    return False


def verify_seating_arrangement(cinema):
    """
    This is the main method that inspects and confirms/denys the validity of a cinema hall
    @param: cinema [] - Given list of lists with seating information
    @return: A bool statement representing the validity of the given hall
    """
    dict_of_cinema = cinema_to_dict(cinema)
    for seat_to_check in dict_of_cinema.keys():
        for space_to_check in range(1, 3):
            if seat_case_for_1(dict_of_cinema, space_to_check, seat_to_check):
                return False
            elif seat_case_for_2(dict_of_cinema, space_to_check, seat_to_check):
                return False
    return True


############################# Q2.1 #############################
def is_DNA(DNA_seq):
    """
    This method inspects a given string to confirm it's a DNA sample. If so, registers a list of each cell of DNA
    @param: DNA_seq [str] - A given string to inspect.
    @return: converted_seq [list] - A list containing the DNA cells in each index.
    """
    converted_seq = []
    DNA_string = ''
    place_in_DNA = 0
    allowed_letters = ['A', 'C', 'G', 'T']
    for DNA_letter in DNA_seq:
        place_in_DNA += 1
        if place_in_DNA % 4 == 0:
            converted_seq.append(DNA_string)
            DNA_string = ''
            if DNA_letter == (' '):
                continue
            else:
                return 'Not DNA seq'
        elif DNA_letter in allowed_letters:
            DNA_string += DNA_letter
        else:
            return 'Not DNA seq'
    if len(DNA_string) != (0 or 3):
        return 'Not DNA seq'
    else:
        converted_seq.append(DNA_string)
    return converted_seq


############################# Q2.2 #############################

def DNA_to_RNA(DNA_seq):
    """
    This method is translating a DNA sample into RNA sample.
    @param: DNA_seq [list] - Given list of DNA cells.
    @return: converted_RNA [list] - A list of RNA cells. If given invalid DNA sample, returns an empty list.
    """
    listed_DNA = is_DNA(DNA_seq)
    converted_RNA = []
    if listed_DNA == 'Not DNA seq':
        return []
    for cell in listed_DNA:
        converted_RNA.append(cell.replace("T", "U"))
    return converted_RNA


############################# Q2.3 #############################
def codon_translator(codon):
    RNA_to_protien = {"UUU": "Phe", "UUC": "Phe", "UUA": "Leu", "UUG": "Leu",
                      "UCU": "Ser", "UCC": "Ser", "UCA": "Ser", "UCG": "Ser",
                      "UAU": "Tyr", "UAC": "Tyr",
                      "UGU": "Cys", "UGC": "Cys", "UGG": "Trp",
                      "CUU": "Leu", "CUC": "Leu", "CUA": "Leu", "CUG": "Leu",
                      "CCU": "Pro", "CCC": "Pro", "CCA": "Pro", "CCG": "Pro",
                      "CAU": "His", "CAC": "His", "CAA": "Gln", "CAG": "Gln",
                      "CGU": "Arg", "CGC": "Arg", "CGA": "Arg", "CGG": "Arg",
                      "AUU": "Ile", "AUC": "Ile", "AUA": "Ile", "AUG": "Met",
                      "ACU": "Thr", "ACC": "Thr", "ACA": "Thr", "ACG": "Thr",
                      "AAU": "Asn", "AAC": "Asn", "AAA": "Lys", "AAG": "Lys",
                      "AGU": "Ser", "AGC": "Ser", "AGA": "Arg", "AGG": "Arg",
                      "GUU": "Val", "GUC": "Val", "GUA": "Val", "GUG": "Val",
                      "GCU": "Ala", "GCC": "Ala", "GCA": "Ala", "GCG": "Ala",
                      "GAU": "Asp", "GAC": "Asp", "GAA": "Glu", "GAG": "Glu",
                      "GGU": "Gly", "GGC": "Gly", "GGA": "Gly", "GGG": "Gly", }
    decoding = RNA_to_protien.get(codon, "stop")
    return decoding


def RNA_to_Protein(DNA_seq):
    """
    This method is using the given dict to translate codons, comparing those to the given list of RNA and
    in return outputs a list of Proteins. If the given RNA list is invalid, return an empty tuple.
    @param: DNA_seq [list] - Given list of DNA.
    @return: converted_RNA_Protein [tuple] - For valid input, a tuple with the appropriate protein, otherwise ().
    """
    listed_RNA = DNA_to_RNA(DNA_seq)
    converted_RNA_Protein = []
    if len(listed_RNA) == 0:
        return ()
    if listed_RNA[0] != 'AUG':
        return ()
    for cell in listed_RNA:
        if cell in ['UAA', 'UAG', 'UGA']:
            return tuple(converted_RNA_Protein)
        Protein_to_add = codon_translator(cell)
        if Protein_to_add == 'stop':
            return ()
        converted_RNA_Protein.append(Protein_to_add)
    return ()


############################# Q3.1 #############################
def test_veganism(vegan_things_to_check):
    """
    A supportive method tasked with validating the ingredient being checked is vegan or not by evaluating the
    string given. If the string contains "True", the same would be returned as a boolean statement - otherwise,
    False will be returned.
    @param: vegan_things_to_check [str] - The string to be checked.
    @return: A boolean statement regarding the inclusion of the string "True".
    """
    if "True" in vegan_things_to_check :
        return True
    else:
        return False


def ingredient_identifier(list_of_ingredients):
    """
    This method is going through all the ingredients in a given list of strings, splitting each string to create a
    dictionary of a menu. The string is being sliced using the index function. Anything till the colon is the key,
    from the colon to the comma is the nutritional value and from the comma to the end is if the ingredient vegan.
    @param: list_of_ingredients [list] - The input list of ingredients.
    @return: dict_of_ingredients [list] - A dictionary with ingredients.
    """
    dict_of_ingredients = {}
    for ingredient_in_list in list_of_ingredients:
        ingredient_name = ingredient_in_list[:ingredient_in_list.index(':')]
        ingredient_nutri_val = ingredient_in_list[ingredient_in_list.index(':') + 1:ingredient_in_list.index(",")]
        ingredient_is_vegan = ingredient_in_list[ingredient_in_list.index(",") + 1:]
        ingredient_is_vegan = test_veganism(ingredient_is_vegan)
        dict_of_ingredients[ingredient_name] = {'nutritional_value': float(ingredient_nutri_val), 'vegan': ingredient_is_vegan}
    return dict_of_ingredients


############################# Q3.2 #############################
all_ingredients = ["Carrot: 123.4, True", "Sweet potato: 100.0, True", "Salmon: 120.0, False", "Cucumber: 90.0, True",
                   "Lettuce: 35.0, True", "Soya beans: 139.8, True", "Tofu: 260, True", "Red Meat: 400, False",
                   "Tuna: 360, False", "Tomato: 50, True", "Potato: 210, True", "Rice: 240, True",
                   "Green beans: 170.0, True", "Egg: 110.0, False", "Pasta: 266.6, True", "Mushrooms: 221.1, True",
                   "Green lentils: 220.9, True", "Pepper: 12.0, True", "Ricotta cheese: 233.4, False",
                   "Mozarella: 311.0, False", "Chicken: 220, False", "Salt: 0, True",
                   "Sugar: 141, True", "Unsalted butter: 321.0, False", "Olive: 120.0, True", "Bread: 140.0, True",
                   "Bell pepper: 119.8, True", "Onion: 121, True", "Broccoli: 12.1, True"]


def meal_calculator(recipes, all_ingredients_details=ingredient_identifier(all_ingredients)):
    """
    This method is given a dictionary with recipes and ingredients making those recipes & an ingredient info dictionary.
    The method uses the ingredient identifier to evaluate the given string in the ingredient info dictionary if not
    given a dict of ingredients.
    @param: recipes [dict] - A given dict with recipes.
    @param: all_ingredients_details [dict] - A dictionary of ingredients and their info.
    @return: dict_of_meals_info [dict] - A dictionary of meal names and their info.
    """
    dict_of_meals_info = {}
    for meal in recipes:
        num_of_ingredients = 0
        nutritional_value_calc = 0
        meal_is_vegan = True
        ingredient_list = recipes.get(meal)
        for ingredient in ingredient_list:
            num_of_ingredients += 1
            ingredient_to_add = all_ingredients_details.get(ingredient)
            nutritional_value_calc += ingredient_to_add.get('nutritional_value')
            if ingredient_to_add.get('vegan') == False:
                meal_is_vegan = False
        dict_of_meals_info[meal] = (num_of_ingredients, nutritional_value_calc, meal_is_vegan)
    return dict_of_meals_info


############################# Q3.3 #############################
all_ingredients = ["Carrot: 123.4,False", "Sweet potato: 100.0,False", "Salmon fish: 120.0,True",
                   "Cucumber: 90.0,False",
                   "Lettuce: 35.0,False", "Soya beans: 139.8,False", "Tofu: 260,False", "Red Meat: 400,True",
                   "Tuna: 360,True", "Tomato: 50,False", "Potato: 210,False", "Rice: 240,False",
                   "Green beans: 170.0,False", "Egg: 110.0,True", "Pasta: 266.6,False", "Mushrooms: 221.1,False",
                   "Green lentils: 220.9,False", "Pepper: 12.0,False", "Ricotta cheese: 233.4,True",
                   "Mozarella: 311.0,True", "Chicken: 220,True", "Salt: 0,False",
                   "Sugar: 141,False", "Unsalted butter: 321.0,True", "Olive: 120.0,False", "Bread: 140.0,False",
                   "Bell pepper: 119.8,False", "Onion: 121,False", "Broccoli: 12.1,False"]


def popular_meal(meals_info):
    """
    This method is checking a dictionary of meals (keys) and meal order number (values) and comparing them to check
    which meal was ordered the most.
    @param: meals_info [dict] - A dictionary with meal names and the number they were ordered.
    @return: A tuple with the name of the most ordered meal (all caps) and the fractional value out of all the
             ordered meals.
    """
    max_meal_ordered = [None, 0]
    sum_of_meals_ordered = sum(list(meals_info.values()))
    for meal in meals_info.keys():
        if meals_info.get(meal) > max_meal_ordered[1]:
            max_meal_ordered[0] = meal
            max_meal_ordered[1] = meals_info[meal]
    if not meals_info:
        return tuple(max_meal_ordered)
    return tuple([max_meal_ordered[0].upper(), max_meal_ordered[1] / sum_of_meals_ordered])