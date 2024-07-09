import os
from PIL import Image, ImageDraw, ImageFont

images_folder = r"C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Result data\train\images"
labels_folder = r"C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Result data\train\labels"

category_names = {
    0: "stop",
    1: "left",
    2: "right",
    3: "straight",
    4: "no_left",
    5: "no_right"
}

label_files = [f for f in os.listdir(labels_folder) if f.endswith('.txt')]

for label_file in label_files:
    image_filename = f"{os.path.splitext(label_file)[0]}.jpg"
    image_path = os.path.join(images_folder, image_filename)

    try:
        image = Image.open(image_path)
    except IOError:
        print(f"Could not read image {image_filename}. Skipping...")
        continue

    print(f"Image File: {image_filename}\n")

    label_file_path = os.path.join(labels_folder, label_file)
    with open(label_file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            label_parts = line.strip().split()
            category_id = int(label_parts[0])
            x_center, y_center, w, h = map(float, label_parts[1:])

            image_width, image_height = image.size
            x = int((x_center - w / 2) * image_width)
            y = int((y_center - h / 2) * image_height)
            w = int(w * image_width)
            h = int(h * image_height)

            category_name = category_names.get(category_id, 'Unknown')

            draw = ImageDraw.Draw(image)
            draw.rectangle([x, y, x + w, y + h], outline=(255, 0, 0), width=2)
            draw.text((x, y - 12), f"{category_name}", fill=(255, 0, 0))
    
    image.show()
    input("Press Enter to continue...")
    image.close()

print("All images processed.")

