import os
import random
from PIL import Image, ImageDraw, ImageFont
from IPython.display import display, clear_output

def read_yolo_bbox(yolo_annotation_file):
    with open(yolo_annotation_file, 'r') as f:
        bboxes = []
        for line in f:
            class_id, x, y, w, h = map(float, line.strip().split())
            bboxes.append((class_id, x, y, w, h))
        return bboxes

def show_image_with_yolo_bboxes(image_path, yolo_annotation_file, class_names):
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()  # Load default font for displaying class names
    
    w, h = image.size
    bboxes = read_yolo_bbox(yolo_annotation_file)
    
    for bbox in bboxes:
        class_id, x, y, bw, bh = bbox
        x1 = int((x - bw / 2) * w)
        y1 = int((y - bh / 2) * h)
        x2 = int((x + bw / 2) * w)
        y2 = int((y + bh / 2) * h)
        
        draw.rectangle([x1, y1, x2, y2], outline="red", width=2)
        
        class_name = class_names[int(class_id)]
        text_size = draw.textbbox((x1, y1), class_name, font=font)  # Get text bounding box
        text_width = text_size[2] - text_size[0]
        text_height = text_size[3] - text_size[1]
        text_background = (x1, y1 - text_height, x1 + text_width, y1)
        
        draw.rectangle(text_background, fill="red")
        draw.text((x1, y1 - text_height), class_name, fill="white", font=font)
    
    clear_output(wait=True)  # Clear the previous output
    display(image)

# Thư mục chứa hình ảnh và file YOLO annotations
image_folder = r'C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\final_data2\train\images'
yolo_annotation_folder = r'C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\final_data2\train\labels'

# Danh sách các file hình ảnh
image_files = os.listdir(image_folder)

# Shuffle the list of image files
random.shuffle(image_files)

# Tạo dictionary mapping class IDs to class names
class_names = {
    0: "stop",
    1: "left",
    2: "right",
    3: "straight",
    4: "no_left",
    5: "no_right"
}

# Hiển thị ảnh đầu tiên
index = 0
while True:
    if index >= len(image_files):
        print("Đã hiển thị hết tất cả các ảnh.")
        break
    
    image_path = os.path.join(image_folder, image_files[index])
    yolo_annotation_file = os.path.join(yolo_annotation_folder, os.path.splitext(image_files[index])[0] + '.txt')
    
    if os.path.exists(yolo_annotation_file):
        show_image_with_yolo_bboxes(image_path, yolo_annotation_file, class_names)
    else:
        print(f"File YOLO annotation không tồn tại: {yolo_annotation_file}")
    
    input("Nhấn Enter để hiển thị ảnh tiếp theo...")
    index += 1
