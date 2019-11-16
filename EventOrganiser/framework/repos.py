class JsonSaver:
    import json

    def __init__(self, file_name):
        self._file_name = file_name

    def get_file_name(self):
        return self._file_name

    def write_to_file(self, data):
        try:
            file = open(self.get_file_name(), "w")
            data = self.json.dumps(data, indent = 4)
            file.write(data)
            file.close()
        except Exception as ex:
            file.close()
            raise Exception(ex)

    def append_to_file(self, data):
        try:
            file = open(self.get_file_name(), "a")
            data = ",\n" + self.json.dumps(data, indent = 4)
            file.write(data)
            file.close()
        except Exception as ex:
            file.close()
            raise Exception(ex)

class Repo:

    def __init__(self, *items):
        self._items = [item for item in items]

    def get_items(self):
        return self._items

    def add(self, item):
        """
        adds an item to the list
        
        Args:
            item (Entity): an item
        """
        self.get_items().append(item)

    def count(self):
        """
        gets the number of items in the list
        
        Returns:
            int: number of items in list
        """
        i = 0
        for item in self.get_items():
            i += 1
        return i

    def index_of(self, item):
        return self.get_items().index(item)

    def replace(self, x, y):
        self.get_items()[self.index_of(x)] = y

class FileRepo(Repo, JsonSaver):

    def __init__(self, file_name, *items):
        self._items = [item for item in items]
        self._file_name = file_name

    def add(self, item):
        """
        adds an item to the list and updates the file
        
        Args:
            item (Entity): an item
        
        Raises:
            Exception: file not updated
        """
        Repo.add(self, item)
        try:
            self.update_file()
        except Exception as ex:
            raise Exception(ex)
        
    def replace(self, x, y):
        Repo.replace(self, x, y)
        try:
            self.update_file()
        except Exception as ex:
            raise Exception(ex)

    def update_file(self):
        """
        updates the json file
        
        Raises:
            Exception: file not updated
        """
        try:
            item_list = []
            for item in self.get_items():
                item_dict = item.make_dict()
                item_list.append(item_dict)
            self.write_to_file(item_list)
        except Exception as ex:
            raise Exception(ex)

class IdRepo(Repo):

    def __init__(self, *items):
        self._items = [item for item in items]

    def get_item_with_id_value(self, id):
        id_items = self.get_items()
        for id_item in id_items:
            if id_item.get_id().get_value() == id:
                return id_item
        raise Exception("No person with the given id!")

class IdFileRepo(IdRepo, FileRepo):

    def __init__(self, file_name, *items):
        self._items = [item for item in items]
        self._file_name = file_name

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