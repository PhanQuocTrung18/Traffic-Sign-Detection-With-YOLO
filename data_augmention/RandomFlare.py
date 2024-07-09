"""
Writer: Phan Quốc Trung
"""
import random
import numpy as np
from PIL import Image
import albumentations as A

class RandomFlare:
    def __init__(self, flare_roi=(0, 0, 1, 0.5), src_color=(255, 255, 255)):
        self.flare_roi = flare_roi
        self.src_color = src_color

    def __call__(self, image):
        angle_upper = random.uniform(0, 1)
        num_flare_circles_lower = random.randint(3, 8)
        num_flare_circles_upper = random.randint(9, 15)
        src_radius = random.randint(100, 200)

        img_np = np.array(image)

        transform = A.Compose([
            A.RandomSunFlare(
                p=1.0, 
                flare_roi=self.flare_roi, 
                angle_lower=0, 
                angle_upper=angle_upper, 
                num_flare_circles_lower=num_flare_circles_lower, 
                num_flare_circles_upper=num_flare_circles_upper, 
                src_radius=src_radius, 
                src_color=self.src_color
            ),
        ])

        augmented = transform(image=img_np)
        augmented_image = Image.fromarray(augmented['image'])

        return augmented_image

    def replace_bbox_in_image(self, image, original_bbox, augmented_image):
        x_min, y_min, x_max, y_max = original_bbox
        flare_image = np.array(augmented_image)
        image[y_min:y_max, x_min:x_max] = flare_image
        return image

