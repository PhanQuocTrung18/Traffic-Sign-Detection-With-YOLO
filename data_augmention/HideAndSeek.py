import random
import numpy as np
from PIL import Image

class HideAndSeek:
    def __init__(self, hide_prob=0.05):
        self.hide_prob = hide_prob
        self.grid_sizes = random.sample(range(5, 15, 2), 5)
        
    def __call__(self, image):
        return self.hide_patches(image)
        
    def hide_patches(self, image):
        image = image.convert('RGB')
        images = np.array(image)
        
        width, height = image.size
        grid_size = self.grid_sizes[random.randint(0, len(self.grid_sizes) - 1)]
        
        if grid_size != 0:
            for x in range(0, width, grid_size):
                for y in range(0, height, grid_size):
                    x_end = min(width, x + grid_size)
                    y_end = min(height, y + grid_size)
                    if random.random() <= self.hide_prob:
                        images[y:y_end, x:x_end, :] = 0  # Note: NumPy array indexing is height (y) first
                    
        augmented_image = Image.fromarray(images)
        return augmented_image



