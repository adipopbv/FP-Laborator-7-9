class Repo:

    def __init__(self, *items):
        self._items = [item for item in items]

    def get_items(self):
        return self._items

    def add(self, item):
        self.get_items().append(item)

    def count(self):
        i = 0
        for item in self.get_items():
            i += 1
        return i

    #--------------------------



class FileRepo(Repo):
    import json

    def __init__(self, file_name, *items):
        self._items = [item for item in items]
        self._file_name = file_name

    def get_file_name(self):
        return self._file_name

    def add(self, item):
        Repo.add(self, item)
        try:
            self.update_file()
        except Exception as ex:
            raise Exception(ex)

    #-------------------------------------

    def update_file(self):
        try:
            file = open(self.get_file_name(), "w")
            item_list = []
            for item in self.get_items():
                item_dict = item.make_dict()
                item_list.append(item_dict)
            file_json = self.json.dumps(item_list, indent = 5)
            file.write(file_json)
            file.close()
        except Exception as ex:
            file.close()
            raise Exception(ex)

class CommandsRepo(Repo):

    def __init__(self, *commands):
        self._items = commands

    #-----------------------------

    def get_command_with_id_value(self, id):
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
            if command.get_id().get_value() == id:
                return command
        raise Exception("No command with the given id!")