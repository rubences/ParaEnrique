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
from warrior_type import WarriorType
from weapon_type import WeaponType


class Warrior():
    """Python class to implement a basic version of a warrior of the game.

    This Python class implements the basic version of a warrior of the game.

    Syntax
    ------
      obj = Warrior(id, warrior_type, weapon_type, health_points,
                    attack_rating, defense_rating)

    Parameters
    ----------
      [in] id Id of warrior.
      [in] warrior_type Type of warrior.
      [in] weapon_type Type of weapon that carries out the warrior.
      [in] health_points Points of health that the warrior has.
      [in] attack_rating Attack rating of the warrior.
      [in] defense_rating Defense rating of the warrior.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Warrior.

    Attributes
    ----------

    Example
    -------
      >>> from warrior import Warrior
      >>> from warrior_type import WarriorType
      >>> from weapon_type import WeaponType
      >>> obj_Warrior = Warrior(1, WarriorType.GLADIATOR, WeaponType.SWORD, 100, 7, 10)
    """

    __list_ids=[]
    def __init__(self, id, warrior_type, weapon_type, health_points, attack_rating,
                 defense_rating):
        """Constructor of the class.

        This special method is executed when an object of this class is
        created.

        Syntax
        ------
          [ ] = __init__(self, warrior_type, weapon_type, health_points,
                         attack_rating, defense_rating)

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
            If the parameter health_points is NOT be an int.
            If the parameter attack_rating is NOT be a int.
            If the parameter defense_rating is NOT be a int.

          ValueError:
            If the parameter id is already found in other warrior.
            If the parameter health_points is NOT > 0 and <= 100.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.
            If the parameter attack_rating is NOT > 0 and <= 10.
            If the parameter defense_rating is NOT > 0 and <= 10.

        Example
        -------
          >>> from warrior import Warrior
          >>> from warrior_type import WarriorType
          >>> from weapon_type import WeaponType
          >>> obj_Warrior = Warrior.__init__(1, WarriorType.GLADIATOR, WeaponType.SWORD, 100, 7, 10)
        """

        if isinstance(id, int):
            if id not in Warrior.__list_ids:
                self._id = id
            else:
                raise ValueError("The parameter id should be a new id not taken by other warrior.")
        else:
            raise TypeError("The parameter id should be a int.")

        if isinstance(warrior_type, WarriorType):
            self._warrior_type = warrior_type
        else:
            raise TypeError("The parameter warrior_type should be a WarriorType.")

        self.set_weapon_type(weapon_type)

        if isinstance(health_points, int):
            if 1 <= health_points <= 100:
                self._health_points = health_points
            else:
                raise ValueError("The parameter health_points should be > 0 and <= 100.")
        else:
            raise TypeError("The parameter health_points should be a int.")

        self.set_attack_rating(attack_rating)

        if isinstance(defense_rating, int):
            if 1 <= defense_rating <= 10:
                self._defense_rating = defense_rating
            else:
                raise ValueError("The parameter defense_rating should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter defense_rating should be a int.")
        # Add the id to the list of ids
        Warrior.__list_ids.append(id)


    def get_id(self):
        """Method to get the attribute id of the object.


        Syntax
        ------
          [ ] = obj_Warrior.get_id( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.get_id( )
        """
        return self._id

    def get_warrior_type(self):
        """Method to get the attribute warrior_type of the object.

        Method to get the attribute warrior_type in a human-readable format of
        the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Warrior.get_warrior_type( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.get_warrior_type( )
        """
        return self._warrior_type


    def get_weapon_type(self):
        """Method to get the attribute weapon_type of the object.

        Method to get the attribute weapon_type in a human-readable format of
        the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Warrior.get_weapon_type( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.get_weapon_type()
        """
        return self._weapon_type


    def get_health_points(self):
        """Method to get the attribute health_points of the object.

        Method to get the attribute health_points in a human-readable format of
        the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Warrior.get_health_points( )

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
          >>> obj_Warrior.get_health_points( )
        """
        return self._health_points


    def get_attack_rating(self):
        """Method to get the attribute attack_rating of the object.

        Method to get the attribute attack_rating in a human-readable format of
        the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Warrior.get_attack_rating( )

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
          >>> obj_Warrior.get_attack_rating( )
        """
        return self._attack_rating


    def get_defense_rating(self):
        """Method to get the attribute defense_rating of the object.

        Method to get the attribute defense_rating in a human-readable format of
        the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Warrior.get_defense_rating( )

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
          >>> obj_Warrior.get_defense_rating( )
        """
        return self._defense_rating


    def set_weapon_type(self, weapon_type_to_be_set):
        """Method to set the attribute weapon_type of the object.

        Method to set the attribute weapon_type based on a human-readable
        format of the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Warrior.set_weapon_type(weapon_type_to_be_set)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.
          [in] weapon_type_to_be_set String that contains the weapon to assign
                                     to the warrior.

        Returns
        -------

        Exceptions
        ----------
          TypeError If the parameter weapon_type_to_be_set is NOT a String.

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.set_weapon_type("Sword")
        """
        if isinstance(weapon_type_to_be_set, WeaponType):
            self._weapon_type = weapon_type_to_be_set
            self.set_attack_rating(weapon_type_to_be_set.value)
        else:
            raise TypeError("The parameter weapon_type_to_be_set should be a String.")


    def set_attack_rating(self, attack_rating_to_be_set):
        """Method to set the attribute attack_rating of the object.

        Method to set the attribute attack_rating based on a human-readable
        format of the object that is formed in this class.

        Syntax
        ------
          [ ] = obj_Warrior.set_attack_rating( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.
          [in] attack_rating_to_be_set String that contains the attack rating
                                       to assign to the warrior.

        Returns
        -------

        Exceptions
        ----------
          TypeError If the parameter attack_rating_to_be_set is NOT a int.
          ValueError If the parameter attack_rating_to_be_set is NOT > 0 and <= 10.

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.set_attack_rating(8)
        """
        if isinstance(attack_rating_to_be_set, int):
            if 1 <= attack_rating_to_be_set <= 10:
                self._attack_rating = attack_rating_to_be_set
            else:
                raise ValueError("The parameter attack_rating_to_be_set should be > 0 and <= 10.")
        else:
            raise TypeError("The parameter attack_rating_to_be_set should be a int.")


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
        print("The warrior " + str(self) + " take a swing at the warrior " +
              str(warrior_to_attack) + ".")

        points_of_damage = self._attack_rating

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

        if points_of_damage > self._defense_rating:
            self._health_points = self._health_points - (points_of_damage - self._defense_rating)
            warrior_hit = True
        else:
            print("No damage received.")
            warrior_hit = False

        # Normalizing the defeat of the warrior.
        if self._health_points < 1:
            self._health_points = 0

        return warrior_hit


    def is_alive(self):
        """Method to know if the warrior is alive.

        Method to know if a warrior is still alive based on the value of the
        attribute health_points.

        Syntax
        ------
          [ ] = obj_Warrior.is_alive( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.

        Returns
        -------
          Boolean True if the warrior is alive. False otherwise.

        Exceptions
        ----------

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.is_alive( )
        """
        return not bool(self._health_points == 0)


    def __del__(self):
        """Method to execute when a warrior is deleted


        Syntax
        ------
          [ ] = __del__( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.


        Exceptions
        ----------

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.__del__( )
        """
        Warrior.__list_ids.remove(self._id)

    def __str__(self):
        """Method to present a human-readable format of the object.

        Method to present a human-readable format of the object that is formed
        in this class. This method is useful for logging or displaying some
        information about the object.

        Syntax
        ------
          [ ] = __str__( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.

        Returns
        -------
          String Human-readable format of the object.

        Exceptions
        ----------

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.__str__( )
        """
        human_readable_string = (self._warrior_type.name +
                                 " with a " +
                                 self._weapon_type.name + " and health: " + str(self._health_points))

        return human_readable_string

    def __repr__(self):
        """Method to present an abbreviated human-readable format of the object.

        Method to present a human-readable format of the object that is formed
        in this class. This method is useful for logging or displaying some
        information about the object.

        Syntax
        ------
          [ ] = __repr__( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Warrior.

        Returns
        -------
          String Human-readable format of the object.

        Exceptions
        ----------

        Example
        -------
          >>> from warrior import Warrior
          >>> obj_Warrior = Warrior()
          >>> obj_Warrior.__repr__( )
        """
        human_readable_string = (str(self._id) + "\t" + self._warrior_type.name +
                                 "\t" +
                                 self._weapon_type.name)

        return human_readable_string

