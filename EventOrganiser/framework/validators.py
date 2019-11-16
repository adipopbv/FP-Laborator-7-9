from domain.entities import Id, Name, CityName, StreetName, Number, Adress, Person
from domain.entities import Day, Month, Year, Date, Hours, Minutes, Duration, Description, Event

class Validator:

    def validate_person(self, repo, person):
        """
        validates the given person
        
        Args:
            person (Person): a person
        
        Raises:
            Exception: invalid person
        """
        if (type(person.get_id()) != Id and person.get_id() < 0 and
            type(person.get_name()) != Name and
            type(person.get_adress()) != Adress and
            type(person.get_adress().get_city()) != CityName and
            type(person.get_adress().get_street()) != StreetName and
            type(person.get_adress().get_number()) != Number ):
            raise Exception("Invalid person!")
        ok = None
        try:
            ok = repo.get_item_with_id_value(person.get_id().get_value())
        except:
            pass
        if ok != None:
            raise Exception("Invalid person!")

    def validate_event(self, repo, event):
        """
        validates the given event
        
        Args:
            event (Event): a event
        
        Raises:
            Exception: invalid event
        """
        if ( type(event.get_id()) != Id and event.get_id() < 0 and
            type(event.get_date().get_day()) != Day and
            type(event.get_date().get_month()) != Month and
            type(event.get_date().get_year()) != Year and
            type(event.get_duration().get_hours()) != Hours and
            type(event.get_duration().get_minutes()) != Minutes and
            type(event.get_gescription()) != Description):
            raise Exception("Invalid event!")
        ok = None
        try:
            ok = repo.get_item_with_id_value(event.get_id().get_value())
        except:
            pass
        if ok != None:
            raise Exception("Invalid event!")