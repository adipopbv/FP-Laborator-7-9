from domain.entities import Id, Name, CityName, StreetName, Number, Adress, Person

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