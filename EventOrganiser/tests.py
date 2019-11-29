from EventOrganiser.business.services import PersonService, EventService, AttendanceService
from EventOrganiser.domain.entities import Person, Event, Entity, Attendance
from EventOrganiser.domain.fields import Address, Date
from EventOrganiser.framework.repos import Repo, PersonRepo, EventRepo, AttendanceRepo
from EventOrganiser.framework.validators import Validator


class Tests:

    class ServicesTests:

        def run_all(self):
            self.person_service()

        def person_service(self):

            def add_person():
                validator = Validator()
                pers_repo = PersonRepo([])
                pers_service = PersonService(validator, pers_repo)
                person1 = Person("1", "vasile", Address("cluj", "republicii", "23A"))
                person2 = Person("2", "andrei", Address("cluj", "republicii", "23A"))
                person3 = Person("3", "ghita", Address("cluj", "republicii", "23A"))

                pers_service.add_person(person1)
                assert pers_service.repo.items[0] == person1

            def modify_person():
                validator = Validator()
                pers_repo = PersonRepo([])
                pers_service = PersonService(validator, pers_repo)
                person1 = Person("1", "vasile", Address("cluj", "republicii", "23A"))
                person2 = Person("2", "andrei", Address("cluj", "republicii", "23A"))
                person3 = Person("3", "ghita", Address("cluj", "republicii", "23A"))

                pers_service.add_person(person1)
                pers_service.add_person(person2)
                pers_service.modify_person("id", "2", person3)
                assert pers_service.repo.items[1] == person3

            def search_person():
                validator = Validator()
                pers_repo = PersonRepo([])
                pers_service = PersonService(validator, pers_repo)
                person1 = Person("1", "vasile", Address("cluj", "republicii", "23A"))
                person2 = Person("2", "andrei", Address("cluj", "republicii", "23A"))
                person3 = Person("3", "ghita", Address("cluj", "republicii", "23A"))

                pers_service.add_person(person1)
                pers_service.add_person(person2)
                assert pers_service.search_person("id", "2") == [person2]

            add_person()
            modify_person()
            search_person()

        def events_service(self):

            def add_event():
                validator = Validator()
                events_repo = EventRepo([])
                events_service = EventService(validator, events_repo)
                event1 = Event("1", Date("2", "april", "2019"), "23", "nice party")
                event2 = Event("2", Date("2", "march", "2019"), "AFDB", "nice party")
                event3 = Event("3", Date("2", "5", "2020"), "aefb", "nice party")
                events_service.add_event(event1)
                assert events_service.repo.items[0] == event1

            def modify_event():
                validator = Validator()
                events_repo = EventRepo([])
                events_service = EventService(validator, events_repo)
                event1 = Event("1", Date("2", "april", "2019"), "23", "nice party")
                event2 = Event("2", Date("2", "march", "2019"), "AFDB", "nice party")
                event3 = Event("3", Date("2", "5", "2020"), "aefb", "nice party")
                events_service.add_event(event1)
                events_service.add_event(event2)
                events_service.modify_event("id", "2", event3)
                assert events_service.repo.items[1] == event3

            def search_event():
                validator = Validator()
                events_repo = EventRepo([])
                events_service = EventService(validator, events_repo)
                event1 = Event("1", Date("2", "april", "2019"), "23", "nice party")
                event2 = Event("2", Date("2", "march", "2019"), "AFDB", "nice party")
                event3 = Event("3", Date("2", "5", "2020"), "aefb", "nice party")
                events_service.add_event(event1)
                events_service.add_event(event2)
                assert events_service.search_event("id", "2") == event3

            def generate_random_events():
                validator = Validator()
                events_repo = EventRepo([])
                events_service = EventService(validator, events_repo)
                event1 = Event("1", Date("2", "april", "2019"), "23", "nice party")
                event2 = Event("2", Date("2", "march", "2019"), "AFDB", "nice party")
                event3 = Event("3", Date("2", "5", "2020"), "aefb", "nice party")

                events_service.generate_random_events(2)
                assert len(events_service.repo.items) != 0

            add_event()
            modify_event()
            search_event()
            generate_random_events()

        def attendance_service(self):

            def add_attendance():
                valid = Validator()
                at_repo = AttendanceRepo([])
                at_service = AttendanceService(valid, at_repo)
                person1 = Person("1", "vasile", Address("cluj", "republicii", "23A"))
                event1 = Event("1", Date("2", "april", "2019"), "23", "nice party")
                attendance1 = Attendance("1", person1, event1)

                at_service.add_attendance(attendance1)
                assert at_service.repo.items == attendance1

            def get_ordered_events_attended_by_person():
                valid = Validator()
                at_repo = AttendanceRepo([])
                at_service = AttendanceService(valid, at_repo)
                person1 = Person("1", "vasile", Address("cluj", "republicii", "23A"))
                event1 = Event("1", Date("2", "april", "2019"), "23", "nice party")
                attendance1 = Attendance("1", person1, event1)

                at_service.add_attendance(attendance1)
                assert at_service.get_ordered_events_attended_by_person(person1) == [event1]

            def persons_attending_most_events():
                valid = Validator()
                at_repo = AttendanceRepo([])
                at_service = AttendanceService(valid, at_repo)
                person1 = Person("1", "vasile", Address("cluj", "republicii", "23A"))
                event1 = Event("1", Date("2", "april", "2019"), "23", "nice party")
                attendance1 = Attendance("1", person1, event1)

                at_service.add_attendance(attendance1)
                assert at_service.persons_attending_most_events() == [person1]

            def first_20percent_events_with_most_attendees():
                valid = Validator()
                at_repo = AttendanceRepo([])
                at_service = AttendanceService(valid, at_repo)
                person1 = Person("1", "vasile", Address("cluj", "republicii", "23A"))
                event1 = Event("1", Date("2", "april", "2019"), "23", "nice party")
                attendance1 = Attendance("1", person1, event1)

                at_service.add_attendance(attendance1)
                assert at_service.first_20percent_events_with_most_attendees() == []

            def persons_with_fewest_attendances():
                valid = Validator()
                at_repo = AttendanceRepo([])
                at_service = AttendanceService(valid, at_repo)
                person1 = Person("1", "vasile", Address("cluj", "republicii", "23A"))
                event1 = Event("1", Date("2", "april", "2019"), "23", "nice party")
                attendance1 = Attendance("1", person1, event1)

                at_service.add_attendance(attendance1)
                assert at_service.persons_attending_most_events() == [person1]

            add_attendance()
            get_ordered_events_attended_by_person()
            persons_attending_most_events()
            first_20percent_events_with_most_attendees()
            persons_with_fewest_attendances()


    class EntitiesTests:

        def run_all(self):
            self.person_has_field_with_value()
            self.event_has_field_with_value()

        def person_has_field_with_value(self):
            person = Person("1", "vasile", Address("cluj", "republicii", "23A"))
            assert person.has_field_with_value("name", "vasile") is True
            assert person.has_field_with_value("city", "cluj") is True
            assert person.has_field_with_value("address", "cluj") is False
            assert person.has_field_with_value("number", "24") is False

        def event_has_field_with_value(self):
            event = Event("1", Date("2", "march", "2019"), "2:35", "nice party")
            assert event.has_field_with_value("id", "1") is True
            assert event.has_field_with_value("month", "march") is True
            assert event.has_field_with_value("date", "2019") is False
            assert event.has_field_with_value("description", "bad party") is False

    class ReposTests:

        person = Person("1", "vasile", Address("cluj", "republicii", "23A"))
        event = Event("1", Date("2", "march", "2019"), "2:35", "nice party")
        attendance = Attendance("0", person, event)

        def run_all(self):
            self.repo_add()
            self.repo_modify()
            self.pr_get_person_with_field_value()
            self.er_get_person_with_field_value()
            self.ar_get_free_id()

        def repo_add(self):
            repo = Repo([])
            repo.add(Entity("2"))
            assert not len(repo.items) == 0
            assert repo.items[0] == Entity("2")
            assert not repo.items[0] == Entity("3")

        def repo_modify(self):
            repo = Repo([Entity("2")])
            repo.modify(Entity("2"), Entity("3"))
            assert len(repo.items) == 1
            assert repo.items[0] == Entity("3")
            assert not repo.items[0] == Entity("2")

        def pr_get_person_with_field_value(self):
            repo = PersonRepo([self.person])
            try:
                assert repo.get_person_with_field_value("name", "vasile") == self.person
            except:
                assert False
            try:
                repo.get_person_with_field_value("ceva", "altceva")
                assert False
            except:
                assert True

        def er_get_person_with_field_value(self):
            repo = EventRepo([self.event])
            try:
                assert repo.get_event_with_field_value("day", "2") == self.event
            except:
                assert False
            try:
                repo.get_event_with_field_value("ceva", "altceva")
                assert False
            except:
                assert True

        def ar_get_free_id(self):
            repo = AttendanceRepo([])
            assert repo.get_free_id() == 0

        def ar_get_attendances_with_person(self):
            repo = AttendanceRepo([self.attendance])
            assert repo.get_attendances_with_person(self.person) == self.attendance

    class ValidatorsTests:

        def run_all(self):
            self.validate_person_from_repo()
            self.validate_event_from_repo()

        validator = Validator()
        person = Person("1", "vasile", Address("cluj", "republicii", "23A"))
        event = Event("1", Date("2", "march", "2019"), "2:35", "nice party")
        pers_repo = PersonRepo([person])
        ev_repo = EventRepo([event])

        def validate_person_from_repo(self):
            try:
                self.validator.validate_person_from_repo(self.pers_repo,
                                                         Person("2", "vasile", Address("cluj", "republicii", "23A")))
                assert True
            except:
                assert False
            try:
                self.validator.validate_person_from_repo(self.pers_repo,
                                                         Person("1", "hbv78268g2", Address("223", "republicii", "q31v")))
                assert False
            except:
                assert True

        def validate_event_from_repo(self):
            try:
                self.validator.validate_event_from_repo(self.ev_repo,
                                                         Event("2", Date("2", "march", "2019"), "2:35", "nice party"))
                assert True
            except:
                assert False
            try:
                self.validator.validate_event_from_repo(self.ev_repo,
                                                        Event("1", Date("kuac", "march", "1c"), "2:35", "nice party"))
                assert False
            except:
                assert True
    #------------------

    @property
    def services_tests(self):
        return self._services_tests
    @services_tests.setter
    def services_tests(self, value):
        self._services_tests = value

    @property
    def repos_tests(self):
        return self._repos_tests
    @repos_tests.setter
    def repos_tests(self, value):
        self._repos_tests = value

    @property
    def entities_tests(self):
        return self._entities_tests
    @entities_tests.setter
    def entities_tests(self, value):
        self._entities_tests = value

    @property
    def validators_tests(self):
        return self._validators_tests
    @validators_tests.setter
    def validators_tests(self, value):
        self._validators_tests = value

    #------------------

    def __init__(self):
        self.services_tests = self.ServicesTests()
        self.repos_tests = self.ReposTests()
        self.entities_tests = self.EntitiesTests()
        self.validators_tests = self.ValidatorsTests()

    #------------------

    def run_all(self):
        self.services_tests.run_all()
        self.repos_tests.run_all()
        self.entities_tests.run_all()
        self.validators_tests.run_all()
