from EventOrganiser.domain.entities import Person, Event, Attendance
from EventOrganiser.framework.repos import PersonFileRepo, EventFileRepo, AttendanceFileRepo


class Validator:

    def validate_person_from_repo(self, repo: PersonFileRepo, person: Person):
        ok = True
        try:
            repo.get_person_with_field_value("id", person.id)
            ok = False
        except:
            try:
                self.validate_person(person)
            except Exception as ex:
                raise Exception(ex)
        if not ok:
            raise Exception("Person with id already in repo")

    def validate_person(self, person: Person):
        ok = True
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
            raise Exception("Invalid person data")

    def validate_event_from_repo(self, repo: EventFileRepo, event: Event):
        ok = True
        try:
            repo.get_event_with_field_value("id", event.id)
            ok = False
        except:
            try:
                self.validate_event(event)
            except Exception as ex:
                raise Exception(ex)
        if not ok:
            raise Exception("Event with id already in repo")


    def validate_event(self, event: Event):
        ok = True
        try:
            int(event.date.year)
            try:
                int(event.date.day)
            except:
                ok = False
        except:
            ok = False
        if not ok:
            raise Exception("Invalid event data")

    def validate_attendance(self, attendance: Attendance):
        try:
            self.validate_person(attendance.person)
            self.validate_event(attendance.event)
        except Exception as ex:
            raise Exception(ex)
