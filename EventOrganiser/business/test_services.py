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
        repo = PersonRepo(Validator(), [self.person])
        self.service = PersonService(repo)

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


class TestCaseEventService(unittest.TestCase):
    def setUp(self):
        date = Date("1", "street", "2000")
        self.event = Event("id", date, "duration", "description")
        repo = EventRepo(Validator(), [self.event])
        self.service = EventService(repo)

    def test_add_event(self):
        self.assertRaises(NotEventException, self.service.add_event, 123)
        self.service.repo.items = []
        self.service.add_event(self.event)
        self.assertIn(self.event, self.service.repo.items)

    def test_delete_event(self):
        self.assertRaises(NoFieldWithValueException, self.service.delete_event, "ceva", "altceva")
        self.service.delete_event("id", "id")
        self.assertNotIn(self.event, self.service.repo.items)
        self.assertRaises(EmptyRepoException, self.service.delete_event, "id", "id")

    def test_modify_event(self):
        event2 = Event("id2", Date("2", "month2", "2001"), "duration2", "description2")
        self.assertRaises(NoFieldWithValueException, self.service.modify_event, "ceva", "ceva", event2)
        self.assertRaises(NotEventException, self.service.modify_event, "id", "id", 123)
        self.service.modify_event("id", "id", event2)
        self.assertIn(event2, self.service.repo.items)
        self.service.repo.items = []
        self.assertRaises(EmptyRepoException, self.service.modify_event, "id", "id", event2)

    def test_generate_random_events(self):
        self.service.repo.items = []
        self.assertRaises(NotIntParameterException, self.service.generate_random_events, "ceva")
        self.service.generate_random_events(2)
        self.assertEqual(len(self.service.repo.items), 2)


class TestCaseAttendanceService(unittest.TestCase):
    def setUp(self):
        address = Address("city", "street", "number")
        self.person1 = Person("id1", "name1", address)
        self.person2 = Person("id2", "name2", address)
        date = Date("1", "street", "2000")
        self.event1 = Event("id1", date, "duration1", "description1")
        self.event2 = Event("id2", date, "duration2", "description2")
        self.attendance1 = Attendance("1", self.person1.id, self.event1.id)
        self.attendance2 = Attendance("2", self.person2.id, self.event1.id)
        self.attendance3 = Attendance("3", self.person2.id, self.event2.id)
        repo = AttendanceRepo(Validator(), [self.attendance1])
        self.service = AttendanceService([self.person1, self.person2], [self.event1, self.event2], repo)

    def test_add_attendance(self):
        self.service.add_attendance(self.attendance2)
        self.assertIn(self.attendance2, self.service.repo.items)
        self.attendance3.person_id = "id3"
        self.assertRaises(InvalidAttendanceDataException, self.service.add_attendance, self.attendance3)
        self.attendance3.event_id = "id3"
        self.assertRaises(InvalidAttendanceDataException, self.service.add_attendance, self.attendance3)

    def test_get_ordered_events_attended_by_person(self):
        self.service.repo = AttendanceRepo(Validator(), [self.attendance1, self.attendance2, self.attendance3])
        self.assertRaises(NotStringParameterException, self.service.get_ordered_events_attended_by_person, 123)
        self.assertEqual(self.service.get_ordered_events_attended_by_person(self.person2.id),
                         [self.event1, self.event2])
        self.service.repo.items = []
        self.assertRaises(EmptyRepoException, self.service.get_ordered_events_attended_by_person, self.person1)

    def test_get_persons_attending_most_events(self):
        self.service.repo.items = []
        self.assertRaises(EmptyRepoException, self.service.get_persons_attending_most_events)
        self.service.repo.items = [self.attendance1, self.attendance2, self.attendance3]
        self.assertEqual(self.service.get_persons_attending_most_events(), [self.person2])

    def test_get_persons_attending_least_events(self):
        self.service.repo.items = []
        self.assertRaises(EmptyRepoException, self.service.get_persons_attending_least_events)
        self.service.repo.items = [self.attendance1, self.attendance2, self.attendance3]
        self.assertEqual(self.service.get_persons_attending_least_events(), [self.person1])

    def test_first_20percent_events_with_most_attendees(self):
        self.service.repo.items = []
        self.assertRaises(EmptyRepoException, self.service.first_20percent_events_with_most_attendees)
        self.service.repo.items = [self.attendance1, self.attendance2, self.attendance3]
        self.assertEqual(self.service.first_20percent_events_with_most_attendees(), [])

if __name__ == '__main__':
    unittest.main()
