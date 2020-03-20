import unittest
from EventOrganiser.domain.fields import Address, Date


class TestCaseAddress(unittest.TestCase):
    def setUp(self):
        self.address = Address("someCity", "someStreet", "someNumber")

    def test_to_json(self):
        d = {
            "city": "someCity",
            "street": "someStreet",
            "number": "someNumber"
        }
        self.assertEqual(self.address.to_json(), d)


class TestCaseDate(unittest.TestCase):
    def setUp(self):
        self.address = Date("08", "september", "2000")

    def test_to_json(self):
        d = {
            "day": "08",
            "month": "september",
            "year": "2000"
        }
        self.assertEqual(self.address.to_json(), d)


if __name__ == '__main__':
    unittest.main()
