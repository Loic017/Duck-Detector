import cv2
import pandas as pd
import numpy as np
import os
import stuff as stuff

# VARIABLES

IMAGE_FOLDER = stuff.IMAGES_FOLDER
IMAGE_FILE_TYPE = "jpg"
IMAGE_NUMBER = 20

box_type_input = input("Enter the type of box you want to select (1: ball, 2: line): ")

if box_type_input == "1":
    box_type = "ball"
    fromCenter = True
else:
    box_type = "line"
    fromCenter = False

CSV_FILE = stuff.BOUNDING_FOLDER + f"{box_type}_bounding_box.csv"

# FUNCTIONS


def get_image_files(IMAGE_FOLDER, IMAGE_FILE_TYPE):
    image_files = []
    for file in os.listdir(IMAGE_FOLDER):
        if file.endswith(IMAGE_FILE_TYPE):
            image_files.append(file)
    return image_files


def load_image_files(image_files, IMAGE_FOLDER):
    images = []
    for file in image_files:
        image = cv2.imread(IMAGE_FOLDER + "/" + file)
        images.append(image)
    return images


# MAIN

image_files = get_image_files(IMAGE_FOLDER, IMAGE_FILE_TYPE)
images = load_image_files(image_files, IMAGE_FOLDER)
np.array(images).shape

x, y, w, h = cv2.selectROI(
    "Select ROI", images[IMAGE_NUMBER], fromCenter=fromCenter, showCrosshair=True
)

existing_data = pd.read_csv(CSV_FILE)
existing_data = existing_data[existing_data["image_id"] != IMAGE_NUMBER]

data = {"image_id": [IMAGE_NUMBER], "x": [x], "y": [y], "width": [w], "height": [h]}
data = pd.DataFrame(data)

data = pd.concat([existing_data, data], ignore_index=True)
data.to_csv(CSV_FILE, index=False)
