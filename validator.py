class Validator:
    """
    Ensures that user inputs are compatible with the program and handles exceptions
    resulting from faulty inputs.
    """
    @staticmethod
    def get_valid_numerical_input(prompt):
        """
        Converts user input to an integer. If the user enters a value that cannot be
        converted to an integer, an error message is displayed. Continues prompting the
        user for valid numerical input until they enter a value that can be converted to an
        integer.
        :param prompt: String that prompts the user for input.
        :return: The Integer value entered by the user, or 0 if the user enters a value that
        cannot be converted.
        """
        while True:
            try:
                num_input = int(input(prompt))
                break
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

        while num_input < 0:
            print("Please enter a positive number!")
            num_input = self.get_valid_numerical_input(prompt)

        return num_input

    def get_number_in_range(self, lower, upper, prompt):
        """
        Prompt the user to enter a number and ensure that it falls between the specified
        lower and upper values. If the number is outside the accepted range, continue to
        prompt the user until they enter a value that falls within the range.
        :param lower: minimum accepted value
        :param upper: maximum accepted value
        :param prompt: String that prompts the user for input.
        :return: the number entered by the user
        """
        number = self.get_valid_numerical_input(prompt)

        while number not in range(lower, upper + 1):
            print(f"Please enter a number between {lower} and {upper} inclusive")
            number = self.get_valid_numerical_input(prompt)

        return number

    @staticmethod
    def get_list_select_input(choice_list, prompt):
        """
        Displays a list of choices to the user and prompts them to select an option. The user's
        choice is then checked to ensure that it is an option in the list. The user will be
        prompted to keep making choices until they make a choice that is listed.
        :param choice_list: The list of options available for the user to choose from
        :param prompt: String that prompts the user for input.
        :return: The user's selection from the list
        """
        for choice in choice_list:
            print(f"\t{choice.title()}")
        user_choice = input(prompt).strip().lower()

        while user_choice not in choice_list:
            print(f"Sorry, {user_choice} is not an available option.")
            user_choice = input(prompt).strip().lower()

        return user_choice
