class Entity:

    def make_dict(self):
        """
        makes a dictionary from its fields
        
        Returns:
            dict: a dictionary
        """
        return {}

class Field(Entity):

    def __init__(self, value):
        self._value = value

    def get_value(self):
        return self._value

    def make_dict(self):
        """
        makes a dictionary from its fields
        
        Returns:
            dict: a dictionary
        """
        return {"value": self.get_value()}

class Id(Field):

    def __init__(self, value):
        Field.__init__(self, value)

class Name(Field):

    def __init__(self, value):
        Field.__init__(self, value)

class CityName(Field):

    def __init__(self, value):
        Field.__init__(self, value)

class StreetName(Field):

    def __init__(self, value):
        Field.__init__(self, value)

class Number(Field):

    def __init__(self, value):
        Field.__init__(self, value)

class Function(Field):

    def __init__(self, value):
        Field.__init__(self, value)

class Command(Entity):

    def __init__(self, id, function):
        self._id = id
        self._function = function

    def get_id(self):
        return self._id

    def get_function(self):
        return self._function

    def make_dict(self):
        """
        makes a dictionary from its fields
        
        Returns:
            dict: a dictionary
        """
        dictionary = {
            "id": self.get_id().make_dict(),
            "function": self.get_function().make_dict()
        }
        return dictionary

    #--------------------------------

    def run(self):
        """
        runs the function
        """
        self.get_function().get_value()()

class Adress(Entity):

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

    def make_dict(self):
        """
        makes a dictionary from its fields
        
        Returns:
            dict: a dictionary
        """
        dictionary = {
            "city_name": self.get_city_name().make_dict(),
            "street_name": self.get_street_name().make_dict(),
            "number": self.get_number().make_dict()
        }
        return dictionary

class Person(Entity):

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

    def make_dict(self):
        """
        makes a dictionary from its fields
        
        Returns:
            dict: a dictionary
        """
        dictionary = {
            "id": self.get_id().make_dict(),
            "name": self.get_name().make_dict(),
            "adress": self.get_adress().make_dict()
        }
        return dictionary