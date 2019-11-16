from domain.entities import Id, Name, CityName, StreetName, Number, Adress, Person
from domain.entities import Day, Month, Year, Date, Hours, Minutes, Duration, Description, Event

class Service:
    
    def __init__(self, persons, events, validator):
        self._persons = persons
        self._events = events
        self._validator = validator

    def get_persons(self):
        return self._persons

    def get_events(self):
        return self._events

    def get_validator(self):
        return self._validator

    #-----------------------------------

    def create_adress(self, city, street, number):
        """
        creates Adress object
        
        Args:
            city (str): a city name
            street (str): a street name
            number (str): a house number
        
        Returns:
            Adress: an adress
        """
        __city = CityName(city)
        __street = StreetName(street)
        __number = Number(number)
        return Adress(__city, __street, __number)

    def create_person(self, id, name, adress):
        """
        creates Person object
        
        Args:
            id (str): an id
            name (str): a name
            adress (Adress): an adress
        
        Returns:
            Person: a person
        """
        __id = Id(id)
        __name = Name(name)
        return Person(__id, __name, adress)

    def create_date(self, day, month, year):
        __day = Day(day)
        __month = Month(month)
        __year = Year(year)
        return Date(__day, __month, __year)

    def create_duration(self, hours, minutes):
        __hours = Hours(hours)
        __minutes = Minutes(minutes)
        return Duration(__hours, __minutes)

    def create_event(self, id, date, duration, description):
        __id = Id(id)
        __description = Description(description)
        return Event(__id, date, duration, __description)

    #-----------------------------------

    def add_person_to_repo(self, repo, id, name, city, street, number):
        """
        adds person with the given data in repo
        
        Args:
            repo (Repo): a repo
            id (str): an id
            name (str): a name
            city (str): a city name
            street (str): a street name
            number (str): a house number
        
        Raises:
            Exception: invalid person
        
        Returns:
            Repo: newly modified repo
        """
        try:
            person = self.create_person(id, name, self.create_adress(city, street, number))
            self.get_validator().validate_person(person)
            self.get_persons().add(person)
            return repo
        except Exception as ex:
            raise Exception(ex)

    def add_event_to_repo(self, repo, id, day, month, year, hours, minutes, description):
        try:
            event = self.create_event(id, self.create_date(day, month, year), self.create_duration(hours, minutes), description)
            self.get_validator().validate_event(event)
            self.get_events().add(event)
            return repo
        except Exception as ex:
            raise Exception(ex)