from EventOrganiser.business.services import CommandsService, PersonService, EventService, AttendanceService
from EventOrganiser.ui.guis import ConsoleGUI
from EventOrganiser.domain.entities import Person, Event, Attendance
from EventOrganiser.domain.fields import Address, Date


class ConsoleUI:

    _commands_service: CommandsService
    @property
    def commands_service(self):
        return self._commands_service
    @commands_service.setter
    def commands_service(self, value):
        self._commands_service = value

    _persons_service: PersonService
    @property
    def persons_service(self):
        return self._persons_service
    @persons_service.setter
    def persons_service(self, value):
        self._persons_service = value

    _events_service: EventService
    @property
    def events_service(self):
        return self._events_service
    @events_service.setter
    def events_service(self, value):
        self._events_service = value

    _attendances_service: AttendanceService
    @property
    def attendances_service(self):
        return self._attendances_service
    @attendances_service.setter
    def attendances_service(self, value):
        self._attendances_service = value

    _gui: ConsoleGUI
    @property
    def gui(self):
        return self._gui
    @gui.setter
    def gui(self, value):
        self._gui = value

    # -----------------------------------------------------------------------------------------

    def __init__(self, commands_service, persons_service, events_service, attendances_service):
        self.commands_service = commands_service
        self.persons_service = persons_service
        self.events_service = events_service
        self.attendances_service = attendances_service
        self.gui = ConsoleGUI()

    def read(self, prompt: str):
        return self.gui.read(prompt)

    def read_command(self):
        input_key = self.read("\nPlease input a command: ")
        try:
            return self.commands_service.get_command_with_key(input_key)
        except Exception as ex:
            self.write_exception(ex)
            return self.read_command()

    def read_person(self):
        self.write("\nPlease input a person's data: ")
        person = Person(
            self.read("Id: "),
            self.read("Name: "),
            Address(
                self.read("Address:\n    City: "),
                self.read("    Street: "),
                self.read("    Number: ")
            )
        )
        return person

    def read_event(self):
        self.write("\nPlease input an event's data: ")
        person = Event(
            self.read("Id: "),
            Date(
                self.read("Date:\n    Day: "),
                self.read("    Month: "),
                self.read("    Year: ")
            ),
            self.read("Duration: "),
            self.read("Description: ")
        )
        return person

    def write(self, message: str):
        self.gui.write(message)

    def write_person(self, person: Person):
        self.write("---------------")
        self.write("Id: " + str(person.id))
        self.write("Name: " + str(person.name))
        self.write("Address\n    City: " + str(person.address.city))
        self.write("    Street: " + str(person.address.street))
        self.write("    Number: " + str(person.address.number))

    def write_persons(self, persons: list):
        self.write("The requested persons:")
        for person in persons:
            self.write_person(person)

    def write_event(self, event: Event):
        self.write("---------------")
        self.write("Id: " + str(event.id))
        self.write("Date\n    Day: " + str(event.date.day))
        self.write("    Month: " + str(event.date.month))
        self.write("    Year: " + str(event.date.year))
        self.write("Duration: " + str(event.duration))
        self.write("Description: " + str(event.description))

    def write_events(self, events: list):
        self.write("The requested events:")
        for event in events:
            self.write_event(event)

    def write_success(self):
        self.write("\nOperation successful!")

    def write_exception(self, exception: Exception):
        self.gui.write("\nError: " + str(exception) + ".\nOperation failed!")

    def write_menu(self):
        self.write("\nEvent Organiser commands:")
        for command in self.commands_service.repo.items:
            keys = ""
            for key in command.keys:
                keys += str(key) + "/"
            self.write(" - [" + str(keys[0:-1]) + "]: " + command.description)

    # ----------------------------------------------

    def add_person(self):
        person = self.read_person()
        self.persons_service.add_person(person)

    def add_event(self):
        event = self.read_event()
        self.events_service.add_event(event)

    def delete_person(self):
        self.write("\nPerson to delete:")
        field = self.read("    Please input a field to search by: ")
        field_value = self.read("    Please input the value: ")
        self.persons_service.delete_person(field, field_value)

    def delete_event(self):
        self.write("\nEvent to delete:")
        field = self.read("    Please input a field to search by: ")
        field_value = self.read("    Please input the value: ")
        self.events_service.delete_event(field, field_value)

    def modify_person(self):
        self.write("\nPerson to modify:")
        field = self.read("    Please input a field to search by: ")
        field_value = self.read("    Please input the value: ")
        self.write("\nModified person:")
        modified_person = self.read_person()
        self.persons_service.modify_person(field, field_value, modified_person)

    def modify_event(self):
        self.write("\nEvent to modify:")
        field = self.read("Please input a field to search by: ")
        field_value = self.read("Please input the value: ")
        self.write("\nModified event:")
        modified_event = self.read_event()
        self.events_service.modify_event(field, field_value, modified_event)

    def search_person(self):
        self.write("\nPerson to search:")
        field = self.read("    Please input a field to search by: ")
        field_value = self.read("    Please input the value: ")
        persons = self.persons_service.search_person(field, field_value)
        self.write_persons(persons)

    def search_event(self):
        self.write("\nEvent to search:")
        field = self.read("    Please input a field to search by: ")
        field_value = self.read("    Please input the value: ")
        events = self.events_service.search_event(field, field_value)
        self.write_events(events)

    def enroll_person(self):
        person_id = self.read("Please input the person's id: ")
        event_id = self.read("Please input the id of the event: ")
        attendance = Attendance(
            self.attendances_service.repo.get_free_id(),
            self.persons_service.search_person("id", person_id)[0],
            self.events_service.search_event("id", event_id)[0]
        )
        self.attendances_service.add_attendance(attendance)

    def ordered_events_attended_by_person(self):
        person_id = self.read("Please input the person's id: ")
        events = self.attendances_service.get_ordered_events_attended_by_person(
            self.persons_service.search_person("id", person_id)[0])
        self.write_events(events)

    def persons_attending_most_events(self):
        persons = self.attendances_service.persons_attending_most_events()
        self.write_persons(persons)

    def first_20percent_events_with_most_attendees(self):
        events = self.attendances_service.first_20percent_events_with_most_attendees()
        self.write_events(events)

    def generate_random_events(self):
        number_of_events = int(self.read("Please input the number of random events to be generated: "))
        self.events_service.generate_random_events(number_of_events)

    def persons_attending_least_events(self):
        persons = self.attendances_service.persons_attending_least_events(self.persons_service.repo.items)
        self.write_persons(persons)

    def exit_application(self):
        exit()

    # ----------------------------------------------

    def run_application(self):
        while True:
            self.write_menu()
            input_command = self.read_command()
            try:
                input_command.run(self)
                self.write_success()
            except Exception as ex:
                self.write_exception(ex)
