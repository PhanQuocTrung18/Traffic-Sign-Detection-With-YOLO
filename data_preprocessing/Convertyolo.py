import json
import os
import shutil

input_path = r"C:\Users\LAPTOP\Traffic_Sign_Detection\via-trafficsign-coco-20210321" # Đường dẫn đến thư mục chứa file JSON và ảnh
output_path = r"C:\Users\LAPTOP\Traffic_Sign_Detection\val" # Đường dẫn đến thư mục chứa ảnh và nhãn đã chuyển đổi

with open(os.path.join(input_path, 'annotations', 'val.json')) as f:
    data = json.load(f)

os.makedirs(os.path.join(output_path, 'images'), exist_ok=True)
os.makedirs(os.path.join(output_path, 'labels'), exist_ok=True)

def load_images_from_folder(folder):
    for filename in os.listdir(folder):
        source = os.path.join(folder, filename)
        destination = os.path.join(output_path, 'images', filename)

        try:
            shutil.copy(source, destination)
            print("File copied successfully.")
        except shutil.SameFileError:
            print("Source and destination represent the same file.")

load_images_from_folder(os.path.join(input_path, 'val'))

def get_img_ann(image_id):
    img_ann = []
    for ann in data['annotations']:
        if ann['image_id'] == image_id:
            img_ann.append(ann)
    return img_ann if img_ann else None

def get_img(filename):
    for img in data['images']:
        if img['file_name'] == filename:
            return img

for filename in os.listdir(os.path.join(input_path, 'val')):
    img = get_img(filename)
    if img is None:
        continue
    
    img_id = img['id']
    img_w = img['width']
    img_h = img['height']

    img_ann = get_img_ann(img_id)

    if img_ann:
        with open(os.path.join(output_path, 'labels', f'{os.path.splitext(filename)[0]}.txt'), "w") as file_object:
            for ann in img_ann:
                current_category = ann['category_id'] - 1  # Vì nhãn định dạng YOLO bắt đầu từ 0
                current_bbox = ann['bbox']
                x = current_bbox[0]
                y = current_bbox[1]
                w = current_bbox[2]
                h = current_bbox[3]

                x_centre = (x + (x + w)) / 2
                y_centre = (y + (y + h)) / 2

                x_centre = x_centre / img_w
                y_centre = y_centre / img_h
                w = w / img_w
                h = h / img_h

                x_centre = format(x_centre, '.6f')
                y_centre = format(y_centre, '.6f')
                w = format(w, '.6f')
                h = format(h, '.6f')

                file_object.write(f"{current_category} {x_centre} {y_centre} {w} {h}\n")

print("Conversion completed.")
