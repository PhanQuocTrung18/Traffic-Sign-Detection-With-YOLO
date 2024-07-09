import json
import os
import random
import shutil

json_file_path = r'C:\Users\LAPTOP\Traffic_Sign_Detection\via-trafficsign-coco-20210321\annotations\train.json'
image_directory = r'C:\Users\LAPTOP\Traffic_Sign_Detection\Data Converted\train\images'
output_image_directory = r'C:\Users\LAPTOP\Traffic_Sign_Detection\Data(-80%)_bbox_area\train'
os.makedirs(output_image_directory, exist_ok=True)

with open(json_file_path, 'r') as f:
    data = json.load(f)

image_paths = []
category_count = {}
invalid_annotations = []

for annotation in data['annotations']:
    bbox = annotation['bbox']
    width = bbox[2]
    height = bbox[3]
    bbox_size = width * height
    
    if 5040 <= bbox_size <= 6250:
        image_id = annotation['image_id']
        for image in data['images']:
            if image['id'] == image_id:
                image_path = image['file_name']
                full_image_path = os.path.join(image_directory, image_path)
                image_paths.append((full_image_path, annotation))
                
                category_id = annotation['category_id']
                if category_id in category_count:
                    category_count[category_id].append(annotation)
                else:
                    category_count[category_id] = [annotation]
                break
    else:
        invalid_annotations.append(annotation)

num_images = len(image_paths)
print(f"Number of images with bounding box size between 5040 and 6250 pixels: {num_images}")

filtered_annotations = []
for category_id, annotations in category_count.items():
    random.shuffle(annotations)
    filtered_annotations.extend(annotations[:int(len(annotations) * 0.2)])

for annotation in invalid_annotations:
    image_id = annotation['image_id']
    for image_info in data['images']:
        if image_info['id'] == image_id:
            image_path = image_info['file_name']
            full_image_path = os.path.join(image_directory, image_path)
            new_image_path = os.path.join(output_image_directory, image_path)
            shutil.copy(full_image_path, new_image_path)
            break

final_annotations = filtered_annotations + invalid_annotations

filtered_data = {
    "images": data['images'],
    "annotations": final_annotations,
    "categories": data['categories']
}

filtered_json_file_path = r'C:\Users\LAPTOP\Traffic_Sign_Detection\Data(-80%)_bbox_area\annotations\train.json'

with open(filtered_json_file_path, 'w') as f:
    json.dump(filtered_data, f)

print(f"Filtered data saved to {filtered_json_file_path}")
