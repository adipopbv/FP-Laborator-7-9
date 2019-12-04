import unittest
from EventOrganiser.domain.entities import Command, Entity, Person
from EventOrganiser.domain.exceptions import NotListException
from EventOrganiser.domain.fields import Address


class TestCaseCommand(unittest.TestCase):
    def setUp(self):
        self.command = Command("function", "description", ["key1", "key2"])

    def test_to_json(self):
        d = {
            "keys": ["key1", "key2"],
            "function": "function",
            "description": "description"
        }
        self.assertEqual(self.command.to_json(), d)


class TestCaseEntity(unittest.TestCase):
    def setUp(self):
        self.entity = Entity("id")

    def test_equal(self):
        e = Entity("id")
        self.assertEqual(self.entity, e)

    def test_to_json(self):
        d = {"id": "id"}
        self.assertEqual(self.entity.to_json(), d)


class TestCasePerson(unittest.TestCase):
    def setUp(self):
        self.address = Address("city", "street", "number")
        self.person = Person("id", "name", self.address)

    def test_equal(self):
        p = Person("id", "name", Address("city", "street", "number"))
        self.assertTrue(self.person == p)

    def test_to_json(self):
        d = {
            "id": "id",
            "name": "name",
            "address": self.address.to_json()
        }
        self.assertEqual(self.person.to_json(), d)

    def test_has_field_with_value(self):
        self.assertTrue(self.person.has_field_with_value("id", "id"))
        self.assertFalse(self.person.has_field_with_value("id", "no"))
        self.assertFalse(self.person.has_field_with_value("no", "id"))
        self.assertTrue(self.person.has_field_with_value("city", "city"))
        self.assertFalse(self.person.has_field_with_value("city", "no"))
        self.assertFalse(self.person.has_field_with_value("address", "city"))

    def test_not_in_list(self):
        self.assertTrue(self.person.not_in_list([]))
        self.assertTrue(self.person.not_in_list([1, "stuff"]))
        self.assertFalse(self.person.not_in_list([self.person, 2]))
        self.assertRaises(NotListException, self.person.not_in_list, 12)


if __name__ == '__main__':
    unittest.main()
