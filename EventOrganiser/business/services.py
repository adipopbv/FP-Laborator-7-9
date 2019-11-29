from EventOrganiser.domain.entities import Attendance, Person, Event


class Service:
    from EventOrganiser.framework.repos import FileRepo

    _repo: FileRepo
    @property
    def repo(self):
        return self._repo
    @repo.setter
    def repo(self, value):
        self._repo = value

    #------------------------

    def __init__(self, repo):
        self.repo = repo


class CommandsService(Service):
    from EventOrganiser.framework.repos import CommandFileRepo

    _repo: CommandFileRepo

    #---------------------------

    def __init__(self, commands):
        super().__init__(commands)
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

    def __init__(self, persons: PersonFileRepo):
        super().__init__(persons)
        self.repo.load_from_json()

    def add_person(self, person: Person):
        try:
            self.repo.add(person)
        except Exception as ex:
            raise Exception(ex)
        self.repo.save_to_json()

    def modify_person(self, field, field_value, modified_person):
        try:
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

    def __init__(self, events: EventFileRepo):
        super().__init__(events)
        self.repo.load_from_json()

    def add_event(self, event: Event):
        try:
            self.repo.add(event)
        except Exception as ex:
            raise Exception(ex)
        self.repo.save_to_json()

    def modify_event(self, field, field_value, modified_event):
        try:
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


class AttendanceService(Service):
    from EventOrganiser.framework.repos import  AttendanceFileRepo

    _repo: AttendanceFileRepo

    #---------------------------------------------------

    def __init__(self, attendances: AttendanceFileRepo):
        super().__init__(attendances)
        self.repo.load_from_json()

    def add_attendance(self, attendance: Attendance):
        try:
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
            events.sort(key=by_description)
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
            at_persons.sort(key=by_attendances, reverse=True)
            max_att = at_persons[0].attendances
            at_persons = [Person(at_person.id, at_person.name, at_person.address)
                for at_person in at_persons if at_person.attendances == max_att]
            return at_persons
        except Exception as ex:
            raise Exception(ex)
