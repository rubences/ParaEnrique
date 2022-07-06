#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Warrior, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  warrior.py
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
import random
from warrior import Warrior
from warrior_type import WarriorType
from weapon_type import WeaponType


class SuperWarrior(Warrior):
    """Python class to implement an advanced version of a warrior of the game.

    This Python class implements the advanced version of a warrior of the game.

    Syntax
    ------
      obj = SuperWarrior(id, warrior_type, weapon_type, health_points,
                         attack_rating, defense_rating,
                         special_attack_rating, special_defense_rating)

    Parameters
    ----------
      [in] id Id of warrior.
      [in] warrior_type Type of warrior.
      [in] weapon_type Type of weapon that carries out the warrior.
      [in] health_points Points of health that the warrior has.
      [in] attack_rating Attack rating of the warrior.
      [in] defense_rating Defense rating of the warrior.
      [in] special_attack_rating Special Attack rating of the warrior.
      [in] special_defense_rating Special Defense rating of the warrior.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class SuperWarrior.

    Attributes
    ----------

    Example
    -------
      >>> from warrior import Warrior
      >>> obj_Warrior = Warrior("Boxer", "Fist", 99, 10, 7, 19, 18)
    """


    def __init__(self, id, warrior_type, weapon_type, health_points, attack_rating,
                 defense_rating, special_attack_rating, special_defense_rating):
        """Constructor of the class.

        This special method is executed when an object of this class is
        created.

        Syntax
        ------
          [ ] = __init__(self, warrior_type, weapon_type, health_points,
                         attack_rating, defense_rating,
                         special_attack_rating, special_defense_rating)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.
          [in] id Id of warrior.
          [in] warrior_type Type of warrior.
          [in] weapon_type Type of weapon that carries out the warrior.
          [in] health_points Points of health that the warrior has.
          [in] attack_rating Attack rating of the warrior.
          [in] defense_rating Defense rating of the warrior.
          [in] special_attack_rating Special Attack rating of the warrior.
          [in] special_defense_rating Special Defense rating of the warrior.

        Returns
        -------
          obj Python object output parameter that represents an instance
              of the class Warrior.

        Exceptions
        ----------
          TypeError:
          
            If the parameter id is NOT a int.
            If the parameter warrior_type is NOT a String.
            If the parameter weapon_type is NOT a String.
            If the parameter health_points is NOT be a int.
            If the parameter attack_rating is NOT be a int.
            If the parameter defense_rating is NOT be a int.
            If the parameter special_attack_rating is NOT be a int.
            If the parameter special_defense_rating is NOT be a int.

          ValueError:
          
            If the parameter id is already found in other warrior.
            If the parameter health_points is NOT > 0 and <= 100.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.
            If the parameter special_attack_rating is NOT > 10 and <= 20.
            If the parameter special_defense_rating is NOT > 10 and <= 20.

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior.__init__("Boxer", "Fist", 99, 10, 7, 19, 18)
        """
        # Constructor from the class Warrior.
        Warrior.__init__(self, id, warrior_type, weapon_type, health_points,
                         attack_rating, defense_rating)

        if isinstance(special_attack_rating, int):
            if 11 <= special_attack_rating <= 20:
                self._special_attack_rating = special_attack_rating
            else:
                raise ValueError("The parameter special_attack_rating should be > 10 and <= 20.")
        else:
            raise TypeError("The parameter special_attack_rating should be a int.")

        if isinstance(special_defense_rating, int):
            if 11 <= special_defense_rating <= 20:
                self._special_defense_rating = special_defense_rating
            else:
                raise ValueError("The parameter special_defense_rating should be > 10 and <= 20.")
        else:
            raise TypeError("The parameter special_defense_rating should be a int.")


    def get_special_attack_rating(self):
        """Method to get the attribute special_attack_rating of the object.

        Method to get the attribute special_attack_rating in a human-readable format of
        the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Warrior.get_special_attack_rating( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.

        Returns
        -------
          int The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.get_special_attack_rating( )
        """
        return self._special_attack_rating


    def get_special_defense_rating(self):
        """Method to get the attribute special_defense_rating of the object.

        Method to get the attribute special_defense_rating in a human-readable format of
        the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Warrior.get_special_defense_rating( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.

        Returns
        -------
          int The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.get_special_defense_rating( )
        """
        return self._special_defense_rating


    def set_special_attack_rating(self, special_attack_rating_to_be_set):
        """Method to set the attribute special_attack_rating of the object.

        Method to set the attribute special_attack_rating based on a
        human-readable format of the object that is formed in this
        class.

        Syntax
        ------
          [ ] = obj_Warrior.set_special_attack_rating(special_attack_rating_to_be_set)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.
          [in] special_attack_rating_to_be_set String that contains the special attack rating
                                               to assign to the warrior.

        Returns
        -------

        Exceptions
        ----------
        TypeError If the parameter attack_rating_to_be_set is NOT an int.
        ValueError If the parameter attack_rating_to_be_set is NOT  > 10 and <= 20.

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.set_special_attack_rating( )

        """
        if isinstance(special_attack_rating_to_be_set, int):
            if 1 <= special_attack_rating_to_be_set <= 10:
                self._special_attack_rating = special_attack_rating_to_be_set
            else:
                raise ValueError("The parameter special_attack_rating_to_be_set should be > 10 and <= 20.")
        else:
            raise TypeError("The parameter special_attack_rating_to_be_set should be a int.")


    def fight_attack(self, warrior_to_attack):
        """Method to attack using a hit to other warrior.

        Method that implements the attack of the warrior using a hit over other
        warrior.

        Syntax
        ------
          [ ] = obj_Warrior.fight_attack(warrior_to_attack)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.
          [in] Warrior warrior_to_attack Warrior to hit to.

        Returns
        -------

        Exceptions
        ----------
        TypeError If the parameter warrior_to_attach is NOT a Warrior.

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.fight_attack(warrior_enemy)
        """
        print("The warrior " + str(self) + " take a swing at the warrior " + str(warrior_to_attack) + ".")



        hit_probability = random.randrange(0, 2)

        if hit_probability == 0:  # Normal attack applied.
            points_of_damage = self._attack_rating
        else:  # Special attack applied.
            points_of_damage = self._special_attack_rating

        print("The warrior " + str(self) + " hits the warrior " + str(warrior_to_attack) +
                " with " + str(points_of_damage) + " points of damage!")
        warrior_hit = warrior_to_attack.fight_defense(points_of_damage)


        return warrior_hit


    def fight_defense(self, points_of_damage):
        """Method to defense from a hit of other warrior.

        Method that implements the defense of the warrior from a hit of other
        warrior.

        Syntax
        ------
          [ ] = obj_Warrior.fight_defense(points_of_damage)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.
          [in] int Points that represent the hit from another warrior.

        Returns
        -------

        Exceptions
        ----------
        TypeError If the parameter points_of_damage is NOT an int.

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.fight_defense(13)
        """
        if not isinstance(points_of_damage, int):
            raise TypeError("The parameter points_of_damage should be an int.")

        print("The warrior " + str(self) + " has received an attack of " +
              str(points_of_damage) + " points of damage.")

        failure_probability = random.randrange(0, 2)

        if failure_probability == 0:  # Normal defense applied.
            if points_of_damage > self._defense_rating:
                self._health_points = self._health_points - (points_of_damage - self._defense_rating)
                warrior_hit = True
            else:
                print("No damage received.")
                warrior_hit = False
        else:  # Special defense applied.
            if points_of_damage > self._special_defense_rating:
                self._health_points = self._health_points - (points_of_damage - self._special_defense_rating)
                warrior_hit = True
            else:
                print("No damage received.")
                warrior_hit = False

        # Normalizing the defeat of the warrior.
        if self._health_points < 1:
            self._health_points = 0

        return warrior_hit



