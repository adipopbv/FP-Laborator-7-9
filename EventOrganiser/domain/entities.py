class Person:

    _person_id = None
    _name = None
    _adress = None

    def __init__(self, person_id, name, adress):
        self._person_id = person_id
        self._name = name
        self._adress = adress

    def get_id(self):
        return self._person_id

    def get_name(self):
        return self._name

    def get_adress(self):
        return self._adress

class Event:

    _event_id = None
    _date = None
    _period = None
    _description = None

    def __init__(self, event_id, date, period, description):
        self._event_id = event_id
        self._date = date
        self._period = period
        self._description = description

    def get_id(self):
        return self._event_id
    
    def get_date(self):
        return self._date

    def get_period(self):
        return self._period

    def get_description(self):
        return self._description