from EventOrganiser.domain.entities import Command, Person, Event, Attendance
from EventOrganiser.domain.exceptions import *
from EventOrganiser.domain.fields import Address, Date
from EventOrganiser.framework.json_tools import JsonFileSaver
from EventOrganiser.framework.validators import Validator


class Repo:

    _items: list
    @property
    def items(self):
        return self._items
    @items.setter
    def items(self, value):
        self._items = value

    # ------------------

    def __init__(self, items: list):
        self.items = items

    def index_of(self, entity):
        try:
            return self.items.index(entity)
        except:
            raise NotInRepoException

    def is_empty(self):
        if len(self.items) == 0:
            return True
        return False


class ModifiableRepo(Repo):

    def add(self, entity):
        self.items.append(entity)

    def delete(self, entity):
        try:
            self.items.remove(entity)
        except:
            raise NotInRepoException

    def modify(self, old_entity, new_entity):
        self.items[self.index_of(old_entity)] = new_entity


class FileRepo(Repo, JsonFileSaver):

    def __init__(self, file_name: str, items: list):
        Repo.__init__(self, items)
        JsonFileSaver.__init__(self, file_name)
        self.load_from_file()

    def save_to_file(self):
        file = open(self.file_name, "w")
        try:
            data_list = [item.to_json() for item in self.items]
            data = self.json.dumps(data_list, indent=4)
            file.write(data)
            file.close()
        except Exception as ex:
            file.close()
            raise Exception(ex)


class CommandRepo(Repo):

    def __init__(self, commands: list):
        super().__init__(commands)


class CommandFileRepo(FileRepo, CommandRepo):

    def __init__(self, file_name: str):
        FileRepo.__init__(self, file_name, [])
        self.load_from_file()

    def load_from_file(self):
        file = open(self.file_name, "r")
        try:
            file_string = file.read()
            data = self.json.loads(file_string)

            commands = []
            for data_command in data:
                keys = []
                for data_key in data_command["keys"]:
                    keys.append(data_key)
                commands.append(Command(data_command["function"], data_command["description"], keys))

            self.items = commands
            file.close()
        except Exception as ex:
            file.close()
            raise Exception(ex)


class ModifiableFileRepo(ModifiableRepo, JsonFileSaver):

    def __init__(self, file_name: str, items: list):
        ModifiableRepo.__init__(self, items)
        JsonFileSaver.__init__(self, file_name)
        self.load_from_file()

    def add(self, entity):
        self.load_from_file()
        super().add(entity)
        self.save_to_file()

    def delete(self, entity):
        self.load_from_file()
        super().delete(entity)
        self.save_to_file()

    def modify(self, old_entity, new_entity):
        self.load_from_file()
        super().modify(old_entity, new_entity)
        self.save_to_file()

    def save_to_file(self):
        file = open(self.file_name, "w")
        try:
            data_list = [item.to_json() for item in self.items]
            data = self.json.dumps(data_list, indent=4)
            file.write(data)
            file.close()
        except Exception as ex:
            file.close()
            raise Exception(ex)


class PersonRepo(ModifiableRepo):

    _validator: Validator
    @property
    def validator(self):
        return self._validator
    @validator.setter
    def validator(self, value):
        self._validator = value

    def __init__(self, validator: Validator, items: list):
        super().__init__(items)
        self.validator = validator

    def add(self, person):
        self.validator.validate_person_from_repo(self.items, person)
        super().add(person)

    def delete(self, person):
        super().delete(person)

    def modify(self, old_person, new_person):
        self.validator.validate_person(new_person)
        super().modify(old_person, new_person)

    def get_person_with_field_value(self, field, value):
        if field != "address":
            if len(self.items) == 0:
                raise EmptyRepoException
            for person in self.items:
                try:
                    if getattr(person, field) == value:
                        return person
                except:
                    try:
                        if getattr(person.address, field) == value:
                            return person
                    except:
                        pass
        raise NoFieldWithValueException

    def get_persons(self, field, field_value):
        persons = [person for person in self.items if person.has_field_with_value(field, field_value)]
        return persons


class PersonFileRepo(ModifiableFileRepo, PersonRepo):

    def __init__(self, validator: Validator, file_name: str, items: list):
        ModifiableFileRepo.__init__(self, file_name, items)
        PersonRepo.__init__(self, validator, items)
        self.load_from_file()

    def add(self, person):
        self.load_from_file()
        PersonRepo.add(self, person)
        self.save_to_file()

    def delete(self, person):
        self.load_from_file()
        PersonRepo.delete(self, person)
        self.save_to_file()

    def modify(self, old_person, new_person):
        self.load_from_file()
        PersonRepo.modify(self, old_person, new_person)
        self.save_to_file()

    def get_person_with_field_value(self, field, value):
        self.load_from_file()
        return PersonRepo.get_person_with_field_value(self, field, value)

    def get_persons(self, field, field_value):
        self.load_from_file()
        return PersonRepo.get_persons(self, field, field_value)

    def load_from_file(self):
        file = open(self.file_name, "r")
        try:
            file_string = file.read()
            data = self.json.loads(file_string)

            persons = []
            for data_person in data:
                persons.append(Person(
                    data_person["id"],
                    data_person["name"],
                    Address(
                        data_person["address"]["city"],
                        data_person["address"]["street"],
                        data_person["address"]["number"]
                    )
                ))

            self.items = persons
            file.close()
        except Exception as ex:
            file.close()
            raise Exception(ex)


