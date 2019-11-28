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
        input_key = self.read("Please input a command: ")
        try:
            return self.commands_service.get_command_with_key(input_key)
        except Exception as ex:
            self.write_exception(ex)
            return self.read_command()

    def read_person(self):
        self.write("Please input a person's data: ")
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
        self.write("Please input an event's data: ")
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

    def write_success(self):
        self.write("Operation successful!")

    def write_exception(self, exception):
        self.gui.write("Error: " + str(exception) + ".\nOperation failed!")

    def write_menu(self):
        self.write("Event Organiser commands:")
        for command in self.commands_service.repo.items:
            keys = ""
            for key in command.keys:
                keys += str(key) + "/"
            self.write(" - [" + str(keys[0:-1]) + "]: " + command.description)

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

    def exit_application(self):
        exit()

    def run_application(self):
        while True:
            self.write_menu()
            input_command = self.read_command()
            input_command.run(self)
