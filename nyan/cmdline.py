#! -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import argparse

from nyan.cat import Cat, Sexes


def main():
    """Main function that is called when the package is used as a CLI tool
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-b",
                        "--breed",
                        type=str,
                        required=True,
                        help="breed of your cat")

    parser.add_argument("-n",
                        "--name",
                        type=str,
                        required=True,
                        help="name of your cat")

    parser.add_argument("-a",
                        "--age",
                        type=int,
                        required=True,
                        help="age of your cat")

    parser.add_argument("-s",
                        "--sex",
                        type=str,
                        choices=[sex.value for sex in list(Sexes)],
                        required=True,
                        help="sex of your cat")

    args = parser.parse_args()

    cat = Cat(breed=args.breed,
              name=args.name,
              age=args.age,
              sex=Sexes(args.sex))
    print(cat.admire())

    sys.exit()
