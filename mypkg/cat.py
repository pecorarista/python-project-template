from enum import Enum, unique


@unique
class Sexes(Enum):
    FEMALE = 'female'
    MALE = 'male'
    OTHERS = 'others'


class Cat(object):
    """Class that represents a cat.

    Args:
        name (str, optional): The name of the cat.
        breed (str, optional): The breed of the cat. For example,
            American Shorthair, Abyssinian, or Russian Blue.
        sex (Sexes, optional): The sex of the cat: FEMALE, MALE, or OTHERS.
        age (int, optional): The age of the cat.

    Attributes:
        name (str): The name of the cat.
        breed (str): The breed of the cat.
        sex (Sexes): The sex of the cat.
        age (int): The age of the cat.
    """

    def __init__(self,
                 name="Chomusuke",
                 breed="Russian Blue",
                 sex=Sexes.OTHERS,
                 age=1):
        self.name = name
        self.breed = breed
        self.sex = sex
        self.age = int(age)

    def add_age(self):
        self.age += 1

    def praise(self):
        """Generate sentences that praise a cat.
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
