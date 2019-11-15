from ui.gui.consoles import Console
from framework.repos import CommandsRepo
from domain.entities import Command

class Client:

    def __init__(self, service):
        self._service = service
        self._gui = Console()
        self._commands = CommandsRepo(
            Command("1", self.add_person_to_repo)
        )

    def get_service(self):
        return self._service

    def get_gui(self):
        return self._gui

    def get_commands(self):
        return self._commands

    #---------------------------

    def read(self, prompt):
        text = self.get_gui().read(prompt)
        return text

    def read_command(self):
        try:
            text = self.read("Please input a command: ")
            text = text.strip()
            text = text.split()
            return text[0]
        except Exception as ex:
            self.write_exception(ex)   
            return self.read_command()         

    def write(self, message):
        self.get_gui().write(message)

    def write_exception(self, exception):
        self.write("Error: " + str(exception))

    #---------------------------

    def add_person_to_repo(self):
        print("person added")

    def run(self):
        while True:
            try:
                command = self.read_command()
                self.get_commands().get_command_with_id(command[0]).run()
            except Exception as ex:
                self.write_exception(ex)