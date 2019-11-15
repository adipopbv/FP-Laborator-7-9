from framework.repos import Repo

class Field:
    
    def __init__(self, name):
        self._name = name

    def get_name(self):
        return self._name

class SingleField(Field):
    
    def __init__(self, name, value):
        Field.__init__(self, name)
        self._value = value

    def get_value(self):
        return self._value

class MultiField(Field):

    def __init__(self, name, *fields):
        Field.__init__(self, name)
        self._fields = fields

    def get_fields(self):
        return self._fields

    def get_field_with_name(self, name):
        for field in self.get_fields():
            if field.get_name() == name:
                return field
        return None

# class ID(SoloField):

#     def __init__(self, id):
#         Field.__init__(self, id)

# class Name(SoloField):

#     def __init__(self, name):
#         Field.__init__(self, name)

# class Adress(MultiField):

#     def __init__(self, city, street, number):
#         self._city = city
#         self._street = street
#         self._number = number

#     def get_city(self):
#         return self._city

#     def get_street(self):
#         return self._street

#     def get_number(self):
#         return self._number

# class Date(MultiField):

#     def __init__(self, day, month, year):
#         self._day = day
#         self._month = month
#         self._year = year
        
#     def get_day(self):
#         return self._day
        
#     def get_month(self):
#         return self._month
        
#     def get_year(self):
#         return self._year

# class Moment(MultiField):

#     def __init__(self, hour, minute, day, month, year):
#         self._hour = hour
#         self._minute = minute
#         Date.__init__(self, day, month, year)
        
#     def get_hour(self):
#         return self._hour

#     def get_minute(self):
#         return self._minute

# class Period(MultiField):

#     def __init__(self, start_moment, end_moment):
#         self._start_moment = start_moment
#         self._end_moment = end_moment

#     def get_start_moment(self):
#         return self._start_moment

#     def get_end_moment(self):
#         return self._end_moment

    
# class Description(SoloField):

#     def __init__(self, description):
#         Field.__init__(self, description)

# class ID:

#     def __init__(self, id):
#         self._id = id
#     def get_id(self):
#         return self._id

# class Name:

#     def __init__(self, name):
#         self._name = name
#     def get_name(self):
#         return self._name

class Adress:

    def __init__(self, city, street, number):
        self._city = city
        self._street = street
        self._number = number
    def get_city(self):
        return self._city
    def get_street(self):
        return self._street
    def get_number(self):
        return self._number

class Date:

    def __init__(self, day, month, year):
        self._day = day
        self._month = month
        self._year = year
    def get_day(self):
        return self._day
    def get_month(self):
        return self._month
    def get_year(self):
        return self._year

class Moment:

    def __init__(self, hour, minute, date):
        self._hour = hour
        self._minute = minute
        self._date = date
    def get_hour(self):
        return self._hour
    def get_minute(self):
        return self._minute
    def get_date(self):
        return self._date

class Period:

    def __init__(self, start_moment, stop_moment):
        self._start_moment = start_moment
        self._stop_moment = stop_moment
    def get_start_moment(self):
        return self._start_moment
    def get_stop_moment(self):
        return self._stop_moment

# class Description:

#     def __init__(self, description):
#         self._description = description
#     def get_description(self):
#         return self._description



class FieldHolder:

    _fields = MultiField("fields", None)

    def __init__(self, *fields):
        self._fields = MultiField("fields", fields)

    def get_fields(self):
        return self._fields

    def get_field_with_name(self, name):
        return self.get_fields().get_field_with_name(name)

class Person(FieldHolder):
    
    _events = Repo()

    def __init__(self, id, name, adress):
        FieldHolder.__init__(
            self,
            SingleField("id", id),
            SingleField("name", name),
            MultiField("adress",
                SingleField("city", adress.get_city()),
                SingleField("street", adress.get_street()),
                SingleField("number", adress.get_number())
            )
        )

    def get_id(self):
        return self.get_fields().get_field_with_name("id")

    def get_name(self):
        return self.get_fields().get_field_with_name("name")

    def get_adress(self):
        return self.get_fields().get_field_with_name("adress")

    def get_events(self):
        return self._events

class Event(FieldHolder):

    _persons = Repo()

    def __init__(self, id, date, period, description):
        FieldHolder.__init__(
            self,
            SingleField("id", id),
            MultiField("date", 
                SingleField("day", date.get_day()),
                SingleField("month", date.get_month()),
                SingleField("year", date.get_year())
            ),
            MultiField("period",
                MultiField("start_moment",
                    SingleField("hour", period.get_start_moment().get_hour()),
                    SingleField("minute", period.get_start_moment().get_minute()),
                    MultiField("date", 
                        SingleField("day", period.get_start_moment().get_date().get_day()),
                        SingleField("month", period.get_start_moment().get_date().get_month()),
                        SingleField("year", period.get_start_moment().get_date().get_year())
                    ) 
                ),
                MultiField("stop_moment",
                    SingleField("hour", period.get_stop_moment().get_hour()),
                    SingleField("minute", period.get_stop_moment().get_minute()),
                    MultiField("date", 
                        SingleField("day", period.get_stop_moment().get_date().get_day()),
                        SingleField("month", period.get_stop_moment().get_date().get_month()),
                        SingleField("year", period.get_stop_moment().get_date().get_year())
                    ) 
                )
            ),
            SingleField("description", description)
        )

    def get_id(self):
        return self.get_fields().get_field_with_name("id")
    
    def get_date(self):
        return self.get_fields().get_field_with_name("date")

    def get_period(self):
        return self.get_fields().get_field_with_name("period")

    def get_description(self):
        return self.get_fields().get_field_with_name("description")

    def get_persons(self):
        return self._persons



# class Command(FieldHolder):

#     def __init__(self):
#         pass

class PickCommand(FieldHolder):

    def __init__(self, id, function):
        field1 = SingleField("id", id)
        field2 = SingleField("function", function)
        FieldHolder.__init__(field1, field2)

    def run(self):
        self.get_field_with_name("function").get_value()()