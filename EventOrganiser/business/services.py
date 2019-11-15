

class Service:
    
    def __init__(self, persons, events):
        self._persons = persons
        self._events = events

    def get_persons(self):
        return self._persons

    def get_events(self):
        return self._events

    #-----------------------------------