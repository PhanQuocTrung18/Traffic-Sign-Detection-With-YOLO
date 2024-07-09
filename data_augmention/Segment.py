import cv2
import numpy as np
from PIL import Image

class MeanShiftSegmentation:
    def __init__(self, spatial_radius=30, color_radius=30, max_pyramid_level=1):
        self.spatial_radius = spatial_radius  # Spatial radius
        self.color_radius = color_radius      # Color radius
        self.max_pyramid_level = max_pyramid_level  # Maximum pyramid level

    def __call__(self, image):
        # Convert PIL image to OpenCV format
        img_array = np.array(image)
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

        # Apply Mean Shift Segmentation
        segmented_image = cv2.pyrMeanShiftFiltering(
            img_bgr, self.spatial_radius, self.color_radius, self.max_pyramid_level
        )

        # Convert back to RGB format
        segmented_image_rgb = cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB)

        # Convert back to PIL Image
        segmented_image_pil = Image.fromarray(segmented_image_rgb)

        return segmented_image_pil