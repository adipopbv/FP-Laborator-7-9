from ui.gui.consoles import Console
from business.services import Service
from domain.entities import PickCommand, Adress, Date, Moment, Period, Person, Event
from framework.repos import Repo

class Client:

    _console = Console()
    def get_console(self):
        return self._console
    def get_service(self):
        return self._service

    def __init__(self, service):
        self._service = service


    def read(self, prompt):
        return self.get_console().read(prompt)

    def read_command(self):
        text = self.read("Please input a command here: ")
        try:
            text = str(text)
            text = text.strip()
            text = text.split()
            return text
        except Exception as ex:
            self.write_exception(ex)
            return self.read_command()

    def read_person(self):
        try:
            self.write("Please input a person:")
            id = int(self.read("ID: "))
            name = self.read("Name: ")
            city = self.read("Adress: \n    City: ")
            street = self.read("    Street: ")
            number = int(self.read("    Number: "))
            person = Person(id, name, Adress(city, street, number))
            return person
        except Exception as ex:
            self.write_exception(ex)
            return self.read_person()

    def write(self, message):
        self.get_console().write(message)

    def write_exception(self, exception):
        self.get_console().write("Error: " + str(exception))

    def write_success(self):
        self.get_console().write("Operation successful!\n")
    
    def write_person(self, person):
        self.write("The requested person is:")
        self.write("ID: " + str(person.get_id()))
        self.write("Name: " + str(person.get_id()))
        self.write("Adress: \n    City: " + str(person.get_id()))
        self.write("    Street: " + str(person.get_id()))
        self.write("    Number: " + str(person.get_id()))

#-----------------------------------

    def add_person(self):
        try:
            person = self.read_person()
            self.get_service().add_person_to_repo(self.get_service().get_persons(), person)
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def remove_person(self):
        try:
            person = self.read_person()
            self.get_service().remove_person_from_repo(self.get_service().get_persons(), person)
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)
    
    _pick_commands = Repo(
        PickCommand("1", add_person),
        PickCommand("2", remove_person)
    )

    def get_pick_commands(self):
        return self._pick_commands

    def run(self):
        while True:
            command_id = self.read_command()
            self.get_pick_commands().get_item_with_field_name_and_value("id", command_id).run()
