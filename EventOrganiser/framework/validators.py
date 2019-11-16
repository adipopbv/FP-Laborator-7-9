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
            type(person.get_adress().get_city()) != Id and
            type(person.get_adress().get_street()) != Id and
            type(person.get_adress().get_number()) != Id ):
            raise Exception("Invalid person!")