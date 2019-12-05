import unittest
from EventOrganiser.domain.exceptions import NotIntParameterException
from EventOrganiser.framework.randomization import Random


class TestCaseRandom(unittest.TestCase):
    def setUp(self):
        self.random = Random()

    def test_int_in_range(self):
        self.assertIs(type(self.random.int_in_range(0, 10)), int)
        self.assertGreaterEqual(self.random.int_in_range(0, 10), 0)
        self.assertLessEqual(self.random.int_in_range(0, 10), 10)
        self.assertRaises(NotIntParameterException, self.random.int_in_range, "dfa", [])

    def test_string_of_chr(self):
        self.assertIs(type(self.random.string_of_chr(2)), str)
        self.assertRaises(NotIntParameterException, self.random.string_of_chr, {})

    def test_string_of_int(self):
        self.assertIs(type(self.random.string_of_int(2)), str)
        self.assertRaises(NotIntParameterException, self.random.string_of_int, 2.3)


if __name__ == '__main__':
    unittest.main()
