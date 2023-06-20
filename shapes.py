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
        Draw the shape on the given canvas
        """
        # Change a slice of the canvas RGB array with new values
        canvas.data[self.x:self.x + self.height, self.y:self.y + self.width] = self.color


class Rectangle(Shape):
    """
    Extends the Shape class to render a Rectangle object with a width and height.
    Includes a method for drawing the Rectangle to a canvas
    """
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, width, height, color)


class Square(Rectangle):
    """
    Extends the Shape class to render a Square object with a side length. Includes
    a method for drawing the Square to a canvas
    """
    def __init__(self, x, y, side_length, color):
        super().__init__(x, y, side_length, side_length, color)
