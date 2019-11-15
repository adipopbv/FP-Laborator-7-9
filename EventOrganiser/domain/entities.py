class Command:

    def __init__(self, id, function):
        self._id = id
        self._function = function

    def get_id(self):
        return self._id

    def get_function(self):
        return self._function

    #--------------------------------

    def run(self):
        """
        runs the function
        """
        self.get_function()()

class Field:

    def _init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

class Id(Field):

    def __init__(self, value):
        Field.__init__(value)

class Name(Field):

    def __init__(self, value):
        Field.__init__(value)

class CityName(Field):

    def __init__(self, value):
        Field.__init__(value)

class StreetName(Field):

    def __init__(self, value):
        Field.__init__(value)

class Number(Field):

    def __init__(self, value):
        Field.__init__(value)

class Adress:

    def __init__(self, city_name, street_name, number):
        self._city_name = city_name
        self._street_name = street_name
        self._number = number

    def get_city_name(self):
        return self._city_name

    def get_street_name(self):
        return self._street_name

    def get_number(self):
        return self._number

class Person:

    def __init__(self, id, name, adress):
        self._id = id
        self._name = name
        self._adress = adress

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_adress(self):
        return self._adress        