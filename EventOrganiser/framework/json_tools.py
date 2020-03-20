class JsonFormattable:

    def to_json(self):
        pass


class JsonFileSaver:
    import json

    _file_name: str
    @property
    def file_name(self):
        return self._file_name
    @file_name.setter
    def file_name(self, value):
        self._file_name = value

    def __init__(self, file_name):
        self.file_name = file_name

    def save_to_file(self):
        pass

    def load_from_file(self):
        pass
