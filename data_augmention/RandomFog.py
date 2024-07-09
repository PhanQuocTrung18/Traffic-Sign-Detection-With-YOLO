"""
Writer: Phan Quốc Trung
"""
import random
import numpy as np
from PIL import Image
import albumentations as A

class RandomFog:
    def __init__(self):
        pass

    def __call__(self, image):
        fog_coef_lower = random.uniform(0.3, 0.5)
        fog_coef_upper = random.uniform(0.5, 0.9)
        alpha_coef = random.uniform(0.1, 0.5)

        img_np = np.array(image)

        transform = A.Compose([
            A.RandomFog(
                p=1.0, 
                fog_coef_lower=fog_coef_lower, 
                fog_coef_upper=fog_coef_upper,
                alpha_coef=alpha_coef
            ),
        ])

        augmented = transform(image=img_np)
        augmented_image = Image.fromarray(augmented['image'])

        return augmented_image

    def replace_bbox_in_image(self, image, original_bbox, augmented_image):
        x_min, y_min, x_max, y_max = original_bbox
        fog_image = np.array(augmented_image)
        image[y_min:y_max, x_min:x_max] = fog_image
        return image

