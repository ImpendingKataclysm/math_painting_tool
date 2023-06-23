from canvas import CanvasCreator
from validator import Validator
from shapes import SHAPES, Square, Rectangle

# Set canvas parameters
bg_colors = {
    "white": (255, 255, 255),
    "black": (0, 0, 0),
    "blue": (0, 0, 250),
}

img_name = 'my_image'
canvas_validator = Validator()

# Generate the canvas
canvas_creator = CanvasCreator(bg_colors, img_name, canvas_validator)
canvas_creator.create_canvas()

# Prompt user to generate the shapes:
while True:
    print("Choose one of the following shapes to draw!")

    shape_to_draw = canvas_validator.get_list_select_input(choice_list=SHAPES,
                                                           prompt="Enter shape: ")

    keep_drawing = input("Draw another shape? (y/n)").strip().lower()

    if keep_drawing == 'n' or keep_drawing == 'no' or keep_drawing == 'stop':
        break


# square = Square(20, 10, 20, (255, 0, 0))
# rectangle = Rectangle(40, 50, 30, 50, (100, 0, 100))
# canvas = Canvas(200, 200, (250, 250, 250))
#
# print(f"{square.width} {square.color} ({square.x}, {square.y})")
# print(f"{rectangle.width} {rectangle.height} {rectangle.color} ({rectangle.x}, {rectangle.y})")
# print(canvas.data)
#
# rectangle.draw(canvas)
# square.draw(canvas)
# canvas.make('surface')
