from EventOrganiser.domain.entities import Attendance, Person, Event
from EventOrganiser.domain.fields import Date
from EventOrganiser.framework.validators import Validator


class Service:
    from EventOrganiser.framework.repos import FileRepo

    _validator: Validator
    @property
    def validator(self):
        return self._validator
    @validator.setter
    def validator(self, value):
        self._validator = value

    _repo: FileRepo
    @property
    def repo(self):
        return self._repo
    @repo.setter
    def repo(self, value):
        self._repo = value

    #------------------------

    def __init__(self, validator: Validator, repo):
        self.validator = validator
        self.repo = repo


class CommandsService(Service):
    from EventOrganiser.framework.repos import CommandFileRepo

    _repo: CommandFileRepo

    #---------------------------

    def __init__(self, commands: CommandFileRepo):
        super().__init__(None, commands)
        self.repo.load_from_json()

    def get_command_with_key(self, key_value):
        for command in self.repo.items:
            for key in command.keys:
                if key == key_value:
                    return command
        raise Exception("No command with the given key")


class PersonService(Service):
    from EventOrganiser.framework.repos import PersonFileRepo

    _repo: PersonFileRepo

    #-------------------------------------------

    def __init__(self, validator: Validator, persons: PersonFileRepo):
        super().__init__(validator, persons)
        self.repo.load_from_json()

    def add_person(self, person: Person):
        try:
            self.validator.validate_person_from_repo(self.repo, person)
            self.repo.add(person)
        except Exception as ex:
            raise Exception(ex)
        self.repo.save_to_json()

    def modify_person(self, field, field_value, modified_person):
        try:
            self.validator.validate_person(modified_person)
            self.repo.modify(self.repo.get_person_with_field_value(field, field_value), modified_person)
            self.repo.save_to_json()
        except Exception as ex:
            raise Exception(ex)

    def search_person(self, field, field_value):
        try:
            persons = [person for person in self.repo.items if person.has_field_with_value(field, field_value)]
            return persons
        except Exception as ex:
            raise Exception(ex)


class EventService(Service):
    from EventOrganiser.framework.repos import  EventFileRepo

    _repo: EventFileRepo

    #-----------------------------------------

    def __init__(self, validator: Validator, events: EventFileRepo):
        super().__init__(validator, events)
        self.repo.load_from_json()

    def add_event(self, event: Event):
        try:
            self.validator.validate_event_from_repo(self.repo, event)
            self.repo.add(event)
        except Exception as ex:
            raise Exception(ex)
        self.repo.save_to_json()

    def modify_event(self, field, field_value, modified_event):
        try:
            self.validator.validate_event(modified_event)
            self.repo.modify(self.repo.get_event_with_field_value(field, field_value), modified_event)
            self.repo.save_to_json()
        except Exception as ex:
            raise Exception(ex)

    def search_event(self, field, field_value):
        try:
            events = [event for event in self.repo.items if event.has_field_with_value(field, field_value)]
            return events
        except Exception as ex:
            raise Exception(ex)

    def generate_random_events(self, number_of_events):
        import random

        def random_str():
            string = ""
            number_of_letters = random.randrange(0, 21, 1)
            for _ in range(0, number_of_letters):
                string += chr(random.randrange(ord('A'), ord('z'), 1))
            return string

        def generate_random_event():
            try:
                event = Event(
                    random_str(),
                    Date(
                        str(random.randint(0, 10)),
                        random_str(),
                        str(random.randint(0, 10))
                    ),
                    random_str(),
                    random_str()
                )
                self.validator.validate_event_from_repo(self.repo, event)
                return event
            except:
                return generate_random_event()

        try:
            for _ in range(0, number_of_events):
                event = generate_random_event()
                self.repo.add(event)
        except Exception as ex:
            raise Exception(ex)
        self.repo.save_to_json()


class AttendanceService(Service):
    from EventOrganiser.framework.repos import  AttendanceFileRepo

    _repo: AttendanceFileRepo

    #---------------------------------------------------

    def __init__(self, validator: Validator, attendances: AttendanceFileRepo):
        super().__init__(validator, attendances)
        self.repo.load_from_json()

    def add_attendance(self, attendance: Attendance):
        try:
            self.validator.validate_attendance(attendance)
            self.repo.add(attendance)
        except Exception as ex:
            raise Exception(ex)
        self.repo.save_to_json()

    def get_ordered_events_attended_by_person(self, person: Person):
        def by_description(elem):
            return elem.description
        try:
            events = []
            for attendance in self.repo.get_attendances_with_person(person):
                events.append(attendance.event)
            # events.sort(key=by_description)
            events.sort(key=lambda event: (event.description, event.date.year, event.date.month, event.date.day))
            return events
        except Exception as ex:
            raise Exception(ex)

    def persons_attending_most_events(self):
        try:
            class AttendingPerson(Person):
                def __init__(self, person_id, name, address):
                    super().__init__(person_id, name, address)
                    self.attendances = 1

            def get_person_in_list(prs: AttendingPerson):
                for at_person in at_persons:
                    if at_person == prs:
                        return at_person
                return None

            def by_attendances(elem):
                return elem.attendances

            at_persons = []
            for attendance in self.repo.items:
                at_person = get_person_in_list(attendance.person)
                if at_person is not None:
                    at_person.attendances += 1
                else:
                    at_persons.append(AttendingPerson(
                        attendance.person.id,
                        attendance.person.name,
                        attendance.person.address
                    ))
            at_persons.sort(key=lambda person: person.attendances, reverse=True)
            max_att = at_persons[0].attendances
            at_persons = [Person(at_person.id, at_person.name, at_person.address)
                for at_person in at_persons if at_person.attendances == max_att]
            return at_persons
        except Exception as ex:
            raise Exception(ex)

    def first_20percent_events_with_most_attendees(self):
        try:
            class AttendedEvent(Event):
                def __init__(self, event_id, date, duration, description):
                    super().__init__(event_id, date, duration, description)
                    self.attendees = 1

            def get_event_in_list(ev : AttendedEvent):
                for at_event in at_events:
                    if at_event == ev:
                        return at_event
                return None

            at_events = []
            for attendance in self.repo.items:
                at_event = get_event_in_list(attendance.event)
                if at_event is not None:
                    at_event.attendees += 1
                else:
                    at_events.append(AttendedEvent(
                        attendance.event.id,
                        attendance.event.date,
                        attendance.event.duration,
                        attendance.event.description
                    ))
            at_events.sort(key=lambda event: event.attendees, reverse=True)
            max_att = at_events[0].attendees
            at_events = [Event(at_event.id, at_event.date, at_event.duration, at_event.description)
                          for at_event in at_events if at_event.attendees == max_att]
            at_events.sort(key=lambda event: event.description)
            number_of_events = int(float(20/100) * len(at_events))
            return at_events[0:number_of_events]

        except Exception as ex:
            raise Exception(ex)
