class Console:

    def read(self, prompt):
        """
        gets input in the console
        
        Args:
            prompt (str): text to output before getting input
        
        Returns:
            str: input text
        """
        text = input(prompt)
        return text

    def write(self, message):
        """
        outputs message in the console
        
        Args:
            message (str): text to be outputted
        """
        print(message)