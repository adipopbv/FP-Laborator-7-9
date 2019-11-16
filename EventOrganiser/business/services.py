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
        """
        creates Date object
        
        Args:
            day (str): a day
            month (str): a month
            year (str): a year
        
        Returns:
            Date: a date
        """
        __day = Day(day)
        __month = Month(month)
        __year = Year(year)
        return Date(__day, __month, __year)

    def create_duration(self, hours, minutes):
        """
        creates Duration object
        
        Args:
            hours (str): number of hours
            minutes (str): number of minutes
        
        Returns:
            Duration: duration
        """
        __hours = Hours(hours)
        __minutes = Minutes(minutes)
        return Duration(__hours, __minutes)

    def create_event(self, id, date, duration, description):
        """
        create Event object
        
        Args:
            id (str): an id
            date (Date): a date
            duration (Duration): a duration
            description (str): a description
        
        Returns:
            Event: an event
        """
        __id = Id(id)
        __description = Description(description)
        return Event(__id, date, duration, __description)

    #-----------------------------------

    def add_person_to_repo(self, repo, id, name, city, street, number):
        """
        adds person with the given data in repo
        
        Args:
            repo (IdRepo): a repo
            id (str): an id
            name (str): a name
            city (str): a city name
            street (str): a street name
            number (str): a house number
        
        Raises:
            Exception: allready existing id / invalid person
        
        Returns:
            IdRepo: newly modified repo
        """
        try:
            person = self.create_person(id, name, self.create_adress(city, street, number))
            self.get_validator().validate_person(repo, person)
            repo.add(person)
            return repo
        except Exception as ex:
            raise Exception(ex)

    def add_event_to_repo(self, repo, id, day, month, year, hours, minutes, description):
        """
        adds event with the given data in repo
        
        Args:
            repo (IdRepo): a repo
            id (str): an id
            day (str): a day
            month (str): a month
            year (str): a year
            hours (str): number of hours
            minutes (str): number of minutes
            description (str): a description
        
        Raises:
            Exception: allready existing id / invalid event
        
        Returns:
            IdRepo: newly modified repo
        """
        try:
            event = self.create_event(id, self.create_date(day, month, year), self.create_duration(hours, minutes), description)
            self.get_validator().validate_event(repo, event)
            repo.add(event)
            return repo
        except Exception as ex:
            raise Exception(ex)

    def modify_person_from_repo(self, repo, search_id, id, name, city, street, number):
        """
        modifies person with the given id to the given data in repo
        
        Args:
            repo (IdRepo): a repo
            search_id (str): an id
            id (str): an id
            name (str): a name
            city (str): a city
            street (str): a street
            number (str): a number
        
        Raises:
            Exception: no person with id / invalid person
        
        Returns:
            IdRepo: newly modified repo
        """
        try:
            person1 = self.get_persons().get_item_with_id_value(search_id)
            person2 = self.create_person(id, name, self.create_adress(city, street, number))
            self.get_validator().validate_person(repo, person2)
            repo.replace(person1, person2)
            return repo
        except Exception as ex:
            raise Exception(ex)

    def modify_event_from_repo(self, repo, search_id, id, day, month, year, hours, minutes, description):
        """
        modifies event with the given id to the given data in repo
        
        Args:
            repo (IdRepo): a repo
            search_id (str): an id
            id (str): an id
            day (str): a day
            month (str): a month
            year (str): a year
            hours (str): number of hours
            minutes (str): number of minutes
            description (str): a description
        
        Raises:
            Exception: no event with id / invalid event
        
        Returns:
            IdRepo: newly modified repo
        """
        try:
            event1 = self.get_events().get_item_with_id_value(search_id)
            event2 = self.create_event(id, self.create_date(day, month, year), self.create_duration(hours, minutes), description)
            self.get_validator().validate_event(repo, event2)
            repo.replace(event1, event2)
            return repo
        except Exception as ex:
            raise Exception(ex)

    def search_person_in_repo(self, repo, id):
        try:
            person = self.get_persons().get_item_with_id_value(id)
            return person
        except Exception as ex:
            raise Exception(ex)