import random
import numpy as np
from PIL import Image

class GridMask:
    def __init__(self, d_min=10, d_max=40, r_min=0.1, r_max=0.4):
        self.d_min = d_min  # Minimum distance between grid lines
        self.d_max = d_max  # Maximum distance between grid lines
        self.r_min = r_min  # Minimum ratio of masked area
        self.r_max = r_max  # Maximum ratio of masked area

    def __call__(self, image):
        img_array = np.array(image)
        height, width = img_array.shape[:2]

        d = random.randint(self.d_min, self.d_max)  # Distance between grid lines
        r = random.uniform(self.r_min, self.r_max)  # Ratio of masked area
        l = int(d * r)  # Length of the mask squares

        grid = np.ones((height, width), dtype=np.uint8)

        for i in range(0, height, d):
            for j in range(0, width, d):
                grid[i:i+l, j:j+l] = 0

        masked_image = img_array * grid[:, :, np.newaxis]
        masked_image = Image.fromarray(masked_image.astype(np.uint8))

        return masked_image