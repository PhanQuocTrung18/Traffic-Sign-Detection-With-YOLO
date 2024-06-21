"""
Writer: Phan Quốc Trung
"""
import random
import numpy as np
from PIL import Image
import albumentations as A

class RandomSnow:
    def __init__(self, brightness_coeff=2.5):
        self.brightness_coeff = brightness_coeff

    def __call__(self, image):
        snow_point_lower = random.uniform(0.2, 1)
        snow_point_upper = random.uniform(snow_point_lower, 1)

        img_np = np.array(image)

        random.seed(42)
        
        transform = A.Compose([
            A.RandomSnow(brightness_coeff=self.brightness_coeff, snow_point_upper=snow_point_upper, 
                         snow_point_lower=snow_point_lower, p=1),
        ])

        augmented = transform(image=img_np)
        augmented_image = Image.fromarray(augmented['image'])

        return augmented_image

    def replace_bbox_in_image(self, image, original_bbox, augmented_image):
        x_min, y_min, x_max, y_max = original_bbox
        flare_image = np.array(augmented_image)
        image[y_min:y_max, x_min:x_max] = flare_image
        return image
