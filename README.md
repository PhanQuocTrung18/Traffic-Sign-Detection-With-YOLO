# Traffic Sign Detection and Classification

## 1. Description
This project is a system for detecting and classifying traffic signs. The detection phase uses Image Processing techniques to create bounding boxes on each video frame.

## 2. Development Strategy
- Convert data from COCO format to YOLO format
- Handle data issues
- Augment data to match the dataset appropriately
- Train the model with YOLO

## 3. Currently Supported Traffic Signs
![](https://i.imgur.com/jrmCOEW.png)

## 4. System Structure

### Main Files
- `RUNME.ipynb`: For performing data augmentation and balancing the data
- `data_augmentation`: Methods for data augmentation
- `data_processing`: Stages of image processing (convert, visualize bounding boxes, split data)

### Other Files
- `README.md`: This file, obviously 

### Dataset

**Download here**

### How to Use the Dataset:
**Traffic Sign Detection**
```
Traffic Sign Detection
│─── train
│    ├─── image
│    │    ├─── 000001.png
│    │    ├─── 000002.png
│    │    └─── ...
│    ├─── labels
│    │    ├─── 000001.txt
│    │    ├─── 000002.txt
│    │    └─── ...
│─── val
│    ├─── image
│    │    ├─── 000001.png
│    │    ├─── 000002.png
│    │    └─── ...
│    ├─── labels
│    │    ├─── 000001.txt
│    │    ├─── 000002.txt
│    │    └─── ...
```
**Data Processing**
- `Convertyolo.py`: Script to convert data to YOLO format
- `Convertcsv.py`: Script to convert data to CSV format
- `Splitdata(-80%)`: Script to split data at an 80% ratio (Handle with large bouding boxes)
 -`Splitdata(-100%)`: Script to split the entire dataset (Handle with large bouding boxes)
**Data Augmentation**
- `RUNME.ipynb`: Notebook for performing data augmentation