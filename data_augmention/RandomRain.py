"""
Writer: Phan Quốc Trung
"""
import random
import numpy as np
from PIL import Image
import albumentations as A

class RandomRain:
    def __init__(self, drop_length=20, drop_width=1, drop_color=(200, 200, 200),
                 blur_value=4, brightness_coefficient=0.9):
        self.drop_length = drop_length
        self.drop_width = drop_width
        self.drop_color = drop_color
        self.blur_value = blur_value
        self.brightness_coefficient = brightness_coefficient

    def __call__(self, image):
        slant_lower = random.randint(-20, 0)
        slant_upper = random.randint(0, 20)
        rain_types = ['drizzle', 'heavy', 'torrential']
        rain_type = random.choice(rain_types)

        img_np = np.array(image)

        transform = A.Compose([
            A.RandomRain(
                p=1.0, 
                slant_lower=slant_lower, 
                slant_upper=slant_upper,
                drop_length=self.drop_length, 
                drop_width=self.drop_width, 
                drop_color=self.drop_color,
                blur_value=self.blur_value, 
                brightness_coefficient=self.brightness_coefficient,
                rain_type=rain_type
            ),
        ])

        augmented = transform(image=img_np)
        augmented_image = Image.fromarray(augmented['image'])

        return augmented_image

    def replace_bbox_in_image(self, image, original_bbox, augmented_image):
        x_min, y_min, x_max, y_max = original_bbox
        rain_image = np.array(augmented_image)
        image[y_min:y_max, x_min:x_max] = rain_image
        return image


