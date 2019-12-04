import unittest
from EventOrganiser.domain.exceptions import NotInRepoException, NoFieldWithValueException, EmptyRepoException
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


class TestCasePersonRepo(unittest.TestCase):
    def setUp(self):
        self.person = Person("id", "name", Address("city", "street", "number"))
        self.repo = PersonRepo([self.person])

    def test_get_person_whit_field_value(self):
        self.assertEqual(self.repo.get_person_with_field_value("id", "id"), self.person)
        self.assertEqual(self.repo.get_person_with_field_value("street", "street"), self.person)
        self.assertRaises(NoFieldWithValueException, self.repo.get_person_with_field_value, "id", "no")
        self.assertRaises(NoFieldWithValueException, self.repo.get_person_with_field_value, "no", "id")
        self.assertRaises(NoFieldWithValueException, self.repo.get_person_with_field_value, "address", "no")
        self.repo.items = []
        self.assertRaises(EmptyRepoException, self.repo.get_person_with_field_value, "any", "any")


class TestCaseEventRepo(unittest.TestCase):
    def setUp(self):
        self.event = Event("id", Date("12", "month", "2019"), "duration", "description")
        self.repo = EventRepo([self.event])

    def test_get_event_whit_field_value(self):
        self.assertEqual(self.repo.get_event_with_field_value("id", "id"), self.event)
        self.assertEqual(self.repo.get_event_with_field_value("month", "month"), self.event)
        self.assertRaises(NoFieldWithValueException, self.repo.get_event_with_field_value, "id", "no")
        self.assertRaises(NoFieldWithValueException, self.repo.get_event_with_field_value, "no", "id")
        self.assertRaises(NoFieldWithValueException, self.repo.get_event_with_field_value, "date", "no")
        self.repo.items = []
        self.assertRaises(EmptyRepoException, self.repo.get_event_with_field_value, "any", "any")


if __name__ == '__main__':
    unittest.main()
