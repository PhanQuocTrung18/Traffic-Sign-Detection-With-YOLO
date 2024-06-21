import os
import csv
from PIL import Image

image_dir = r"C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Result data\train\images"
label_dir = r"C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Result data\train\labels"

csv_path = r'C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Result data\data.csv'

def readlabel(label_path):
    with open(label_path, 'r') as file:
        lines = file.readlines()
        bboxes = []
        for line in lines:
            parts = line.strip().split()
            bbox = {
                'class': int(float(parts[0])),
                'x': float(parts[1]),
                'y': float(parts[2]),
                'w': float(parts[3]),
                'h': float(parts[4]),
            }
            bboxes.append(bbox)
        return bboxes

def createcsv(image_dir, label_dir, output_csv_path):
    with open(output_csv_path, 'w', newline='') as csvfile:
        fieldnames = ['image_name', 'class', 'bbox', 'centroid', 'bb_area']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        
        for image_name in os.listdir(image_dir):
            image_path = os.path.join(image_dir, image_name)
            label_path = os.path.join(label_dir, os.path.splitext(image_name)[0] + '.txt')
            
            if os.path.exists(label_path):
                try:
                    image = Image.open(image_path)
                    width, height = image.size
                except Exception as e:
                    print(f"Failed to read image: {image_path}. Error: {e}")
                    continue
                
                bboxes = readlabel(label_path)
                if not bboxes:
                    print(f"No bounding boxes found in label file: {label_path}")
                    continue

                for bbox in bboxes:
                    x, y, w, h = bbox['x'], bbox['y'], bbox['w'], bbox['h']
                    centroid = (x + w / 2, y + h / 2)
                    bb_area = w * h
                    
                    writer.writerow({
                        'image_name': image_name,
                        'class': bbox['class'],
                        'bbox': f"({x}, {y}, {w}, {h})",
                        'centroid': f"({centroid[0]}, {centroid[1]})",
                        'bb_area': bb_area
                    })
            else:
                print(f"Label file not found for image: {image_name}")

createcsv(image_dir, label_dir, csv_path)

