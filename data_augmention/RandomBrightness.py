"""
Writer: Phan Quốc Trung
"""
import random
import numpy as np
from PIL import Image
import albumentations as A

class RandomBrightnessContrast:
    def __init__(self, brightness_range=(-0.4, 0.4), contrast_range=(-0.5, 0.5)):
        self.brightness_range = brightness_range
        self.contrast_range = contrast_range

    def __call__(self, image):
        img_np = np.array(image)
        brightness_limit = random.uniform(*self.brightness_range)
        contrast_limit = random.uniform(*self.contrast_range)

        transform = A.Compose([
            A.RandomBrightnessContrast(
                brightness_limit=(brightness_limit, brightness_limit), 
                contrast_limit=(contrast_limit, contrast_limit), 
                p=1),
        ])

        augmented = transform(image=img_np)
        augmented_image = Image.fromarray(augmented['image'])

        return augmented_image

# """
# Writer: Phan Quốc Trung
# """
# import random
# import numpy as np
# from PIL import Image, ImageEnhance
# import albumentations as A

# class RandomBrightness:
#     def __init__(self, brightness_range=(0.85, 1.15)):
#         self.brightness_range = brightness_range

#     def __call__(self, image):
#         img_np = np.array(image)
#         brightness_factor = random.uniform(*self.brightness_range)

#         transform = A.Compose([
#             A.RandomBrightnessContrast(brightness_limit=(brightness_factor - 1, brightness_factor - 1), p=1),
#         ])

#         augmented = transform(image=img_np)
#         augmented_image = Image.fromarray(augmented['image'])

#         return augmented_image

    # def replace_bbox_in_image(self, image, original_bbox, augmented_image):
    #     x_min, y_min, x_max, y_max = original_bbox
    #     brightness_image_np = np.array(augmented_image)
    #     image[y_min:y_max, x_min:x_max] = brightness_image_np[y_min:y_max, x_min:x_max]
    #     return image
