# # augmentations.py
# import os
# import random
# import shutil
# from PIL import Image
# import numpy as np
# import albumentations as A
# from tqdm import tqdm

# class RandomSnow:
#     def __init__(self, brightness_coeff=2.5):
#         self.brightness_coeff = brightness_coeff

#     def __call__(self, image):
#         snow_point_lower = random.uniform(0.2, 1)
#         snow_point_upper = random.uniform(snow_point_lower, 1)
#         img_np = np.array(image)
#         transform = A.Compose([
#             A.RandomSnow(brightness_coeff=self.brightness_coeff, snow_point_upper=snow_point_upper, 
#                          snow_point_lower=snow_point_lower, p=1),
#         ])
#         augmented = transform(image=img_np)
#         return Image.fromarray(augmented['image'])

# class RandomFog:
#     def __init__(self):
#         pass

#     def __call__(self, image):
#         fog_coef_lower = random.uniform(0.3, 0.5)
#         fog_coef_upper = random.uniform(0.5, 0.9)
#         alpha_coef = random.uniform(0.1, 0.5)
#         img_np = np.array(image)
#         transform = A.Compose([
#             A.RandomFog(p=1.0, fog_coef_lower=fog_coef_lower, fog_coef_upper=fog_coef_upper, alpha_coef=alpha_coef),
#         ])
#         augmented = transform(image=img_np)
#         return Image.fromarray(augmented['image'])

# class RandomFlare:
#     def __init__(self, flare_roi=(0, 0, 1, 0.5), src_color=(255, 255, 255)):
#         self.flare_roi = flare_roi
#         self.src_color = src_color

#     def __call__(self, image):
#         angle_upper = random.uniform(0, 1)
#         num_flare_circles_lower = random.randint(3, 8)
#         num_flare_circles_upper = random.randint(9, 15)
#         src_radius = random.randint(100, 200)
#         img_np = np.array(image)
#         transform = A.Compose([
#             A.RandomSunFlare(p=1.0, flare_roi=self.flare_roi, angle_lower=0, angle_upper=angle_upper, 
#                              num_flare_circles_lower=num_flare_circles_lower, num_flare_circles_upper=num_flare_circles_upper, 
#                              src_radius=src_radius, src_color=self.src_color),
#         ])
#         augmented = transform(image=img_np)
#         return Image.fromarray(augmented['image'])

# class RandomRain:
#     def __init__(self, drop_length=20, drop_width=1, drop_color=(200, 200, 200), blur_value=4, brightness_coefficient=0.9):
#         self.drop_length = drop_length
#         self.drop_width = drop_width
#         self.drop_color = drop_color
#         self.blur_value = blur_value
#         self.brightness_coefficient = brightness_coefficient

#     def __call__(self, image):
#         slant_lower = random.randint(-20, 0)
#         slant_upper = random.randint(0, 20)
#         rain_types = ['drizzle', 'heavy', 'torrential']
#         rain_type = random.choice(rain_types)
#         img_np = np.array(image)
#         transform = A.Compose([
#             A.RandomRain(p=1.0, slant_lower=slant_lower, slant_upper=slant_upper, drop_length=self.drop_length, 
#                          drop_width=self.drop_width, drop_color=self.drop_color, blur_value=self.blur_value, 
#                          brightness_coefficient=self.brightness_coefficient, rain_type=rain_type),
#         ])
#         augmented = transform(image=img_np)
#         return Image.fromarray(augmented['image'])

# def copy_label(image_path, output_label_dir):
#     label_name = os.path.splitext(os.path.basename(image_path))[0] + ".txt"
#     original_label_path = os.path.join(os.path.dirname(image_path), "../labels", label_name)
#     output_label_path = os.path.join(output_label_dir, label_name)
#     shutil.copyfile(original_label_path, output_label_path)

# def augment_images(augmenter, num_augment, image_dir, output_image_dir, label_dir, output_label_dir):
#     if not os.path.exists(output_image_dir):
#         os.makedirs(output_image_dir)
#     if not os.path.exists(output_label_dir):
#         os.makedirs(output_label_dir)

#     image_paths = [os.path.join(image_dir, fname) for fname in os.listdir(image_dir) if fname.endswith('.jpg')]
#     for i in tqdm(range(num_augment)):
#         image_path = random.choice(image_paths)
#         image = Image.open(image_path)
#         augmented_image = augmenter(image)
#         output_image_path = os.path.join(output_image_dir, f'augmented_{i}.jpg')
#         augmented_image.save(output_image_path)
#         copy_label(image_path, output_label_dir)
