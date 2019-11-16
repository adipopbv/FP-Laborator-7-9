from domain.entities import Id, Name, CityName, StreetName, Number, Adress, Person

class Validator:

    def validate_person(self, person):
        """
        validates the given person
        
        Args:
            person (Person): a person
        
        Raises:
            Exception: invalid person
        """
        if ( type(person.get_id()) != Id and person.get_id() < 0 and
            type(person.get_name()) != Name and
            type(person.get_adress()) != Adress and
            type(person.get_adress().get_city()) != CityName and
            type(person.get_adress().get_street()) != StreetName and
            type(person.get_adress().get_number()) != Number ):
            raise Exception("Invalid person!")