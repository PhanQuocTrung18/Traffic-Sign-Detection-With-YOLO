"""
Writer: Phan Quốc Trung
"""
import random
import numpy as np
from PIL import Image
import albumentations as A

class RandomBlur:
    def __init__(self, max_kernel_size=5):
        self.max_kernel_size = max_kernel_size if max_kernel_size % 2 != 0 else max_kernel_size - 1

    def __call__(self, image):
        img_np = np.array(image)
        kernel_size = random.choice(range(1, self.max_kernel_size + 1, 2))
        transform = A.Compose([
            A.GaussianBlur(blur_limit=(kernel_size, kernel_size), p=1),
        ])
        augmented = transform(image=img_np)
        augmented_image = Image.fromarray(augmented['image'])
        return augmented_image

    def replace_bbox_in_image(self, image, original_bbox, augmented_image):
        x_min, y_min, x_max, y_max = original_bbox
        blur_image = np.array(augmented_image)
        image[y_min:y_max, x_min:x_max] = blur_image[y_min:y_max, x_min:x_max]
        return image
