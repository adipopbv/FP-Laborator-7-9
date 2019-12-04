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
        super().__init__("The parameter is not an int")


class NotListException(AppException):
    def __init__(self):
        super().__init__("The type is not a list")


class NotPersonException(AppException):
    def __init__(self):
        super().__init__("The type is not a person")


class ExistentIdException(AppException):
    def __init__(self):
        super().__init__("Entity with given id already in repo")


class InvalidPersonDataException(AppException):
    def __init__(self):
        super().__init__("Invalid person data")


class InvalidEventDataException(AppException):
    def __init__(self):
        super().__init__("Invalid event data")


class InvalidAttendanceDataException(AppException):
    def __init__(self):
        super().__init__("Invalid attendance data")
