class AppException(Exception):
    _message: str
    @property
    def message(self):
        return self._message
    @message.setter
    def message(self, value):
        self._message = value

    def __int__(self, message: str):
        self.message = message

    def __str__(self):
        return str(self.message)


class NotIntParameterException(AppException):
    def __init__(self):
        self.message = "The parameter is not an int"


class NotStringParameterException(AppException):
    def __init__(self):
        self.message = "The parameter is not a string"


class NotListException(AppException):
    def __init__(self):
        self.message = "The type is not a list"


class NotPersonException(AppException):
    def __init__(self):
        self.message = "The type is not a person"


class NotEventException(AppException):
    def __init__(self):
        self.message = "The type is not an event"


class ExistentIdException(AppException):
    def __init__(self):
        self.message = "Entity with given id already in repo"


class InvalidPersonDataException(AppException):
    def __init__(self):
        self.message = "Invalid person data"


class InvalidEventDataException(AppException):
    def __init__(self):
        self.message = "Invalid event data"


class InvalidAttendanceDataException(AppException):
    def __init__(self):
        self.message = "Invalid attendance data"


class NotInRepoException(AppException):
    def __init__(self):
        self.message = "Entity not in repo"


class InexistentCommandException(AppException):
    def __init__(self):
        self.message = "Command inexistent"


class EmptyRepoException(AppException):
    def __init__(self):
        self.message = "No entity in repo"


class NoFieldWithValueException(AppException):
    def __init__(self):
        self.message = "No field with the given value"
