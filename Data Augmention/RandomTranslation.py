import random
import numpy as np
from PIL import Image
from typing import List

class RandomTranslation:
    def __init__(self, max_transX: int = 15, max_transY: int = 15):
        self.max_transX = max_transX
        self.max_transY = max_transY

    def __call__(self, image: Image.Image):
        # Randomly generate translation amounts
        transX = random.randint(-self.max_transX, self.max_transX)
        transY = random.randint(-self.max_transY, self.max_transY)

        # Apply translation
        augmented_image = image.transform(image.size, Image.AFFINE, (1, 0, transX, 0, 1, transY))

        return augmented_image, transX, transY

    def replace_bbox_in_image(self, original_bbox: List[int], transX: int, transY: int):
        x_min, y_min, x_max, y_max = original_bbox

        # Adjust bounding box coordinates based on translation
        new_x_min = x_min + transX
        new_y_min = y_min + transY
        new_x_max = x_max + transX
        new_y_max = y_max + transY

        return [new_x_min, new_y_min, new_x_max, new_y_max]
