import os
import shutil
import matplotlib.pyplot as plt
import seaborn as sns

# Thư mục chứa các file YOLO annotation và hình ảnh
yolo_annotation_folder = "" # folder annotation
image_folder = "" # folder image
large_bbox_annotation_folder = "" # folder annotation for large bbox
large_bbox_image_folder = "" # folder image for large bbox

# Threshold for determining large bounding boxes (e.g., area greater than 0.1)
area_threshold = 0.1

def read_yolo_bbox(yolo_annotation_file):
    with open(yolo_annotation_file, 'r') as f:
        bboxes = []
        for line in f:
            class_id, x, y, w, h = map(float, line.strip().split())
            bboxes.append((class_id, x, y, w, h))
        return bboxes

# create folder for large bbox
os.makedirs(large_bbox_annotation_folder, exist_ok=True)
os.makedirs(large_bbox_image_folder, exist_ok=True)

# List to store areas of small bounding boxes
small_areas = []

for annotation_file in os.listdir(yolo_annotation_folder):
    yolo_annotation_file = os.path.join(yolo_annotation_folder, annotation_file)
    if os.path.isfile(yolo_annotation_file):
        bboxes = read_yolo_bbox(yolo_annotation_file)
        move_file = False
        for bbox in bboxes:
            _, _, _, w, h = bbox
            area = w * h
            if area > area_threshold:
                move_file = True
                break
            else:
                small_areas.append(area)
        
        if move_file:
            # move annotation file
            shutil.move(yolo_annotation_file, large_bbox_annotation_folder)
            
            # move file image
            image_file = annotation_file.replace('.txt', '.jpg') 
            image_path = os.path.join(image_folder, image_file)
            if os.path.exists(image_path):
                shutil.move(image_path, large_bbox_image_folder)
            else:
                print(f"Image file {image_file} not found, skipping.")

# Show the distribution of bounding box areas
plt.figure(figsize=(10, 6))
sns.histplot(small_areas, kde=True, color='blue')
plt.xlabel('Bounding Box Area')
plt.ylabel('Count')
plt.title('Distribution of Bounding Box Areas (After Moving Large BBoxes)')
plt.show()
