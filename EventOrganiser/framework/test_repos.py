import unittest
from EventOrganiser.domain.exceptions import *
from EventOrganiser.framework.repos import Repo, ModifiableRepo, PersonRepo, EventRepo, AttendanceRepo
from EventOrganiser.domain.entities import Entity, Person, Event, Attendance
from EventOrganiser.domain.fields import Address, Date
from EventOrganiser.framework.validators import Validator


class TestCaseRepo(unittest.TestCase):
    def setUp(self):
        self.entity = Entity("id")
        self.repo = Repo([self.entity])

    def test_index_of(self):
        self.assertEqual(self.repo.index_of(self.entity), 0)
        self.assertRaises(NotInRepoException, self.repo.index_of, Entity("otherId"))

    def test_is_empty(self):
        self.repo = Repo([])
        self.assertTrue(self.repo.is_empty())


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
        self.assertRaises(NotInRepoException, self.repo.delete, self.entity)

    def test_modify(self):
        e = Entity("otherId")
        self.repo.modify(self.entity, e)
        self.assertIn(e, self.repo.items)
        self.assertNotIn(self.entity, self.repo.items)
        self.assertRaises(NotInRepoException, self.repo.modify, self.entity, e)


class TestCasePersonRepo(unittest.TestCase):
    def setUp(self):
        validator = Validator()
        self.person = Person("id", "name", Address("city", "street", "number"))
        self.repo = PersonRepo(validator, [self.person])

    def test_get_person_whit_field_value(self):
        self.assertEqual(self.repo.get_person_with_field_value("id", "id"), self.person)
        self.assertEqual(self.repo.get_person_with_field_value("street", "street"), self.person)
        self.assertRaises(NoFieldWithValueException, self.repo.get_person_with_field_value, "id", "no")
        self.assertRaises(NoFieldWithValueException, self.repo.get_person_with_field_value, "no", "id")
        self.assertRaises(NoFieldWithValueException, self.repo.get_person_with_field_value, "address", "no")
        self.repo.items = []
        self.assertRaises(EmptyRepoException, self.repo.get_person_with_field_value, "any", "any")

    def test_get_persons(self):
        self.assertEqual(self.repo.get_persons("id", "id"), [self.person])


class TestCaseEventRepo(unittest.TestCase):
    def setUp(self):
        validator = Validator()
        self.event = Event("id", Date("12", "month", "2019"), "duration", "description")
        self.repo = EventRepo(validator, [self.event])

    def test_get_event_whit_field_value(self):
        self.assertEqual(self.repo.get_event_with_field_value("id", "id"), self.event)
        self.assertEqual(self.repo.get_event_with_field_value("month", "month"), self.event)
        self.assertRaises(NoFieldWithValueException, self.repo.get_event_with_field_value, "id", "no")
        self.assertRaises(NoFieldWithValueException, self.repo.get_event_with_field_value, "no", "id")
        self.assertRaises(NoFieldWithValueException, self.repo.get_event_with_field_value, "date", "no")
        self.repo.items = []
        self.assertRaises(EmptyRepoException, self.repo.get_event_with_field_value, "any", "any")

    def test_get_events(self):
        self.assertEqual(self.repo.get_events("id", "id"), [self.event])


class TestCaseAttendanceRepo(unittest.TestCase):
    def setUp(self):
        validator = Validator()
        self.person = Person("id", "name", Address("city", "street", "number"))
        event = Event("id", Date("12", "month", "2019"), "duration", "description")
        self.attendance = Attendance("id", "id", "id")
        self.repo = AttendanceRepo(validator, [self.attendance])

    def test_get_free_id(self):
        self.assertEqual(self.repo.get_free_id(), 1)

    def test_get_attendances_with_person_id(self):
        self.assertIn(self.attendance, self.repo.get_attendances_with_person_id(self.person.id))
        self.assertRaises(NotStringParameterException, self.repo.get_attendances_with_person_id, 123)
        self.repo.items = []
        self.assertRaises(EmptyRepoException, self.repo.get_attendances_with_person_id, self.person)

    def test_get_persons_attendances_counts(self):
        self.assertEqual(self.repo.get_persons_attendances_counts(), {"id": 1})
        self.repo.items = []
        self.assertEqual(self.repo.get_persons_attendances_counts(), {})

    def test_get_events_attendances_count(self):
        self.assertEqual(self.repo.get_events_attendances_count(), {"id": 1})
        self.repo.items = []
        self.assertEqual(self.repo.get_events_attendances_count(), {})


if __name__ == '__main__':
    unittest.main()
