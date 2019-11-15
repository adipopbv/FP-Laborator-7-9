from domain.entities import Repo

class Service:
    
    _persons = Repo()
    def get_persons(self):
        return self._persons
    _events = Repo()
    def get_events(self):
        return self._events

    def __init__(self, persons, events):
        self._persons = persons
        self._events = events

    def add_person_to_repo(self, repo, person):
        pass

    def remove_person_from_repo(self, repo, person):
        pass