def main():
    """Function main of the module.

    The function main of this module is used to test the Class Warrior.

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
    warrior1 = Warrior(1,WarriorType.GLADIATOR, WeaponType.SWORD, 100, 8, 9)

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


    print("=================================================================.")
    print("Test Case 2: Human-readable format of the object.")
    print("=================================================================.")
    warrior2 = Warrior(2,WarriorType.GLADIATOR, WeaponType.SWORD, 100, 7, 10)

    if str(warrior2) == "GLADIATOR with a SWORD and health: 100":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__()." + " RESULT: " + str(warrior2))


    print("=================================================================.")
    print("Test Case 3: Warrior alive?¿?.")
    print("=================================================================.")
    warrior3 = Warrior(3,WarriorType.UFC, WeaponType.KICK, 97, 8, 9)

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
    warrior4 = Warrior(4,WarriorType.MMA, WeaponType.ELBOW, 93, 9, 6)

    warrior4.fight_defense(70)

    if warrior4.get_health_points() == 29:
        print("Test PASS. The method fight_defense() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method fight_defense().")


    print("=================================================================.")
    print("Test Case 5: Check the attack during a Fight.")
    print("=================================================================.")
    warrior5 = Warrior(5,WarriorType.BOXER, WeaponType.PUNCH, 99, 10, 7)
    warrior6 = Warrior(6,WarriorType.BOXER, WeaponType.PUNCH, 99, 9, 8)

    warrior_hit = warrior5.fight_attack(warrior6)

    if warrior_hit:
        if warrior6.get_health_points() == 97:
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
