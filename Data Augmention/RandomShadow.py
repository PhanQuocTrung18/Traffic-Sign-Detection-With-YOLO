"""
Writer: Phan Quốc Trung
"""
import random
import numpy as np
from PIL import Image
import albumentations as A

class RandomShadow:
    def __init__(self):
        pass

    def __call__(self, image):

        img_np = np.array(image)
        
        x_min = random.uniform(0, 0.5)
        y_min = random.uniform(0, 0.5)
        x_max = random.uniform(0.5, 1)
        y_max = random.uniform(0.5, 1)
        
        x_min, x_max = min(x_min, x_max), max(x_min, x_max)
        y_min, y_max = min(y_min, y_max), max(y_min, y_max)
        
        shadow_roi = (x_min, y_min, x_max, y_max)
        num_shadows_lower = random.randint(1, 3)
        num_shadows_upper = random.randint(4, 6)
        shadow_dimension = random.randint(100, 300)
        
        transform = A.Compose([
            A.RandomShadow(p=1.0, shadow_roi=shadow_roi, num_shadows_lower=num_shadows_lower,
                           num_shadows_upper=num_shadows_upper, shadow_dimension=shadow_dimension),
        ], p=1.0)
        
        augmented = transform(image=img_np)
        augmented_image = Image.fromarray(augmented['image'])

        return augmented_image

    def replace_bbox_in_image(self, image, original_bbox, augmented_image):
        x_min, y_min, x_max, y_max = original_bbox
        shadow_image_np = np.array(augmented_image)
        image[y_min:y_max, x_min:x_max] = shadow_image_np[y_min:y_max, x_min:x_max]
        return image
