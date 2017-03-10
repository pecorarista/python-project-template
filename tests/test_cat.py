# -*- encoding: utf-8 -*-

from __future__ import unicode_literals

import unittest

from nyan.cat import Cat, Sexes


class TestCat(unittest.TestCase):

    def setUp(self):
        self.luna = Cat(name='Luna',
                        breed='Russian Blue',
                        sex=Sexes.FEMALE,
                        age=7)

        self.tom = Cat(name='Tom',
                       breed='Abyssinian',
                       sex=Sexes.MALE,
                       age=6)

    def test_add_age(self):
        self.luna.add_age()
        self.assertEqual(self.luna.age, 8)

    def test_praise(self):

        self.assertEqual(self.luna.praise().split('\n')[1],
                         'She is a Russian Blue.')

        self.assertEqual(self.tom.praise().split('\n')[1],
                         'He is an Abyssinian.')


if __name__ == '__main__':
    unittest.main()
