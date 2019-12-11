from EventOrganiser.domain.entities import Attendance, Person, Event
from EventOrganiser.domain.exceptions import *


class Service:
    from EventOrganiser.framework.repos import Repo

    _repo: Repo
    @property
    def repo(self):
        return self._repo
    @repo.setter
    def repo(self, value):
        self._repo = value

    # ------------------------

    def __init__(self, repo):
        self.repo = repo


class CommandsService(Service):
    from EventOrganiser.framework.repos import CommandFileRepo

    _repo: CommandFileRepo

    # ---------------------------

    def __init__(self, commands: CommandFileRepo):
        super().__init__(commands)

    def get_command_with_key(self, key_value):
        for command in self.repo.items:
            for key in command.keys:
                if key == key_value:
                    return command
        raise InexistentCommandException


class PersonService(Service):
    from EventOrganiser.framework.repos import PersonFileRepo

    _repo: PersonFileRepo

    # -------------------------------------------

    def __init__(self, persons: PersonFileRepo):
        super().__init__(persons)

    def add_person(self, person: Person):
        self.repo.add(person)

    def delete_person(self, field, field_value):
        self.repo.delete(self.repo.get_person_with_field_value(field, field_value))

    def modify_person(self, field, field_value, modified_person):
        self.repo.modify(self.repo.get_person_with_field_value(field, field_value), modified_person)

    def search_person(self, field, field_value):
        persons = self.repo.get_persons(field, field_value)
        return persons


class EventService(Service):
    from EventOrganiser.framework.repos import EventFileRepo

    _repo: EventFileRepo

    # -----------------------------------------

    def __init__(self, events: EventFileRepo):
        super().__init__(events)

    def add_event(self, event: Event):
        self.repo.add(event)

    def delete_event(self, field, field_value):
        self.repo.delete(self.repo.get_event_with_field_value(field, field_value))

    def modify_event(self, field, field_value, modified_event):
        self.repo.modify(self.repo.get_event_with_field_value(field, field_value), modified_event)

    def search_event(self, field, field_value):
        events = self.repo.get_events(field, field_value)
        return events

    def generate_random_events(self, number_of_events):
        try:
            for _ in range(0, number_of_events):
                self.repo.generate_random_event()
        except:
            raise NotIntParameterException


class AttendanceService(Service):
    from EventOrganiser.framework.repos import AttendanceFileRepo

    _repo: AttendanceFileRepo

    _persons: list
    @property
    def persons(self):
        return self._persons
    @persons.setter
    def persons(self, value):
        self._persons = value

    _events: list
    @property
    def events(self):
        return self._events
    @events.setter
    def events(self, value):
        self._events = value

    # ---------------------------------------------------

    def __init__(self, persons: list, events: list, attendances: AttendanceFileRepo):
        super().__init__(attendances)
        self.persons = persons
        self.events = events

    def add_attendance(self, attendance: Attendance):
        self.repo.add(self.persons, self. events, attendance)

    def get_ordered_events_attended_by_person(self, person_id: str):
        attendances = self.repo.get_attendances_with_person_id(person_id)
        event_ids = [attendance.event_id for attendance in attendances]
        events = [event for event in self.events if event.id in event_ids]
        events.sort(key=lambda event: (event.description, event.date.year, event.date.month, event.date.day))
        return events

    def get_persons_attending_most_events(self):
        persons_attendances_count = self.repo.get_persons_attendances_counts()
        if self.repo.is_empty():
            raise EmptyRepoException
        max_att_count = max(persons_attendances_count.items())[1]
        persons = []
        for person in self.persons:
            if person.id in persons_attendances_count.keys():
                if persons_attendances_count[person.id] == max_att_count:
                    persons.append(person)
        persons.sort(key=lambda person: person.name)
        return persons

    def get_persons_attending_least_events(self):
        persons_attendances_count = self.repo.get_persons_attendances_counts()
        if self.repo.is_empty():
            raise EmptyRepoException
        min_att_count = min(persons_attendances_count.items())[1]
        persons = []
        for person in self.persons:
            if person.id in persons_attendances_count.keys():
                persons.append(person)
        diff_persons = [person for person in self.persons if person not in persons]
        if len(diff_persons) != 0:
            persons = diff_persons
        else:
            persons = [person for person in persons if persons_attendances_count[person.id] == min_att_count]
        persons.sort(key=lambda person: person.name)
        return persons

    def first_20percent_events_with_most_attendees(self):
        events_attendances_count = self.repo.get_events_attendances_count()
        if self.repo.is_empty():
            raise EmptyRepoException
        max_att_count = max(events_attendances_count.items())[1]
        events = []
        for event in self.events:
            if event.id in events_attendances_count.keys():
                if events_attendances_count[event.id] == max_att_count:
                    events.append(event)
        events.sort(key=lambda event: event.description)
        number_of_events = int(float(20 / 100) * len(events))
        return events[0:number_of_events]
