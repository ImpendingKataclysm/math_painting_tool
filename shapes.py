class Shape:
    """
    An object to be rendered on a canvas. Attributes include x- and y-coordinates
    and a color.
    """
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color


class Square(Shape):
    """
    Extends the Shape class to render a Square object with a side length. Includes
    a method for drawing the Square to a canvas
    """
    def __init__(self, side_length, x, y, color):
        super().__init__(x, y, color)
        self.side_length = side_length

    def draw(self, canvas):
        pass


class Rectangle(Shape):
    """
    Extends the Shape class to render a Rectangle object with a width and height.
    Includes a method for drawing the Rectangle to a canvas
    """
    def __init__(self, width, height, x, y, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def draw(self, canvas):
        pass
