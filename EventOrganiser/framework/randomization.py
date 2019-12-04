class Random:
    import random

    def int_in_range(self, start: int, stop: int):
        return self.random.randint(start, stop)

    def string_of_chr(self, length: int):
        string = ""
        for _ in range(0, length):
            string += chr(self.int_in_range(ord('A'), ord('z')))
        return string

    def string_of_int(self, length: int):
        string = ""
        for _ in range(0, length):
            string += chr(self.int_in_range(0, 9))
        return string
