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
canvas = canvas_creator.create_canvas()

# Prompt user to generate the shapes:
while True:
    # Get type of Shape to draw
    print("Choose one of the following shapes to draw!")
    shape_to_draw = canvas_validator.get_list_select_input(choice_list=SHAPES,
                                                           prompt="Enter shape: "
                                                           ).strip().lower()

    # Get Shape origin coordinates
    print(f"Where would you like to put your {shape_to_draw} on the canvas grid?")
    origin_x = canvas_validator.get_positive_numerical_input("Starting X-Coordinate: ")
    origin_y = canvas_validator.get_positive_numerical_input("Starting Y-Coordinate: ")

    # Get Shape color
    print(f"What color is your {shape_to_draw}? Choose the RGB values:")
    red = canvas_validator.get_number_in_range(0, 255, "How much red? ")
    green = canvas_validator.get_number_in_range(0, 255, "How much green? ")
    blue = canvas_validator.get_number_in_range(0, 255, "How much blue? ")

    # Get Shape dimensions based on Shape type
    if shape_to_draw == 'rectangle':
        width = canvas_validator.get_number_in_range(0, canvas.width + 1,
                                                     "How wide is your rectangle? ")
        height = canvas_validator.get_number_in_range(0, canvas.height + 1,
                                                      "How tall is your rectangle? ")
        rect = Rectangle(origin_x, origin_y, width, height, (red, green, blue))
        rect.draw(canvas=canvas)
    elif shape_to_draw == 'square':
        side_length = canvas_validator.get_positive_numerical_input("How long are the sides?")
        square = Square(origin_x, origin_y, side_length, (red, green, blue))
        square.draw(canvas=canvas)
    else:
        print("Sorry, we can't draw that shape!")

    # Ask if the user wants to draw another image or save and exit the program
    keep_drawing = input("Draw another shape? (y/n)").strip().lower()

    if keep_drawing == 'n' or keep_drawing == 'no' or keep_drawing == 'stop':
        break

# Save the canvas
canvas.make(image_path=img_name)


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
