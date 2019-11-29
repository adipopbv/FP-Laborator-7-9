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

    #------------------------------------------------------------------------------------------

    def __init__(self, commands_service, persons_service, events_service, attendances_service):
        self.commands_service = commands_service
        self.persons_service = persons_service
        self.events_service = events_service
        self.attendances_service = attendances_service
        self.gui = ConsoleGUI()
        # self.commands = Repo(
        #     Command("exit_application", "Closes the application.", "0", "exit"),
        #     Command("add_person", "Adds a person to the repo.", "1", "add person")
        # )

    def read(self, prompt):
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

    def write(self, message):
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

    def write_exception(self, exception):
        self.gui.write("\nError: " + str(exception) + ".\nOperation failed!")

    def write_menu(self):
        self.write("\nEvent Organiser commands:")
        for command in self.commands_service.repo.items:
            keys = ""
            for key in command.keys:
                keys += str(key) + "/"
            self.write(" - [" + str(keys[0:-1]) + "]: " + command.description)

    #----------------------------------------------

    def add_person(self):
        try:
            person = self.read_person()
            self.persons_service.add_person(person)
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def add_event(self):
        try:
            event = self.read_event()
            self.events_service.add_event(event)
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def modify_person(self):
        try:
            self.write("\nPerson to modify:")
            field = self.read("    Please input a field to search by: ")
            field_value = self.read("    Please input the value: ")
            self.write("\nModified person:")
            modified_person = self.read_person()
            self.persons_service.modify_person(field, field_value, modified_person)
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def modify_event(self):
        try:
            self.write("\nEvent to modify:")
            field = self.read("Please input a field to search by: ")
            field_value = self.read("Please input the value: ")
            self.write("\nModified event:")
            modified_event = self.read_event()
            self.events_service.modify_event(field, field_value, modified_event)
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def search_person(self):
        try:
            self.write("\nPerson to search:")
            field = self.read("    Please input a field to search by: ")
            field_value = self.read("    Please input the value: ")
            persons = self.persons_service.search_person(field, field_value)
            self.write_persons(persons)
        except Exception as ex:
            self.write_exception(ex)

    def search_event(self):
        try:
            self.write("\nEvent to search:")
            field = self.read("    Please input a field to search by: ")
            field_value = self.read("    Please input the value: ")
            events = self.events_service.search_event(field, field_value)
            self.write_events(events)
        except Exception as ex:
            self.write_exception(ex)

    def enroll_person(self):
        try:
            person_id = self.read("Please input the person's id: ")
            event_id = self.read("Please input the id of the event: ")
            attendance = Attendance(
                self.attendances_service.repo.get_free_id(),
                self.persons_service.search_person("id", person_id)[0],
                self.events_service.search_event("id", event_id)[0]
            )
            self.attendances_service.add_attendance(attendance)
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def ordered_events_attended_by_person(self):
        try:
            person_id = self.read("Please input the person's id: ")
            events = self.attendances_service.get_ordered_events_attended_by_person(
                self.persons_service.search_person("id", person_id)[0])
            self.write_events(events)
        except Exception as ex:
            self.write_exception(ex)

    def exit_application(self):
        exit()

    #----------------------------------------------

    def run_application(self):
        while True:
            self.write_menu()
            input_command = self.read_command()
            input_command.run(self)