class EventRepo(ModifiableRepo):

    _validator: Validator
    @property
    def validator(self):
        return self._validator
    @validator.setter
    def validator(self, value):
        self._validator = value

    def __init__(self, validator: Validator, items: list):
        super().__init__(items)
        self.validator = validator

    def add(self, event):
        self.validator.validate_event_from_repo(self.items, event)
        super().add(event)

    def delete(self, event):
        super().delete(event)

    def modify(self, old_event, new_event):
        self.validator.validate_event(new_event)
        super().modify(old_event, new_event)

    def _random_event(self):
        from EventOrganiser.framework.randomization import Random
        rand = Random()
        event = Event(
            rand.string_of_chr(10),
            Date(
                rand.string_of_int(2),
                rand.string_of_chr(10),
                rand.string_of_int(4)
            ),
            rand.string_of_chr(10),
            rand.string_of_chr(10)
        )
        return event

    def generate_random_event(self):
        try:
            event = self._random_event()
            self.add(event)
        except:
            self.generate_random_event()

    def get_event_with_field_value(self, field, value):
        if field != "date":
            if len(self.items) == 0:
                raise EmptyRepoException
            for event in self.items:
                try:
                    if getattr(event, field) == value:
                        return event
                except:
                    try:
                        if getattr(event.date, field) == value:
                            return event
                    except:
                        pass
        raise NoFieldWithValueException

    def get_events(self, field, field_value):
        events = [event for event in self.items if event.has_field_with_value(field, field_value)]
        return events


class EventFileRepo(ModifiableFileRepo, EventRepo):

    def __init__(self, validator: Validator, file_name: str, items: list):
        ModifiableFileRepo.__init__(self, file_name, items)
        EventRepo.__init__(self, validator, items)
        self.load_from_file()

    def add(self, event):
        self.load_from_file()
        EventRepo.add(self, event)
        self.save_to_file()

    def delete(self, event):
        self.load_from_file()
        EventRepo.delete(self, event)
        self.save_to_file()

    def modify(self, old_event, new_event):
        self.load_from_file()
        EventRepo.modify(self, old_event, new_event)
        self.save_to_file()

    def generate_random_event(self):
        self.load_from_file()
        EventRepo.generate_random_event(self)
        self.save_to_file()

    def get_event_with_field_value(self, field, value):
        self.load_from_file()
        return EventRepo.get_event_with_field_value(self, field, value)

    def get_events(self, field, value):
        self.load_from_file()
        return EventRepo.get_events(self, field, value)

    def load_from_file(self):
        file = open(self.file_name, "r")
        try:
            file_string = file.read()
            data = self.json.loads(file_string)

            events = []
            for data_event in data:
                events.append(Event(
                    data_event["id"],
                    Date(
                        data_event["date"]["day"],
                        data_event["date"]["month"],
                        data_event["date"]["year"]
                    ),
                    data_event["duration"],
                    data_event["description"]
                ))

            self.items = events
            file.close()
        except Exception as ex:
            file.close()
            raise Exception(ex)


class AttendanceRepo(ModifiableRepo):

    _validator: Validator
    @property
    def validator(self):
        return self._validator
    @validator.setter
    def validator(self, value):
        self._validator = value

    def __init__(self, validator: Validator, items: list):
        super().__init__(items)
        self.validator = validator

    def add(self, persons: list, events: list, attendance):
        self.validator.validate_attendance(persons, events, attendance)
        super().add(attendance)

    def get_free_id(self):
        return len(self.items)

    def get_attendances_with_person_id(self, person_id: str):
        attendances = []
        if len(self.items) == 0:
            raise EmptyRepoException
        if type(person_id) != str:
            raise NotStringParameterException
        for attendance in self.items:
            if attendance.person_id == person_id:
                attendances.append(attendance)
        return attendances

    def get_persons_attendances_counts(self):
        attendances_count = {}
        for attendance in self.items:
            try:
                attendances_count[str(attendance.person_id)] += 1
            except:
                attendances_count[str(attendance.person_id)] = 1
        return attendances_count

    def get_events_attendances_count(self):
        attendances_count = {}
        for attendance in self.items:
            try:
                attendances_count[str(attendance.event_id)] += 1
            except:
                attendances_count[str(attendance.event_id)] = 1
        return attendances_count


class AttendanceFileRepo(ModifiableFileRepo, AttendanceRepo):

    def __init__(self, validator: Validator, file_name: str, items: list):
        ModifiableFileRepo.__init__(self, file_name, items)
        AttendanceRepo.__init__(self, validator, items)
        self.load_from_file()

    def add(self, persons: list, events: list, attendance):
        self.load_from_file()
        AttendanceRepo.add(self, persons, events, attendance)
        self.save_to_file()

    def get_free_id(self):
        self.load_from_file()
        return AttendanceRepo.get_free_id(self)

    def get_attendances_with_person_id(self, person_id: str):
        self.load_from_file()
        return AttendanceRepo.get_attendances_with_person_id(self, person_id)

    def get_persons_attendances_counts(self):
        self.load_from_file()
        return AttendanceRepo.get_persons_attendances_counts(self)

    def get_events_attendances_count(self):
        self.load_from_file()
        return AttendanceRepo.get_events_attendances_count(self)

    def load_from_file(self):
        file = open(self.file_name, "r")
        try:
            file_string = file.read()
            data = self.json.loads(file_string)

            attendances = []
            for data_attendance in data:
                attendances.append(Attendance(
                    data_attendance["id"],
                    data_attendance["person_id"],
                    data_attendance["event_id"]
                ))

            self.items = attendances
            file.close()
        except Exception as ex:
            file.close()
            raise Exception(ex)
