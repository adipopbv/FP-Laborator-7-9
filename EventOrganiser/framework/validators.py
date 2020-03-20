from EventOrganiser.domain.entities import Person, Event, Attendance
from EventOrganiser.domain.exceptions import *


class Validator:

    def validate_person_from_repo(self, persons_list: list, person: Person):
        if type(person) is not Person:
            raise NotPersonException
        for list_person in persons_list:
            if list_person.id == person.id:
                raise ExistentIdException
        self.validate_person(person)

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

    def validate_event_from_repo(self, events_list: list, event: Event):
        if type(event) is not Event:
            raise NotEventException
        for list_event in events_list:
            if list_event.id == event.id:
                raise ExistentIdException
        self.validate_event(event)


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

    def validate_attendance(self, persons_list: list, events_list: list, attendance: Attendance):
        for person in persons_list:
            if person.id == attendance.person_id:
                for event in events_list:
                    if event.id == attendance.event_id:
                        return
        raise InvalidAttendanceDataException
