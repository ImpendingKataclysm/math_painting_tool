SHAPES = ["square", "rectangle"]


class Shape:
    """
    An object to be rendered on a canvas. Attributes include x- and y-coordinates
    and a color.
    """
    def __init__(self, x, y, width, height, color):
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = color

    def draw(self, canvas):
        """
        Draws the Shape onto a specified Canvas by changing the RGB values of
        the canvas to the Shape's background color, starting at the shape's
        origin and covering the Shape's surface area based on its width and
        height.
        :param canvas: The Canvas on which to draw the Shape
        :return:
        """
        x_slice = self.x + self.height
        y_slice = self.y + self.width
        # Change a slice of the canvas RGB array with new values
        canvas.data[self.x:x_slice, self.y:y_slice] = self.color


class Rectangle(Shape):
    """
    Extends the Shape class to render a Rectangle object with a width and height.
    Includes a method for drawing the Rectangle to a canvas
    """
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)


class Square(Rectangle):
    """
    Extends the Rectangle class to render a Square object with a side length.
    Includes a method for drawing the Square to a canvas
    """
    def __init__(self, x, y, side_length, color):
        super().__init__(x, y, side_length, side_length, color)
