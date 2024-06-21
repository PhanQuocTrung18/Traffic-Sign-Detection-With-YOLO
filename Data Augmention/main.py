import os
import random
import numpy as np
import pandas as pd
from PIL import Image
from tqdm import tqdm
from RandomRain import RandomRain
from RandomFlare import RandomFlare
from RandomSnow import RandomSnow
from RandomFog import RandomFog
from RandomBlur import RandomBlur
from RandomBrightness import RandomBrightness
from Noise import GaussianNoise
from RandomShadow import RandomShadow
import getpass

def load_data(image_dir, label_dir, csv_path):
    data = pd.read_csv(csv_path)
    image_paths = [os.path.join(image_dir, img) for img in data['image_name']]
    label_paths = [os.path.join(label_dir, img.replace('.jpg', '.txt')) for img in data['image_name']]
    classes = data['class'].tolist()
    return image_paths, label_paths, classes

# Function to save augmented image and label
def save_data(output_image_dir, output_label_dir, image_name, augmented_image, label_content):
    os.makedirs(output_image_dir, exist_ok=True)
    os.makedirs(output_label_dir, exist_ok=True)
    output_image_path = os.path.join(output_image_dir, image_name)
    augmented_image.save(output_image_path)
    label_name = image_name.replace('.jpg', '.txt')
    output_label_path = os.path.join(output_label_dir, label_name)
    with open(output_label_path, 'w') as f:
        f.write(label_content)

# Function to augment images and save
def augment_and_save(image_paths, label_paths, classes, output_image_dir, output_label_dir, num_images_to_augment, augmentations_per_image, augmentation_methods, class_labels):
    available_augmenters = {
        'rain': RandomRain(),
        'flare': RandomFlare(),
        'snow': RandomSnow(),
        'fog': RandomFog(),
        'blur': RandomBlur(),
        'brightness': RandomBrightness(),
        'noise': GaussianNoise(),
        'shadow': RandomShadow()
    }

    selected_augmenters = {name: available_augmenters[name] for name in augmentation_methods}

    # Filter images and labels by selected classes
    filtered_data = [(image_paths[i], label_paths[i], classes[i]) for i in range(len(image_paths)) if classes[i] in class_labels]

    # Limit the number of images to augment
    filtered_data = filtered_data[:num_images_to_augment]

    existing_images = set(os.listdir(output_image_dir))
    existing_labels = set(os.listdir(output_label_dir))

    for image_path, label_path, class_id in tqdm(filtered_data, desc='Augmenting images'):
        image = Image.open(image_path)
        with open(label_path, 'r') as f:
            label_content = f.read()

        for _ in range(augmentations_per_image):
            # Randomly choose an augmentation technique
            augmentation_method_name = random.choice(list(selected_augmenters.keys()))
            augmentation_method = selected_augmenters[augmentation_method_name]
            # Apply augmentation
            augmented_image = augmentation_method(image)
            # Generate unique filename for augmented image
            original_filename = os.path.splitext(os.path.basename(image_path))[0]
            image_name = f'{augmentation_method_name}_{original_filename}.jpg'

            # Ensure no duplicate images in output directory
            if image_name not in existing_images:
                save_data(output_image_dir, output_label_dir, image_name, augmented_image, label_content)
                existing_images.add(image_name)

def main():
    image_dir = r"C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Data Converted(-80%)\train\images"
    label_dir = r"C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Data Converted(-80%)\train\labels"
    output_image_dir = r"C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Result data\train\images"
    output_label_dir = r"C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Result data\train\labels"
    csv_path = r"C:\Users\LAPTOP\Desktop\Traffic Sign Detection With Yolo\Result data\data.csv"  
    image_paths, label_paths, classes = load_data(image_dir, label_dir, csv_path)

    # User input for number of images to augment
    while True:
        try:
            num_images_to_augment = int(getpass.getpass("Enter the number of images to augment: ").strip())
            if num_images_to_augment <= 0:
                print("Number of images to augment must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    # User input for number of augmentations per image
    while True:
        try:
            augmentations_per_image = int(getpass.getpass("Enter the number of augmentations per image: ").strip())
            if augmentations_per_image <= 0:
                print("Number of augmentations per image must be a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    augmentation_methods = getpass.getpass("Enter the augmentation methods (comma separated, available: rain, flare, snow, fog, blur, brightness, noise, shadow): ").strip().split(',')
    augmentation_methods = [method.strip() for method in augmentation_methods]

    # User input for class labels to augment
    class_labels_input = getpass.getpass("Enter the class labels to augment (comma separated): ").strip().split(',')
    class_labels = [int(label.strip()) for label in class_labels_input]

    augment_and_save(image_paths, label_paths, classes, output_image_dir, output_label_dir, num_images_to_augment, augmentations_per_image, augmentation_methods, class_labels)

if __name__ == "__main__":
    main()
