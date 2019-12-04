from EventOrganiser.domain.entities import Person, Event, Attendance
from EventOrganiser.domain.exceptions import *
from EventOrganiser.framework.repos import PersonRepo, EventRepo


class Validator:

    def validate_person_from_repo(self, repo: PersonRepo, person: Person):
        ok = True
        try:
            repo.get_person_with_field_value("id", person.id)
            ok = False
        except:
            self.validate_person(person)
        if not ok:
            raise ExistentIdException

    def validate_person(self, person: Person):
        ok = True
        if type(person) is not Person:
            raise NotPersonException
        try:
            int(person.name)
            ok = False
        except:
            try:
                int(person.address.city)
                ok = False
            except:
                pass
        if not ok:
            raise InvalidPersonDataException

    def validate_event_from_repo(self, repo: EventRepo, event: Event):
        ok = True
        try:
            repo.get_event_with_field_value("id", event.id)
            ok = False
        except:
            self.validate_event(event)
        if not ok:
            raise ExistentIdException


    def validate_event(self, event: Event):
        ok = True
        if type(event) is not Event:
            raise NotEventException
        try:
            int(event.date.year)
            try:
                int(event.date.day)
            except:
                ok = False
        except:
            ok = False
        if not ok:
            raise InvalidEventDataException

    def validate_attendance(self, attendance: Attendance):
        try:
            self.validate_person(attendance.person)
            self.validate_event(attendance.event)
        except:
            raise InvalidAttendanceDataException
