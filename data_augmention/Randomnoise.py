import random
import numpy as np
from PIL import Image

class GaussianNoise:
    def __init__(self, mean=0.1, stddev_min=10, stddev_max=50):
        self.mean = mean
        self.stddev_min = stddev_min
        self.stddev_max = stddev_max

    def __call__(self, image):
        img_array = np.array(image)
        stddev = random.uniform(self.stddev_min, self.stddev_max)  # Chọn ngẫu nhiên độ lệch chuẩn trong khoảng cho phép
        noise = np.random.normal(self.mean, stddev, img_array.shape).astype(np.float32)
        
        # Đảm bảo giá trị trong khoảng [0, 255] và chuyển đổi thành kiểu uint8
        noisy_image = Image.fromarray(np.clip(img_array + noise, 0, 255).astype(np.uint8))
        
        return noisy_image
