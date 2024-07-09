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

# import random
# from PIL import Image
# import numpy as np

# class GaussianNoise:
#     def __init__(self, mean_range=(-10, 10), std_range=(0, 1)):
#         self.mean = random.uniform(*mean_range)
#         self.std = random.uniform(*std_range)

#     def __call__(self, image):
#         img_array = np.array(image)
#         noise = np.random.normal(self.mean, self.std, img_array.shape).astype(np.int16)
#         noisy_image = Image.fromarray(np.clip(img_array + noise, 0, 255).astype(np.uint8))
#         return noisy_image

"""
# Writer: Phan Quốc Trung
# """
# import random
# from PIL import Image
# import numpy as np

# class GaussianNoise:
#     def __init__(self, mean=0, std=10):
#         self.mean = mean
#         self.std = std

#     def __call__(self, image):
#         img_array = np.array(image)
#         noise = np.random.normal(self.mean, self.std, img_array.shape).astype(np.uint8)
#         noisy_image = Image.fromarray(np.clip(img_array + noise, 0, 255))
#         return noisy_image

