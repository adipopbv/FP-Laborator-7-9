import unittest
from EventOrganiser.domain.exceptions import NotInRepoException
from EventOrganiser.framework.repos import Repo, ModifiableRepo, PersonRepo, EventRepo, AttendanceRepo
from EventOrganiser.domain.entities import Entity, Person, Event, Attendance
from EventOrganiser.domain.fields import Address, Date


class TestCaseRepo(unittest.TestCase):
    def setUp(self):
        self.entity = Entity("id")
        self.repo = Repo([self.entity])

    def test_index_of(self):
        self.assertEqual(self.repo.index_of(self.entity), 0)
        self.assertRaises(NotInRepoException, self.repo.index_of, Entity("otherId"))


class TestCaseModifiableRepo(unittest.TestCase):
    def setUp(self):
        self.entity = Entity("id")
        self.repo = ModifiableRepo([self.entity])

    def test_add(self):
        e = Entity("otherId")
        self.repo.add(e)
        self.assertIn(e, self.repo.items)

    def test_delete(self):
        self.repo.delete(self.entity)
        self.assertNotIn(self.entity, self.repo.items)

    def test_modify(self):
        e = Entity("otherId")
        self.repo.modify(self.entity, e)
        self.assertIn(e, self.repo.items)
        self.assertNotIn(self.entity, self.repo.items)


if __name__ == '__main__':
    unittest.main()