def main():
    """Function main of the module.

    The function main of this module is used to test the Class SuperWarrior.

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

    print("=================================================================.")
    print("Test Case 1: Create a Warrior.")
    print("=================================================================.")
    warrior1 = SuperWarrior(1, WarriorType.GLADIATOR, WeaponType.SWORD, 100, 8, 9, 17, 15)

    if warrior1.get_warrior_type().name == "GLADIATOR":
        print("Test PASS. The parameter warrior_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_weapon_type().name == "SWORD":
        print("Test PASS. The parameter weapon_type has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_health_points() == 100:
        print("Test PASS. The parameter health_points has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_attack_rating() == 8:
        print("Test PASS. The parameter attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_defense_rating() == 9:
        print("Test PASS. The parameter defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_special_attack_rating() == 17:
        print("Test PASS. The parameter special_attack_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if warrior1.get_special_defense_rating() == 15:
        print("Test PASS. The parameter special_defense_rating has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    warrior2 = SuperWarrior(2, WarriorType.GLADIATOR, WeaponType.SWORD, 100, 7, 10, 19, 20)

    if str(warrior2) == "GLADIATOR with a SWORD and health: 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(warrior2))


    print("=================================================================.")
    print("Test Case 3: Warrior alive?¿?.")
    print("=================================================================.")
    warrior3 = SuperWarrior(3, WarriorType.UFC, WeaponType.KICK, 97, 8, 9, 12, 14)

    if warrior3.is_alive():
        warrior3.fight_defense(200)  # With this the warrior should be retired.

        if not warrior3.is_alive():
            print("Test PASS. The method is_alive() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method is_alive().")
    else:
        print("Test FAIL. Check the method is_alive().")


    print("=================================================================.")
    print("Test Case 4: Check the defense during a Fight.")
    print("=================================================================.")
    warrior4 = SuperWarrior(4, WarriorType.MMA, WeaponType.ELBOW, 93, 9, 6, 17, 14)

    warrior4.fight_defense(70)

    if (warrior4.get_health_points() == 29) or ((warrior4.get_health_points() == 37)):
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    warrior5 = SuperWarrior(5, WarriorType.BOXER, WeaponType.PUNCH, 99, 10, 7, 19, 18)
    warrior6 = SuperWarrior(6, WarriorType.BOXER, WeaponType.PUNCH, 99, 9, 8, 20, 17)

    warrior_hit = warrior5.fight_attack(warrior6)

    print(warrior6.get_health_points())

    if warrior_hit:
        if (warrior6.get_health_points() == 97) or ((warrior6.get_health_points() == 88)):
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")
    else:
        if warrior6.get_health_points() == 99:
            print("Test PASS. The method fight_attack() has been implemented correctly.")
        else:
            print("Test FAIL. Check the method fight_attack().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
