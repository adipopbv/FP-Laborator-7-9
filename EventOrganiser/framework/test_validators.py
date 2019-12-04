import unittest
from EventOrganiser.domain.entities import Person, Event, Attendance
from EventOrganiser.domain.exceptions import *
from EventOrganiser.domain.fields import Address, Date
from EventOrganiser.framework.repos import PersonRepo, EventRepo
from EventOrganiser.framework.validators import Validator


class TestCaseValidator(unittest.TestCase):
    def setUp(self):
        self.validator = Validator()

    def test_validate_person(self):
        p = Person("id", 1234, Address("5678", "street", "number"))
        self.assertRaises(InvalidPersonDataException, self.validator.validate_person, p)

    def test_validate_person_from_repo(self):
        p = Person("id", 1234, Address("5678", "street", "number"))
        pr = PersonRepo([])
        self.assertRaises(InvalidPersonDataException, self.validator.validate_person_from_repo, pr, p)
        pr = PersonRepo([p])
        self.assertRaises(ExistentIdException, self.validator.validate_person_from_repo, pr, p)

    def test_validate_event(self):
        e = Event("id", Date([], "street", "year"), "duration", "description")
        self.assertRaises(InvalidEventDataException, self.validator.validate_event, e)

    def test_validate_event_from_repo(self):
        e = Event("id", Date([], "street", "year"), "duration", "description")
        er = EventRepo([])
        self.assertRaises(InvalidEventDataException, self.validator.validate_event_from_repo, er, e)
        er = EventRepo([e])
        self.assertRaises(ExistentIdException, self.validator.validate_event_from_repo, er, e)

    def test_validate_attendance(self):
        p = Person("id", 1234, Address("5678", "street", "number"))
        e = Event("id", Date([], "street", "year"), "duration", "description")
        a = Attendance("id", p, e)
        self.assertRaises(InvalidAttendanceDataException, self.validator.validate_attendance, a)


if __name__ == '__main__':
    unittest.main()
