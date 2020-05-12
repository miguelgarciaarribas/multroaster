import unittest

from generator import generateLetters
from multiconfig import *
from operation import Letters


class TestGenerateLetters(unittest.TestCase):
    def test_generate_letters(self):
        """
        Test the differnt combos to generate letters
        """
        self.numbers = '0123456789'
        self.consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTU'
        self.vowels = 'aeiouAEIOU'
        config = MultiConfig()
        config.resetConfig()
        config.operations[OperationType.DottedLetter] = 50
        config.includeDottedLetters = True

        res = generateLetters(config)
        self.assertNotPresent(res, '-') # initialization char
        self.assertNotInRange(res, self.numbers) # only letters
        self.assertPairInOrder(res)

        config.includeDottedNumbers = True
        config.includeDottedLetters = False
        res = generateLetters(config)

        self.assertNotPresent(res, '-') # initialization char
        self.assertNotInRange(res, self.vowels) # Only numbers
        self.assertNotInRange(res, self.consonants)

        config.includeDottedNumbers = False
        config.includeDottedLetters = False
        res = generateLetters(config)

        self.assertNotPresent(res, '-') # initialization char
        self.assertNotInRange(res, self.numbers) # Only letters
        self.assertPairInOrder(res)



    def assertNotPresent(self, letters, character):
        for letter in letters:
            self.assertNotEqual(letter.first, character)
            self.assertNotEqual(letter.second, character)

    def assertNotInRange(self, letters, letterRange):
        for letter in letters:
            self.assertFalse(letter.first in letterRange,
                             letter.first + ' not in ' + letterRange)
            self.assertFalse(letter.second in letterRange,
                             letter.second + ' not in ' + letterRange)

    def assertPairInOrder(self, letters):
        for letter in letters:
            self.assertTrue(letter.first in self.consonants,
                            letter.first + ' not in ' + self.consonants)
            self.assertTrue(letter.second in self.vowels,
                            letter.first + ' not in ' + self.vowels)



if __name__ == '__main__':
    unittest.main()
