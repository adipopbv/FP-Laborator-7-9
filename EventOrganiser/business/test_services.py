import unittest
from EventOrganiser.business.services import *
from EventOrganiser.framework.repos import *
from EventOrganiser.domain.exceptions import *

class TestCaseCommandService(unittest.TestCase):
    def setUp(self):
        self.command = Command("function", "description", ["key1", "key2"])
        repo = CommandRepo([self.command])
        self.service = CommandsService(repo)

    def test_get_command_with_key(self):
        self.assertEqual(self.service.get_command_with_key("key1"), self.command)
        self.assertRaises(InexistentCommandException, self.service.get_command_with_key, "someKey")


class TestCasePersonService(unittest.TestCase):
    def setUp(self):
        address = Address("city", "street", "number")
        self.person = Person("id", "name", address)
        repo = PersonRepo([self.person])
        self.service = PersonService(Validator(), repo)

    def test_add_person(self):
        self.assertRaises(NotPersonException, self.service.add_person, 123)
        self.service.repo.items = []
        self.service.add_person(self.person)
        self.assertIn(self.person, self.service.repo.items)

    def test_delete_person(self):
        self.assertRaises(NoFieldWithValueException, self.service.delete_person, "ceva", "altceva")
        self.service.delete_person("id", "id")
        self.assertNotIn(self.person, self.service.repo.items)
        self.assertRaises(EmptyRepoException, self.service.delete_person, "id", "id")

    def test_modify_person(self):
        person2 = Person("id2", "name2", Address("city2", "street2", "number2"))
        self.assertRaises(NoFieldWithValueException, self.service.modify_person, "ceva", "altceva", person2)
        self.assertRaises(NotPersonException, self.service.modify_person, "id", "id", 123)
        self.service.modify_person("id", "id", person2)
        self.assertIn(person2, self.service.repo.items)
        self.service.repo.items = []
        self.assertRaises(EmptyRepoException, self.service.modify_person, "id", "id", person2)

    def test_search_person(self):
        self.assertEqual(self.service.search_person("id", "id"), [self.person])
        self.assertEqual(self.service.search_person("id", "ceva"), [])
        self.assertEqual(self.service.search_person("ceva", "altceva"), [])


if __name__ == '__main__':
    unittest.main()
