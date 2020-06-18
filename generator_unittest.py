import unittest

from generator import generateLetters, generateTimes
from multiconfig import *
from operation import Letters


class TestGenerateLetters(unittest.TestCase):
    def test_generate_letters(self):
        """
        Test the differnt combos to generate letters
        """
        self.numbers = '0123456789'
        self.consonants = 'bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'
        self.vowels = 'aeiouAEIOU'
        config = MultiConfig()
        config.resetConfig()
        config.filterBy = [Category.EarlyYears, Category.Primary]
        config.operations[OperationType.DottedLetter] = 50
        config.includeDottedLetters = True

        res = generateLetters(config)
        self.assertNotPresent(res, '-') # initialization char
        self.assertNotInRange(res, self.numbers) # only letters
        self.assertInOrder(res)
        self.assertEqual(len(res), 50)

        config.includeDottedNumbers = True
        config.includeDottedLetters = False
        res = generateLetters(config)

        self.assertNotPresent(res, '-') # initialization char
        self.assertNotInRange(res, self.vowels) # Only numbers
        self.assertNotInRange(res, self.consonants)
        self.assertEqual(len(res), 50)

        config.includeDottedNumbers = False
        config.includeDottedLetters = False
        res = generateLetters(config)

        self.assertNotPresent(res, '-') # initialization char
        self.assertNotInRange(res, self.numbers) # Only letters
        self.assertInOrder(res)
        self.assertEqual(len(res), 50)

    def test_generate_times(self):
        config = MultiConfig()
        config.resetConfig()
        config.operations[OperationType.Time] = 50
        config.filterBy = [Category.EarlyYears, Category.Primary]
        config.deltaToTimes = False
        res = generateTimes(config)
        self.assertNoDeltas(res)
        self.assertEqual(len(res), 50)
        config.digitalTime = True
        res = generateTimes(config)
        self.assertEqual(len(res), 50)

    def assertNoDeltas(self, times):
        for time in times:
            self.assertEqual(time.delta, 0)

    def assertNotPresent(self, letters, character):
        for letter in letters:
            for char in letter.first:
                self.assertNotEqual(char, character)

    def assertNotInRange(self, letters, letterRange):
        for letter in letters:
            for char in letter.first:
                self.assertFalse(char in letterRange,
                                 char + ' not in ' + letterRange)

    def assertInOrder(self, letters):
        for letter in letters:
            self.assertTrue(letter.first[0] in self.consonants,
                            letter.first[0] + ' not in ' + self.consonants)
            self.assertTrue(letter.first[1] in self.vowels,
                            letter.first[1] + ' not in ' + self.vowels)



if __name__ == '__main__':
    unittest.main()
