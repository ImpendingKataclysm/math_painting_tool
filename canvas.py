import numpy as np

from PIL import Image


class Canvas:
    """
    Numpy array image generated based on width, height and color parameter that
    is saved as a PNG image file.
    """
    def __init__(self, width, height, color):
        self.color = color
        self.height = height
        self.width = width

        # Create 3d numpy array
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)

        # Change default (0, 0, 0) color with user-given color value
        self.data[:] = self.color

    def make(self, image_path):
        """
        Creates an image from the numpy array and saves it as a PNG file.
        :param image_path: the filename under which to save the image.
        :return:
        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(f"files/{image_path}.png")


class CanvasCreator:
    """
    Generates a Canvas with width, height and background color parameters entered
    by the user. Instantiated with a dictionary of available color names and
    their corresponding RGB values, a file path under which the image will be
    saved, and a Validator to check user inputs.
    """
    def __init__(self, color_list, img_path, validator):
        self.colors = color_list
        self.img_path = img_path
        self.validator = validator

    def get_canvas_width(self):
        """
        Prompt the user to enter the canvas width in pixels and validate the
        input to ensure it can be used as a width value.
        :return: The user inpt as a valid integer.
        """
        prompt = "Enter canvas width (px): "
        return self.validator.get_positive_numerical_input(prompt)

    def get_canvas_height(self):
        """
         Prompt the user to enter the canvas height in pixels and validate the
        input to ensure it can be used as a height value.
        :return: The user inpt as a valid integer.
        """
        prompt = "Enter canvas height (px): "
        return self.validator.get_positive_numerical_input(prompt)

    def get_canvas_color(self):
        """
        Prompts the user to select the background color from a list of available
        colors and checks that the user input is on the list.
        :return: The color selected by the user
        """
        print("Choose your background color!")
        print("Available options are:")
        color_names = list(self.colors.keys())
        for color in color_names:
            print(f"\t{color.title()}")
        canvas_color = input("Enter background color: ").strip().lower()

        while canvas_color not in color_names:
            print(f"Sorry, {canvas_color} is not an available background color.")
            canvas_color = input("Enter background color: ").strip().lower()

        return self.colors[canvas_color]

    def create_canvas(self):
        """
        Generates the canvas with the user-entered parameters and saves it as
        an image file.
        :return:
        """
        canvas_width = self.get_canvas_width()
        canvas_height = self.get_canvas_height()
        bg_color = self.get_canvas_color()
        canvas = Canvas(width=canvas_width, height=canvas_height, color=bg_color)
        canvas.make(self.img_path)
