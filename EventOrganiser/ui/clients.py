from ui.gui.consoles import Console
from framework.repos import CommandsRepo
from domain.entities import Id, Function, Command

class Client:
    
    def __init__(self, service):
        self._service = service
        self._gui = Console()
        self._commands = CommandsRepo(
            Command(Id("0"), Function(self.exit_app)),
            Command(Id("1"), Function(self.add_person_to_repo)),
            Command(Id("2"), Function(self.add_event_to_repo)),
            Command(Id("3"), Function(self.modify_person_from_repo)),
            Command(Id("4"), Function(self.modify_event_from_repo)),
            Command(Id("5"), Function(self.search_person_in_repo)),
            Command(Id("6"), Function(self.search_event_in_repo))
        )

    def get_service(self):
        return self._service

    def get_gui(self):
        return self._gui

    def get_commands(self):
        return self._commands

    #---------------------------

    def read(self, prompt):
        """
        reads input from the user
        
        Args:
            prompt (str): text to be outputted before getting input
        
        Returns:
            str: input text
        """
        text = self.get_gui().read(prompt)
        return text

    def read_command(self):
        """
        reads input command from the user
        
        Returns:
            list: a command
        """
        try:
            text = self.read("Please input a command: ")
            text = text.strip()
            text = text.split()
            return text[0]
        except Exception as ex:
            self.write_exception(ex)   
            return self.read_command()         

    def write(self, message):
        """
        writes output message to the user
        
        Args:
            message (str): output text
        """
        self.get_gui().write(message)

    def write_success(self):
        self.write("Operation successful!")

    def write_person(self, person):
        """
        writes a person's data to the user
        
        Args:
            person (Person): a person
        """
        self.write("The requested person is:")
        self.write("Id: " + person.get_id().get_value())
        self.write("Name: " + person.get_name().get_value())
        self.write("Adress")
        self.write("    City: " + person.get_adress().get_city_name().get_value())
        self.write("    Street: " + person.get_adress().get_street_name().get_value())
        self.write("    Number: " + person.get_adress().get_number().get_value())

    def write_event(self, event):
        """
        writes an event's data to the user
        
        Args:
            event (Event): an event
        """
        self.write("The requested event is:")
        self.write("Id: " + event.get_id().get_value())
        self.write("Date")
        self.write("    Day: " + event.get_date().get_day().get_value())
        self.write("    Day: " + event.get_date().get_month().get_value())
        self.write("    Day: " + event.get_date().get_year().get_value())
        self.write("Duration")
        self.write("    Hours: " + event.get_duration().get_hours().get_value())
        self.write("    Minutes: " + event.get_duration().get_minutes().get_value())
        self.write("Description: " + event.get_description().get_value())

    def write_exception(self, exception):
        """
        writes exception to the user
        
        Args:
            exception (Exception): an exception
        """
        self.write("Error: " + str(exception))

    #---------------------------

    def add_person_to_repo(self):
        """
        reads and adds a person to the repo
        """
        try:
            self.write("Please input a person:")
            self.get_service().add_person_to_repo(
                self.get_service().get_persons(), 
                self.read("Id: "),  
                self.read("Name: "),
                self.read("Adress \n    City: "),
                self.read("    Street: "),
                self.read("    Number: ")
            )
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def add_event_to_repo(self):
        """
        reads and adds an event to the repo
        """
        try:
            self.write("Please input an event:")
            self.get_service().add_event_to_repo(
                self.get_service().get_events(),
                self.read("Id: "),
                self.read("Date \n    Day: "),
                self.read("    Month: "),
                self.read("    Year: "),
                self.read("Duration \n    Hours: "),
                self.read("    Minutes: "),
                self.read("Description: ")
            )
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def modify_person_from_repo(self):
        """
        reads an id and a person's new data to change to
        """
        try:
            self.write("Please input a person's id:")
            self.get_service().modify_person_from_repo(
                self.get_service().get_persons(),
                self.read("Id: "),
                self.read("Please input the modified person's data:\nId: "),  
                self.read("Name: "),
                self.read("Adress \n    City: "),
                self.read("    Street: "),
                self.read("    Number: ")
            )
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def modify_event_from_repo(self):
        """
        reads an id and a event's new data to change to
        """
        try:
            self.write("Please input an event's id:")
            self.get_service().modify_event_from_repo(
                self.get_service().get_events(),
                self.read("Id: "),
                self.read("Please input the modified event's data:\nId: "),
                self.read("Date \n    Day: "),
                self.read("    Month: "),
                self.read("    Year: "),
                self.read("Duration \n    Hours: "),
                self.read("    Minutes: "),
                self.read("Description: ")
            )
            self.write_success()
        except Exception as ex:
            self.write_exception(ex)

    def search_person_in_repo(self):
        """
        searches a person by id
        """
        try:
            self.write("Please input a person's id:")
            person = self.get_service().search_person_in_repo(
                self.get_service().get_persons(),
                self.read("Id: ")
            )
            self.write_person(person)
        except Exception as ex:
            self.write_exception(ex)

    def search_event_in_repo(self):
        """
        searches a event by id
        """
        try:
            self.write("Please input an event's id:")
            event = self.get_service().search_event_in_repo(
                self.get_service().get_events(),
                self.read("Id: ")
            )
            self.write_event(event)
        except Exception as ex:
            self.write_exception(ex)

    def exit_app(self):
        """
        exits application
        """
        self.write("Application exit...")
        exit()

    def run(self):
        """
        application main loop
        """
        while True:
            try:
                command = self.read_command()
                self.get_commands().get_command_with_id_value(command[0]).run()
            except Exception as ex:
                self.write_exception(ex)