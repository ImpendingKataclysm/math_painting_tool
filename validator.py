class Validator:
    """
    Ensures that user inputs are compatible with the program by handling exceptions
    resulting from faulty inputs.
    """
    @staticmethod
    def get_valid_numerical_input(prompt):
        """
        Converts user input to an integer and displays an error message if the
        user enters a value that cannot be converted to an integer.
        :param prompt: String that prompts the user for input.
        :return: The Integer value entered by the user, or 0 if the user enters
        a value that cannot be converted.
        """
        num_input = 0
        try:
            num_input = int(input(prompt))
        except ValueError:
            print("We were unable to process that! Please enter a numerical value.")

        return num_input

    def get_positive_numerical_input(self, prompt):
        """
        Checks that an integer input is positive and not zero, and continues to
        prompt the user for input until they enter a positive, nonzero numerical
        value.
        :param prompt: String that prompts the user for input.
        :return: Integer value entered by the user.
        """
        num_input = self.get_valid_numerical_input(prompt)

        while num_input <= 0:
            if num_input < 0:
                print("Please enter a positive number!")
            num_input = self.get_valid_numerical_input(prompt)

        return num_input
