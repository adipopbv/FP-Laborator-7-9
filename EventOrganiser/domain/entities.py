class Command:

    def __init__(self, id, function):
        self._id = id
        self._function = function

    def get_id(self):
        return self._id

    def get_function(self):
        return self._function

    #--------------------------------

    def run(self):
        """
        runs the function
        """
        self.get_function()()