"""Functions to parse a file containing villager data."""


def all_species(filename):
    """Return a set of unique species in the given file.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - set[str]: a set of strings
    """

    species = set()

    # open filename
    list_of_species = open(filename)
    # for loop to get each line in the file
    for item in list_of_species:
        # in each line of data, remove the whitespace on the right and seperate each item (separator |)
        item.rstrip()
        item_token = item.split('|')
        # get each species from the item_token list; index 1
        each_specie = item_token[1]
        # add each specie to the set
        species.add(each_specie)

    # close file
    list_of_species.close()

    return species

# species = all_species("villagers.csv")
# print(species)

def get_villagers_by_species(filename, search_string="All"):
    """Return a list of villagers' names by species.

    Arguments:
        - filename (str): the path to a data file
        - search_string (str): optional, the name of a species

    Return:
        - list[str]: a list of names
    """

    villagers = []

    villager_info = open(filename)


    for line in villager_info:
        line.rstrip()
        tokenized_villager_info = line.split("|")
        villager_name = tokenized_villager_info[0]
        villager_specie = tokenized_villager_info[1]
        
        # species = all_species(filename)
        # append all villagers name to the villagers list if search string is all
        if search_string == "All":
            villagers.append(villager_name)

        
        elif villager_specie == search_string:
            villagers.append(villager_name)

            # print("*******************")
            # # loop over all the species from all_species function, if species match the search_string
            # for each_specie in species:
            #     if each_specie == search_string:
            #         # add the villager name to the villagers list
            #         villagers.append(villager_name)

    villager_info.close()

    return sorted(villagers)

print(get_villagers_by_species("villagers.csv", "Rabbit"))
# print(get_villagers_by_species("villagers.csv"))

def all_names_by_hobby(filename):
    """Return a list of lists containing villagers' names, grouped by hobby.

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[list[str]]: a list of lists containing names
    """

    # TODO: replace this with your code

    return []


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (name, species, personality, hobby,
    saying).

    Arguments:
        - filename (str): the path to a data file

    Return:
        - list[tuple[str]]: a list of tuples containing strings
    """

    all_data = []

    # TODO: replace this with your code

    return all_data


def find_motto(filename, villager_name):
    """Return the villager's motto.

    Return None if you're not able to find a villager with the
    given name.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name

    Return:
        - str: the villager's motto or None
    """

    # TODO: replace this with your code


def find_likeminded_villagers(filename, villager_name):
    """Return a set of villagers with the same personality as the given villager.

    Arguments:
        - filename (str): the path to a data file
        - villager_name (str): a villager's name
    
    Return:
        - set[str]: a set of names

    For example:
        >>> find_likeminded_villagers('villagers.csv', 'Wendy')
        {'Bella', ..., 'Carmen'}
    """

    # TODO: replace this with your code
