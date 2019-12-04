import unittest
from EventOrganiser.domain.entities import Command, Entity


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
        d = { "id": "id" }
        self.assertEqual(self.entity.to_json(), d)


if __name__ == '__main__':
    unittest.main()
