import unittest

from operation import Time


class TestSum(unittest.TestCase):
    def test_time(self):
        """
        Test the sum calculation algorithm
        """
        sut = Time(3, 35, 5, '-')
        self.assertEqual(sut.calculate(), '03 : 30')
        sut = Time(3, 20, 25, '-')
        self.assertEqual(sut.calculate(), '02 : 55')
        sut = Time(5, 50, 35, '+')
        self.assertEqual(sut.calculate(), '06 : 25')
        sut = Time(11, 45, 16, '+')
        self.assertEqual(sut.calculate(), '12 : 01')
        sut = Time(12, 45, 50, '-')
        self.assertEqual(sut.calculate(), '11 : 55')


if __name__ == '__main__':
    unittest.main()
