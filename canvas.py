import numpy as np
from PIL import Image


class Canvas:
    """
    Canvas object where all Shape objects will be rendered
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
        Convert current array into an image file
        """
        img = Image.fromarray(self.data, 'RGB')
        img.save(f"files/{image_path}.png")
