import sys
import argparse

from nyan.__version__ import __version__
from nyan.cat import Cat, Sexes


def main():
    """Main function that is called when the package is used as a CLI tool
    """

    default_cat = Cat()

    parser = argparse.ArgumentParser()

    parser.add_argument("-v",
                        "--version",
                        action='store_true',
                        help="breed of your cat")

    parser.add_argument("-b",
                        "--breed",
                        type=str,
                        default=default_cat.breed,
                        help="breed of your cat")

    parser.add_argument("-n",
                        "--name",
                        type=str,
                        default=default_cat.name,
                        help="name of your cat")

    parser.add_argument("-a",
                        "--age",
                        type=int,
                        default=default_cat.age,
                        help="age of your cat")

    parser.add_argument("-s",
                        "--sex",
                        type=str,
                        default=default_cat.sex,
                        choices=[sex.value for sex in list(Sexes)],
                        help="sex of your cat")

    args = parser.parse_args()

    if args.version:
        print("Nyan version {}".format(__version__))
        sys.exit()

    args = parser.parse_args()

    cat = Cat(breed=args.breed,
              name=args.name,
              age=args.age,
              sex=Sexes(args.sex))

    print(cat.praise())


if __name__ == '__main__':
    sys.exit(main())
