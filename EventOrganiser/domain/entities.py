from EventOrganiser.domain.exceptions import NotListException
from EventOrganiser.domain.fields import Address, Date
from EventOrganiser.framework.json_tools import JsonFormattable


class Command(JsonFormattable):

    _keys: list
    @property
    def keys(self):
        return self._keys
    @keys.setter
    def keys(self, value):
        self._keys = value

    _function: str
    @property
    def function(self):
        return self._function
    @function.setter
    def function(self, value):
        self._function = value

    _description: str
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value

    #-----------------------------------

    def __init__(self, function: str, description: str, keys: list):
        self.keys = keys
        self.function = function
        self.description = description

    def run(self, instance_obj):
        getattr(instance_obj, self.function)()

    def to_json(self):
        return {
            "keys": self.keys,
            "function": self.function,
            "description": self.description
        }


class Entity(JsonFormattable):

    _id: str
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, value):
        self._id = value

    #---------------------------

    def __init__(self, id: str):
        self.id = id

    def __eq__(self, other):
        equal = self.id == other.id
        return equal

    def to_json(self):
        return {
            "id": self.id
        }


class Person(Entity):

    _name: str
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value):
        self._name = value

    _address: Address
    @property
    def address(self):
        return self._address
    @address.setter
    def address(self, value):
        self._address = value

    #---------------------------------------------------------------

    def __init__(self, person_id: str, name: str, address: Address):
        super().__init__(person_id)
        self.name = name
        self.address = address

    def __eq__(self, other):
        return super().__eq__(other)

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address.to_json()
        }

    def has_field_with_value(self, field, field_value):
        try:
            try:
                if getattr(self, field) == field_value:
                    return True
            except:
                if getattr(self.address, field) == field_value:
                    return True
        except:
            return False
        return False

    def not_in_list(self, persons):
        try:
            for person in persons:
                try:
                    if person == self:
                        return False
                except:
                    continue
            return True
        except:
            raise NotListException


class Event(Entity):

    _date: Date
    @property
    def date(self):
        return self._date
    @date.setter
    def date(self, value):
        self._date = value

    _duration: str
    @property
    def duration(self):
        return self._duration
    @duration.setter
    def duration(self, value):
        self._duration = value

    _description: str
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value

    #------------------------------------------------------------------------------------------

    def __init__(self, event_id: str, date: Date, duration: str, description: str):
        super().__init__(event_id)
        self.date = date
        self.duration = duration
        self.description = description

    def __eq__(self, other):
        return super().__eq__(other)

    def to_json(self):
        return {
            "id": self.id,
            "date": self.date.to_json(),
            "duration": self.duration,
            "description": self.description
        }

    def has_field_with_value(self, field, field_value):
        try:
            try:
                if getattr(self, field) == field_value:
                    return True
            except:
                if getattr(self.date, field) == field_value:
                    return True
        except:
            return False
        return False


class Attendance(Entity):

    _person_id: str
    @property
    def person_id(self):
        return self._person_id
    @person_id.setter
    def person_id(self, value):
        self._person_id = value

    _event_id: str
    @property
    def event_id(self):
        return self._event_id
    @event_id.setter
    def event_id(self, value):
        self._event_id = value

    #------------------------------------------------

    def __init__(self, attendance_id: str, person_id: str, event_id: str):
        super().__init__(attendance_id)
        self.person_id = person_id
        self.event_id = event_id

    def to_json(self):
        return {
            "id": self.id,
            "person_id": self.person_id,
            "event_id": self.event_id
        }