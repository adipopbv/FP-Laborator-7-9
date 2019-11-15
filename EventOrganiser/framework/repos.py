class Repo:

    def __init__(self, *items):
        self._items = items

    def get_items(self):
        return self._items

    #--------------------------



class CommandsRepo(Repo):

    def __init__(self, *commands):
        self._items = commands

    #-----------------------------

    def get_command_with_id(self, id):
        """
        gets the first found command with the given id
        
        Args:
            id (str): an id
        
        Raises:
            Exception: no command with the given id in the repo
        
        Returns:
            Command: a command
        """
        commands = self.get_items()
        for command in commands:
            if command.get_id() == id:
                return command
        raise Exception("No command with the given id!")