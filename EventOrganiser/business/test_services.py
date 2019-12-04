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


if __name__ == '__main__':
    unittest.main()
