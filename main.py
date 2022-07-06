#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python method contains the application of the Game.

@contents :  This module contains the complete implementation of the application
             of the Game.
@project :  N/A
@program :  N/A
@file :  main.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Alberto Gil De la Fuente (alberto.gildelafuente@ceu.es)

@version :  0.0.1, 04 January 2021
@information :  The Zen of Python
                  https://www.python.org/dev/peps/pep-0020/
                Style Guide for Python Code
                  https://www.python.org/dev/peps/pep-0008/
                Example NumPy Style Python Docstrings
                  http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html
                doctest – Testing through documentation
                  https://pymotw.com/2/doctest/

@copyright :  Copyright 2021 GNU AFFERO GENERAL PUBLIC.
              All rights are reserved. Reproduction in whole or in part is
              prohibited without the written consent of the copyright owner.
"""


# Source packages.
import csv
from coach import Coach
from warrior_type import WarriorType
from weapon_type import WeaponType
from superwarrior import SuperWarrior
from warrior import Warrior

def get_data_from_user_1():
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------ 
      [ ] = get_data_from_user()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> get_data_from_user()
    """
    coach_set_of_warriors = []

    coach_name_s = "COACH 1"
    name_file_s = "coach_1_warriors.csv"
    try:
        with open(name_file_s, newline='') as csv_file:
            reader = csv.reader(csv_file)
            data_from_file = list(reader)
        for temp_warrior_csv in data_from_file:
            id = int(temp_warrior_csv[0])
            warrior_type = WarriorType.from_str(temp_warrior_csv[1])
            weapon_type = WeaponType.from_str(temp_warrior_csv[2])
            coach_warrior = SuperWarrior(id,
                                    warrior_type,
                                    weapon_type,
                                    int(temp_warrior_csv[3]),
                                    int(temp_warrior_csv[4]),
                                    int(temp_warrior_csv[5]),
                                    int(temp_warrior_csv[6]),
                                    int(temp_warrior_csv[7]))

            coach_set_of_warriors.append(coach_warrior)

    except Exception as e:
        print("Oops! The warriors of the coach were not introduced correctly." +
                " Try again...")
        print(e)

    # After the configuration we create the game user.
    temp_coach = Coach(coach_name_s, coach_set_of_warriors)

    return temp_coach


