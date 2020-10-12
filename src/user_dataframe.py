"""
Creates pandas DataFrame for a user
"""
from math import *
from statistics import mean

# third-party modules
import pandas as pd

# my modules
import data_checks



def set_index():
    """asks if the user wants to change the default names of the stats"""

    index = None    # Base case, eventually changed by user

    while True:
        ask = input("Voulez vous saisir vos propres noms de statistiques? (o/n) : ")

        if ask.lower() != 'n' and ask.lower() != 'o':
            print("ERREUR : format de réponse non pris en charge !\n")

        elif ask.lower() == 'n':
            break    # Answer is acceptable, exit loop

        else:
            print("Le nombre de noms de statistiques insérées déterminera le nombre de valeurs de statistiques à insérer ultérieurement.\n")
            index = input("Insérez les noms de statistiques séparés par des espaces : ").split()

            break    # Answer is acceptable, exit loop

    return index


def make_mean_dict_(index):
    """make mean dictionary"""
    do_repeat = True
    dict_ = {}  # Initializes empty dictionary
    while do_repeat:
        c_name = input("Insérez un titre : ").title()    # Transforms name to title case
        nb = input("Combien de personnes ont répondu au questionnaire ? ")
        stat_list=[]
        cpt=1
        while cpt<len(index)+1:
            lst = list(map(int, input(f"Insérez toutes les statistiques ({int(nb)}) du domaine {cpt} séparées par un espace, les valeurs excédentaires seront ignorées : ").split()))
            lst = lst[:len(index)]
            stat_list.append(mean(lst))
            cpt+=1

        # If not all the stats are numeric, the stats' request for the current character starts again
        if data_checks.check_stat_type(stat_list) is True:
            continue
        dict_[c_name] = stat_list

        while True:
            ask = input('Continuer? (o/n): ')  # Asks if you want to insert another line

            if ask.lower() != 'n' and ask != 'o':
                print("ERREUR : format de réponse non pris en charge !\n")
            elif ask.lower() == 'n':
                # Answer is NO, exit "continue?" loop AND user stats imput loop
                do_repeat = False
                break
            else:
                print()    # Print empty line to separate each user input
                # Answer is YES, exit "continue?" loop
                break
    return dict_


def make_mean_dataframe():
    """transforms stats dictionary into DataFrame"""
    index = set_index()
    if index is None:    # If index is not modified uses default index
        index = ['a', 'b', 'c', 'd', 'e']    # default index

    dict_ = make_mean_dict_(index)    # Asks user's name and stats
    data_checks.check_len(dict_, index)    # Fill empty values with zeroes

    return pd.DataFrame(dict_, index)    # Transform dictionary into DataFrame adding a line index