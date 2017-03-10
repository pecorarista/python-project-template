# -*- coding: utf-8 -*-

from enum import Enum, unique


@unique
class Sexes(Enum):
    FEMALE = 'female'
    MALE = 'male'
    OTHERS = 'others'


class Cat(object):
    """Class that represents a cat.

    Attributes:
        name (str): The name of the cat.
        breed (str): The breed of the cat. For example, American Shorthair,
            Abyssinian, or Russian Blue.
        sex (Sexes): The sex of the cat: FEMALE, MALE, or OTHERS.
        age (int): The age of the cat.
    """

    def __init__(self,
                 name="Chomusuke",
                 breed="Russian Blue",
                 sex=Sexes.OTHERS,
                 age=1):
        """
        Args:
            name (str, optional)
            breed (str, optional)
            sex (Sexes, optional)
            age (int, optional)
        """
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = int(age)

    def add_age(self):
        self.age += 1

    def praise(self):
        """
        Returns:
            str
        """

        pronoun = "She" if self.sex == Sexes.FEMALE else "He"
        article = "an" \
            if self.breed[0].lower() in ["a", "e", "i", "o", "u"] \
            else "a"

        lines = ["This is my cat, {}.".format(self.name),
                 "{} is {} {}.".format(pronoun, article, self.breed)]

        return '\n'.join(lines)
