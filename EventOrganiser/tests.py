from EventOrganiser.domain.entities import Person, Event, Entity, Attendance
from EventOrganiser.domain.fields import Address, Date
from EventOrganiser.framework.repos import Repo, PersonRepo, EventRepo, AttendanceRepo


class Tests:

    class ServicesTests:

        def run_all(self):
            self.create_adress_test()
            self.creare_person_test()
            self.add_person_to_repo_test()
            self.add_event_to_repo_test()
            self.modify_person_from_repo_test()
            self.modify_event_from_repo_test()
            self.search_person_in_repo_test()
            self.search_event_in_repo_test()

        def create_adress_test(self):
            persons = self.IdRepo()
            events = self.IdRepo()
            validator = self.Validator()
            service = self.Service(persons, events, validator)
            adress = service.create_adress("cluj", "dorobantilor", "123")
            assert adress.get_city_name().get_value() == "cluj"
            assert adress.get_street_name().get_value() == "dorobantilor"
            assert adress.get_number().get_value() == "123"

        def creare_person_test(self):
            persons = self.IdRepo()
            events = self.IdRepo()
            validator = self.Validator()
            service = self.Service(persons, events, validator)
            adress = service.create_adress("cluj", "dorobantilor", "123")
            person = service.create_person("1", "cineva", adress)
            assert person.get_id().get_value() == "1"
            assert person.get_name().get_value() == "cineva"
            assert person.get_adress().get_city_name().get_value() == "cluj"
            assert person.get_adress().get_street_name().get_value() == "dorobantilor"
            assert person.get_adress().get_number().get_value() == "123"

        def add_person_to_repo_test(self):
            persons = self.IdRepo()
            events = self.IdRepo()
            validator = self.Validator()
            service = self.Service(persons, events, validator)
            service.add_person_to_repo(persons, "1", "cineva", "cluj", "dorobantilor", "123")
            assert service.get_persons().count() == 1
            assert not service.get_persons().count() == 0

        def add_event_to_repo_test(self):
            events = self.IdRepo()
            events = self.IdRepo()
            validator = self.Validator()
            service = self.Service(events, events, validator)
            service.add_event_to_repo(events, "1", "1", "1", "2000", "02", "35", "best party")
            assert service.get_events().count() == 1
            assert not service.get_events().count() == 0

        def modify_person_from_repo_test(self):
            persons = self.IdRepo()
            events = self.IdRepo()
            validator = self.Validator()
            service = self.Service(persons, events, validator)
            person1 = service.create_person("1", "maBoi", service.create_adress("cluj", "doro", "2"))
            person2 = service.create_person("2", "yaBoi", service.create_adress("cluj-napoca", "dorobantilor", "3"))
            service.get_persons().add(person1)
            service.modify_person_from_repo(persons, "1", "2", "yaBoi", "cluj-napoca", "dorobantilor", "3")
            person = service.get_persons().get_item_with_id_value("2")
            assert person == person2
            assert not person == person1

        def modify_event_from_repo_test(self):
            persons = self.IdRepo()
            events = self.IdRepo()
            validator = self.Validator()
            service = self.Service(persons, events, validator)
            event1 = service.create_event("1", service.create_date("1", "1", "2000"), service.create_duration("3", "35"), "best party")
            event2 = service.create_event("2", service.create_date("15", "12", "2019"), service.create_duration("4", "45"), "best parteee")
            service.get_events().add(event1)
            service.modify_event_from_repo(events, "1", "2", "15", "12", "2019", "4", "45", "best parteee")
            event = service.get_events().get_item_with_id_value("2")
            assert event == event2
            assert not event == event1

        def search_person_in_repo_test(self):
            persons = self.IdRepo()
            validator = self.Validator()
            service = self.Service(persons, None, validator)
            person = service.create_person("1", "Pop", service.create_adress("bv", "ag-lui", "17"))
            service.get_persons().add(person)
            assert service.search_person_in_repo(service.get_persons(), "1") == person
            assert not service.search_person_in_repo(service.get_persons(), "1") != person

        def search_event_in_repo_test(self):
            events = self.IdRepo()
            validator = self.Validator()
            service = self.Service(None, events, validator)
            event = service.create_event("1", service.create_date("1", "1", "2019"), service.create_duration("02", "35"), "best party ever")
            service.get_events().add(event)
            assert service.search_event_in_repo(service.get_events(), "1") == event
            assert not service.search_event_in_repo(service.get_events(), "1") != event

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
            self.validate_person_test()

        def validate_person_test(self):
            validator = self.Validator()
            person = self.Person(self.Id("123"), self.Name("kajner"), self.Adress(self.CityName("hkuygdkf"), self.StreetName("knwjv"), self.Number("51")))
            repo = self.IdRepo()
            try:
                validator.validate_person(repo, person)
                assert True
            except:
                assert False
            person = self.Person(self.Id("123"), self.Name("kajner"), self.Adress(self.CityName("hkuygdkf"), self.StreetName(2314), self.Number(1)))
            repo.add(person)
            try:
                validator.validate_person(repo, person)
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
