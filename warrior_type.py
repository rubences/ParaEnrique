#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
This Python module contains not only the Enum WarriorType, but also the test of
this Python class.

@contents :  This module contains not only a single Python class, but also the
             test cases to probe its functionality.
@project :  N/A
@program :  N/A
@file :  warrior_type.py
@author :  Antonio Artes Garcia (antonio.artesgarcia@ceu.es)
           Alberto Gil De la Fuente (alberto.gildelafuente@ceu.es)

@version :  0.0.1, 08 January 2021
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
from enum import Enum


class WarriorType(Enum):
    """Python class to implement an enumeration for the attribute Warrior Type.

    This Python class implements an enumeration for the attribute Warrior Type.

    Syntax
    ------
      obj = WarriorType.Enum

    Parameters
    ----------

    Returns
    -------
      obj Python object output parameter that represents an instance
          of the class WarriorType.

    Attributes
    ----------

    Example
    -------
      >>> from warrior_type import WarriorType
      >>> obj_WarriorType = WarriorType.Boxer
    """
    BOXER = 1
    GLADIATOR = 2
    UFC = 3  # Ultimate Fighting Championship
    MMA = 4  # Mixed martial arts

    def __str__(self):
        return self.name

    @staticmethod
    def from_str(strWarriorType):
        strWarriorType = strWarriorType.lower()
        if strWarriorType == 'boxer':
            return WarriorType.BOXER
        elif strWarriorType == 'gladiator':
            return WarriorType.GLADIATOR
        elif strWarriorType == 'ufc':
            return WarriorType.UFC
        elif strWarriorType == 'mma':
            return WarriorType.MMA
        else:
            raise TypeError("The str " + strWarriorType + " does not correspond with a warrior Type")

def main():
    """Function main of the module.

    The function main of this module is used to test the Class WarriorType.

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
    print("Test Case 1: Check Class WarriorType.")
    print("=================================================================.")

    if isinstance(WarriorType.BOXER, WarriorType):
        print("Test PASS. The enum for Boxer has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WarriorType.GLADIATOR, WarriorType):
        print("Test PASS. The enum for Gladiator has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WarriorType.UFC, WarriorType):
        print("Test PASS. The enum for UFC has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")

    if isinstance(WarriorType.MMA, WarriorType):
        print("Test PASS. The enum for MMA has been correctly set.")
    else:
        print("Test FAIL. Check the method __init__().")


# Checking whether this module is executed just itself alone.
if __name__ == "__main__":
    main()


# EOF
