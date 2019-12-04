import unittest
from EventOrganiser.domain.fields import Address


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


if __name__ == '__main__':
    unittest.main()
