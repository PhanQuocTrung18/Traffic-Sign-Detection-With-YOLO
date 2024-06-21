"""
Writer: Phan Quốc Trung
"""
import random
from PIL import Image
import numpy as np

class GaussianNoise:
    def __init__(self, mean=0, std=10):
        self.mean = mean
        self.std = std

    def __call__(self, image):
        img_array = np.array(image)
        noise = np.random.normal(self.mean, self.std, img_array.shape).astype(np.uint8)
        noisy_image = Image.fromarray(np.clip(img_array + noise, 0, 255))
        return noisy_image