def get_data_from_user_2():
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------ 
      [ ] = get_data_from_user()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> get_data_from_user()
    """
    coach_set_of_warriors = []

    coach_name_s = "COACH 2"
    name_file_s = "coach_2_warriors.csv"
    try:
        with open(name_file_s, newline='') as csv_file:
            reader = csv.reader(csv_file)
            data_from_file = list(reader)
        for temp_warrior_csv in data_from_file:
            id = int(temp_warrior_csv[0])
            warrior_type = WarriorType.from_str(temp_warrior_csv[1])
            weapon_type = WeaponType.from_str(temp_warrior_csv[2])
            coach_warrior = SuperWarrior(id,
                                    warrior_type,
                                    weapon_type,
                                    int(temp_warrior_csv[3]),
                                    int(temp_warrior_csv[4]),
                                    int(temp_warrior_csv[5]),
                                    int(temp_warrior_csv[6]),
                                    int(temp_warrior_csv[7]))

            coach_set_of_warriors.append(coach_warrior)

    except Exception as e:
        print("Oops! The warriors of the coach were not introduced correctly." +
                " Try again...")
        print(e)

    # After the configuration we create the game user.
    temp_coach = Coach(coach_name_s, coach_set_of_warriors)

    return temp_coach

def get_data_from_user():
    """Function to obtain data from each user.

    This function obtains data from each user in order to set the configuration
    of the Game.

    Syntax
    ------ 
      [ ] = get_data_from_user()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> get_data_from_user()
    """
    coach_set_of_warriors = []

    while True:
        print("Provide the name of the Coach you want to play with...")
        coach_name_s = input(":~>")

        print("Provide the name of the file where the characteristics of " +
              "the warriors are stored.")
        name_file_s = input(":~>")
        try:
            with open(name_file_s, newline='') as csv_file:
                reader = csv.reader(csv_file)
                data_from_file = list(reader)

            print(data_from_file)

            for temp_warrior_csv in data_from_file:
                id = int(temp_warrior_csv[0])
                warrior_type = WarriorType.from_str(temp_warrior_csv[1])
                weapon_type = WeaponType.from_str(temp_warrior_csv[2])
                coach_warrior = SuperWarrior(id,
                                        warrior_type,
                                        weapon_type,
                                        int(temp_warrior_csv[3]),
                                        int(temp_warrior_csv[4]),
                                        int(temp_warrior_csv[5]),
                                        int(temp_warrior_csv[6]),
                                        int(temp_warrior_csv[7]))

                coach_set_of_warriors.append(coach_warrior)

        except Exception as e:
            print("Oops! The warriors of the coach were not introduced correctly." +
                  " Try again...")
            print(e)
            continue

        # Ask for a new Warrior to add to the Coach.
        answer = ''
        while answer not in ('YES', 'NO'):
            answer = input("Do you want to add a warrior to the coach? Answer YES or NO. \n" +
                           ":~>")
            if answer not in ('YES', 'NO'):
                print("The answer is incorrect.")

        if answer == "YES":
            continue

        if answer == "NO":
            break

    # After the configuration we create the game user.
    temp_coach = Coach(coach_name_s, coach_set_of_warriors)

    return temp_coach

def get_warrior_in_a_list_of_warriors(question,list_of_warriors):
    if isinstance(list_of_warriors,list):
        for warrior in list_of_warriors:
            if not isinstance(warrior,Warrior):
                raise TypeError("All warriors should be warrior Type")
        print(question + "\n")
        while True:
            print(str(list_of_warriors) + "\n")
            string_introduced = input(":~>")
            try:
                int_introduced= int(string_introduced)
            except Exception as e:
                print("Please, introduce an id present in the list:")
            for warrior in list_of_warriors:
                if(int_introduced == warrior.get_id()):
                    return warrior
            print("Please, introduce a number present in the list: ")
    else: 
        raise TypeError("list_warriors should be a list")

def main():
    """Function main of the module.

    The function main of this module is used to perform the Game.

    Syntax
    ------
      [ ] = main()

    Parameters
    ----------
      Null .

    Returns
    -------
      Null .

    Example
    -------
      >>> main()
    """

    print("Welcome to the Game.")
    print("Let's start to set the configuration of each game user. \n")

    # Get configuration for Game User 1.
    print("For Game User 1: \n")
    game_user_1 = get_data_from_user_1()

    # Get configuration for Game User 2.
    print("For Game User 2: \n")
    game_user_2 = get_data_from_user_2()

    print("------------------------------------------------------------------")
    print("The Game starts...")
    print("------------------------------------------------------------------")

    # Get a copy of the list of warriors:
    import copy
    temp_list_warriors_from_coach_1 = game_user_1.get_set_of_warriors()
    list_warriors_alive_coach_1 = copy.copy(temp_list_warriors_from_coach_1)
    
    temp_list_warriors_from_coach_2 = game_user_2.get_set_of_warriors()
    list_warriors_alive_coach_2 = copy.copy(temp_list_warriors_from_coach_2)
    # Choose first warriors
    print(game_user_1.get_coach_name() + ": choose your first warrior")
    temp_warrior_coach_1 = get_warrior_in_a_list_of_warriors("Please coach 1 introduce the id of the warrior", list_warriors_alive_coach_1)
    print(game_user_2.get_coach_name() + ": choose your first warrior")
    temp_warrior_coach_2 = get_warrior_in_a_list_of_warriors("Please coach 2 introduce the id of the warrior ",list_warriors_alive_coach_2)

    while(game_user_1.is_undefeated() and game_user_2.is_undefeated()):

        if not temp_warrior_coach_1.is_alive():
            # Select a new warrior
            print(game_user_1.get_coach_name() + ": your warrior: " + str(temp_warrior_coach_1) + " has been defeated. Please select the new warrior to fight ")
            list_warriors_alive_coach_1.remove(temp_warrior_coach_1)
            temp_warrior_coach_1 = get_warrior_in_a_list_of_warriors("Please coach 1 introduce the id of the warrior", list_warriors_alive_coach_1)
        if not temp_warrior_coach_2.is_alive():
            # Select a new warrior
            print(game_user_2.get_coach_name() + ": your warrior: " + str(temp_warrior_coach_2) + " has been defeated. Please select the new warrior to fight ")
            list_warriors_alive_coach_2.remove(temp_warrior_coach_2)
            temp_warrior_coach_2 = get_warrior_in_a_list_of_warriors("Please coach 2 introduce the id of the warrior", list_warriors_alive_coach_2)

        print("Game User 1 with coach " + game_user_1.get_coach_name() + " attacks.")
        temp_warrior_coach_1.fight_attack(temp_warrior_coach_2)
        print("Game User 2 with coach " + game_user_2.get_coach_name() + " attacks.")
        temp_warrior_coach_2.fight_attack(temp_warrior_coach_1)

        

        



    print("------------------------------------------------------------------")
    print("The Game has end...")
    print("------------------------------------------------------------------")
    if (game_user_1.is_undefeated() and not game_user_2.is_undefeated()):
        print("The WINNER is Game User 1.")
    elif (not game_user_1.is_undefeated() and game_user_2.is_undefeated()):
        print("The WINNER is Game User 2.")
    else:
        print("Both Game Users have been defeated. There is a DRAW.")


    print("------------------------------------------------------------------")
    print("Statistics")
    print("------------------------------------------------------------------")
    print("Game User 1:")
    temp_list_warriors_from_coach_1 = game_user_1.get_set_of_warriors()
    for temp_warrior in temp_list_warriors_from_coach_1:
        print(str(temp_warrior.get_warrior_type()) + " has a health of " +
              str(temp_warrior.get_health_points()) + " points.")
    print("Game User 2:")
    temp_list_warriors_from_coach_2 = game_user_2.get_set_of_warriors()
    for temp_warrior in temp_list_warriors_from_coach_2:
        print(str(temp_warrior.get_warrior_type()) + " has a health of " +
              str(temp_warrior.get_health_points()) + " points.")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
