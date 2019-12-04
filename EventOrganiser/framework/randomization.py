from EventOrganiser.domain.exceptions import NotIntParameterException


class Random:
    import random

    def int_in_range(self, start: int, stop: int):
        try:
            return self.random.randint(start, stop)
        except:
            raise NotIntParameterException

    def string_of_chr(self, length: int):
        try:
            string = ""
            for _ in range(0, length):
                string += chr(self.int_in_range(ord('A'), ord('z')))
            return string
        except:
            raise NotIntParameterException

    def string_of_int(self, length: int):
        try:
            string = ""
            for _ in range(0, length):
                string += chr(self.int_in_range(0, 9))
            return string
        except:
            raise NotIntParameterException
