#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the class Coach, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  coach.py
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
from warrior import Warrior


class Coach:
    """Python class to implement a Coach which owns a set of warriors in the Game.

    This Python class implements a coach of the Game. Each coach owns a set of
    warriors in the Game.

    Syntax
    ------
      obj = Coach(coach_name, set_of_warriors)

    Parameters
    ----------
      [in] coach_name Name of the Coach.
      [in] set_of_warrior Set of warriors handled by the Coach.

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class Coach.

    Attributes
    ----------

    Example
    -------
      >>> from user import User
      >>> obj_Coach = Coach()
    """


    def __init__(self, coach_name, set_of_warriors):
        """Constructor of the class.

        This special method is executed when an object of this class is
        created.

        Syntax
        ------
          [ ] = __init__(self, coach_name, set_of_warriors)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class User.
          [in] coach_name Name of the Coach.
          [in] set_of_warrior Set of warriors handled by the Coach.

        Returns
        -------
          obj Python object output parameter that represents an instance
              of the class Coach.

        Exceptions
        ----------
          TypeError:
            If the parameter coach_name is NOT a String.
            If the parameter set_of_warriors is NOT a list of Warriors.
          ValueError:
            If the parameter set_of_warrior is an empty list of Warriors.

        Example
        -------
          >>> from coach import Coach
          >>> obj_Coach = Coach("Entrenador", list_warriors)
        """
        if isinstance(coach_name, str):
            self._coach_name = coach_name
        else:
            raise TypeError("The parameter coach_name should be a String.")

        self.__warriors = set_of_warriors
        if len(set_of_warriors) > 0:
            for temp_warrior in set_of_warriors:
                if not isinstance(temp_warrior, Warrior):
                    raise TypeError("The parameter temp_warrior should be a list of Warriors.")
            self.__defeated = False
        else:
            raise ValueError("The parameter set_of_warrior cannot be an empty list. " +
                             "It should be a list of Warriors.")


    def get_coach_name(self):
        """Method to get the attribute coach_name of the object.

        Method to get the attribute coach_name in a human-readable format of
        the object that is formed in this class.

        Syntax
        ------
          [ ] = get_coach_name( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Coach.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from coach import Coach
          >>> obj_Coach = Coach()
          >>> obj_Coach.get_coach_name( )
        """
        return self._coach_name


    def get_set_of_warriors(self):
        """Method to get the attribute warriors of the object.

        Method to get the attribute warriors in a human-readable format of
        the object that is formed in this class.

        Syntax
        ------
          [ ] = get_set_of_warriors( )

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Coach.

        Returns
        -------
          String The value of the specific attribute.

        Exceptions
        ----------

        Example
        -------
          >>> from coach import Coach
          >>> obj_Coach = Coach()
          >>> obj_Coach.get_set_of_warriors( )
        """
        return self.__warriors


    def is_undefeated(self):
        """Method to know if the Coach is still undefeated.

        This get method is used in order to obtain the attribute defeated. This
        attribute is to know if the Coach is still undefeated.

        Syntax
        ------
          [ ] = is_undefeated(self)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Coach.

        Returns
        -------
          Null .

        Example
        -------
          >>> from coach import Coach
          >>> obj_Coach = Coach()
          >>> obj_Coach.is_undefeated()
        """
        defeated = True

        for temp_warrior in self.__warriors:
            if temp_warrior.is_alive():
                defeated = False

        self.__defeated = defeated

        return not self.__defeated


    def surrender(self):
        """Method to surrender a Coach.

        This method is used to set the attribute defeated to the value
        True. In this way, it is possible to surrender the Coach.

        Syntax
        ------
          [ ] = surrender(self)

        Parameters
        ----------
          [in] self Python object that represents an instance of the
                    class Coach.

        Returns
        -------
          Null .

        Example
        -------
          >>> from coach import Coach
          >>> obj_Coach = Coach()
          >>> obj_Coach.surrended()
        """
        for temp_warrior in self.__warriors:
            temp_warrior._health_points = 0

        self.__defeated = True


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
                    class Coach.

        Returns
        -------
          String Human-readable format of the object.

        Exceptions
        ----------

        Example
        -------
          >>> from coach import Coach
          >>> obj_Coach = Coach()
          >>> obj_Coach.__str__( )
        """
        human_readable_string = (self._coach_name +
                                 " with " +
                                 str(len(self.__warriors)) + " warriors.")

        return human_readable_string


def main():
    """Function main of the module.

    The function main of this module is used to test the Class Coach.

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
    from warrior_type import WarriorType
    from weapon_type import WeaponType
    print("=================================================================.")
    print("Test Case 1: Create a Coach with an empty list.")
    print("=================================================================.")
    coach1_warriors = []
    try:
        coach1 = Coach("", coach1_warriors)
        print("Test FAIL. It should raise a ValueError exception. Check the method __init__() based on the object: " + str(coach1))
    except ValueError as value_error:
        print("Test PASS. The exception was raised: " + str(value_error) + " .")


    print("=================================================================.")
    print("Test Case 2: Create a Coach with a NON empty list.")
    print("=================================================================.")
    warrior1 = Warrior(1, WarriorType.BOXER, WeaponType.KICK, 99, 10, 7)
    warrior2 = Warrior(2, WarriorType.BOXER, WeaponType.KICK, 99, 9, 8)
    coach2_warriors = []
    coach2_warriors.append(warrior1)
    coach2_warriors.append(warrior2)
    try:
        coach2 = Coach("Rocky Balboa", coach2_warriors)
        print("The following coach has been generated: " + str(coach2))
        print("Test PASS. The method __init__() has been implemented correctly.")
    except ValueError as value_error:
        print("Test FAIL. Check the method __init__(): " + str(value_error))


    print("=================================================================.")
    print("Test Case 3: Human-readable format of the object.")
    print("=================================================================.")
    coach3_warriors = []
    coach3_warriors.append(warrior1)
    coach3_warriors.append(warrior2)
    coach3 = Coach("Rocky Balboa", coach3_warriors)

    if str(coach3) == "Rocky Balboa with 2 warriors.":
        print("Test PASS. The human-readable format of the object has been implemented correctly.")
    else:
        print("Test FAIL. Check the method __str__().")


    print("=================================================================.")
    print("Test Case 4: Coach undefeated?¿?.")
    print("=================================================================.")
    coach4_warriors = []
    coach4_warriors.append(warrior1)
    coach4_warriors.append(warrior2)
    coach4 = Coach("Rocky Balboa", coach3_warriors)

    if coach4.is_undefeated():
        print("Test PASS. The method is_undefeated() has been implemented correctly.")
    else:
        print("Test FAIL. Check the method is_undefeated().")

    coach4.surrender()

    if coach4.is_undefeated():
        print("Test FAIL. Check the method is_undefeated().")
    else:
        print("Test PASS. The method is_undefeated() has been implemented correctly.")


# Checking whether this script is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
