from EventOrganiser.framework.repos import FileRepo, CommandFileRepo


class Service:

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
    from EventOrganiser.domain.entities import Person

    #---------------------------

    def __init__(self, persons):
        super().__init__(persons)
        self.repo.load_from_json()

    def add_person(self, person: Person):
        try:
            self.repo.add(person)
            self.repo.save_to_json()
        except Exception as ex:
            raise Exception(ex)


class EventService(Service):
    from EventOrganiser.domain.entities import Event

    #--------------------------

    def __init__(self, events):
        super().__init__(events)

    def add_event(self, event: Event):
        try:
            self.repo.add(event)
            self.repo.save_to_json()
        except Exception as ex:
            raise Exception(ex)
        self.repo.save_to_json()


class AttendanceService(Service):
    from EventOrganiser.domain.entities import Attendance

    #-------------------------------

    def __init__(self, attendances):
        super().__init__(attendances)
