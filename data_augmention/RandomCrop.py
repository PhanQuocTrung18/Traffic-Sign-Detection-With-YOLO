import random
from PIL import Image
import numpy as np

class RandomCrop:
    def __init__(self, crop_ratio_range=(0.7, 1.0)):
        self.crop_ratio_range = crop_ratio_range

    def __call__(self, image, label_content):
        img_array = np.array(image)
        width, height = image.size
        x_min, y_min, x_max, y_max = 0, 0, width, height
        cropped_bbox = self.crop_bbox((x_min, y_min, x_max, y_max))
        img_array, updated_label_content = self.replace_bbox_in_image(img_array, (x_min, y_min, x_max, y_max), cropped_bbox, label_content)
        augmented_image = Image.fromarray(img_array)
        return augmented_image, updated_label_content

    def crop_bbox(self, bbox):
        x_min, y_min, x_max, y_max = bbox
        width = x_max - x_min
        height = y_max - y_min
        crop_ratio = random.uniform(*self.crop_ratio_range)
        new_width = int(width * crop_ratio)
        new_height = int(height * crop_ratio)
        x_start = random.randint(0, width - new_width)
        y_start = random.randint(0, height - new_height)
        new_x_min = x_min + x_start
        new_y_min = y_min + y_start
        new_x_max = new_x_min + new_width
        new_y_max = new_y_min + new_height
        return new_x_min, new_y_min, new_x_max, new_y_max

    def replace_bbox_in_image(self, image, original_bbox, cropped_bbox, label_content):
        x_min, y_min, x_max, y_max = original_bbox
        cropped_x_min, cropped_y_min, cropped_x_max, cropped_y_max = cropped_bbox

        # Create a black image to replace the cropped region
        black_image = np.zeros((y_max - y_min, x_max - x_min, 3), dtype=np.uint8)

        # Calculate offsets to place the cropped region in the black image
        x_offset = (black_image.shape[1] - (cropped_x_max - cropped_x_min)) // 2
        y_offset = (black_image.shape[0] - (cropped_y_max - cropped_y_min)) // 2

        # Copy the cropped region from original image to the black image
        black_image[y_offset:y_offset + (cropped_y_max - cropped_y_min),
                    x_offset:x_offset + (cropped_x_max - cropped_x_min)] = \
            image[cropped_y_min:cropped_y_max, cropped_x_min:cropped_x_max]

        # Update label content with adjusted bounding box coordinates
        lines = label_content.strip().split('\n')
        updated_lines = []

        for line in lines:
            if line.strip() == '':
                continue  # Skip empty lines

            parts = line.split()
            if len(parts) != 5:
                print(f"Issue with line: {line}. Skipping...")
                continue  # Skip lines that do not have exactly 5 parts

            try:
                class_id, x_center, y_center, bbox_width, bbox_height = map(float, parts)
            except ValueError as e:
                print(f"Error parsing line: {line}. Skipping... Error: {e}")
                continue

            # Adjust bounding box coordinates if necessary
            if (cropped_x_min <= x_center <= cropped_x_max) and (cropped_y_min <= y_center <= cropped_y_max):
                new_x_center = (x_center - cropped_x_min + x_offset) / (cropped_x_max - cropped_x_min) * black_image.shape[1]
                new_y_center = (y_center - cropped_y_min + y_offset) / (cropped_y_max - cropped_y_min) * black_image.shape[0]
                new_bbox_width = bbox_width * (black_image.shape[1] / (cropped_x_max - cropped_x_min))
                new_bbox_height = bbox_height * (black_image.shape[0] / (cropped_y_max - cropped_y_min))

                # Update label line with adjusted coordinates
                updated_line = f"{int(class_id)} {new_x_center} {new_y_center} {new_bbox_width} {new_bbox_height}"
                updated_lines.append(updated_line)
            else:
                updated_lines.append(line)

        updated_label_content = '\n'.join(updated_lines)
        return black_image, updated_label_content

