from EventOrganiser.framework.json_tools import JsonFormattable


class Address(JsonFormattable):

    _city: str
    @property
    def city(self):
        return self._city
    @city.setter
    def city(self, value):
        self._city = value

    _street: str
    @property
    def street(self):
        return self._street
    @street.setter
    def street(self, value):
        self._street = value

    _number: str
    @property
    def number(self):
        return self._number
    @number.setter
    def number(self, value):
        self._number = value

    def __init__(self, city: str, street: str, number: str):
        self.city = city
        self.street = street
        self.number = number

    def to_json(self):
        return {
            "city": self.city,
            "street": self.street,
            "number": self.number
        }


class Date(JsonFormattable):

    _day: str
    @property
    def day(self):
        return self._day
    @day.setter
    def day(self, value):
        self._day = value

    _month: str
    @property
    def month(self):
        return self._month
    @month.setter
    def month(self, value):
        self._month = value

    _year: str
    @property
    def year(self):
        return self._year
    @year.setter
    def year(self, value):
        self._year = value

    def __init__(self, day: str, month: str, year: str):
        self.day = day
        self.month = month
        self.year = year

    def to_json(self):
        return {
            "day": self.day,
            "month": self.month,
            "year": self.year
        }
