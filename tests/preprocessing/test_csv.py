# -*- encoding: utf-8 -*-

import tempfile
import unittest

import nyan.preprocessing.csv as csv
from nyan.cat import Sexes


class TestCSV(unittest.TestCase):

    def setUp(self):
        self.lines = '\n'.join([
            '\t'.join([
                'Artemis',
                'American Shorthair',
                '2',
                'female']),
            '\t'.join([
                'Liz',
                'Siamese',
                '3',
                'male'])])

    def test_read_csv(self):

        with tempfile.NamedTemporaryFile(mode='w+') as f:
            f.write(self.lines)
            f.flush()
            cats = csv.read_csv(filename=f.name)

        self.assertEqual(cats[0].name, 'Artemis')
        self.assertEqual(cats[1].breed, 'Siamese')
        self.assertEqual(cats[0].age, 2)
        self.assertEqual(cats[0].sex, Sexes.FEMALE)
