from PIL import Image
import os


def crop_left(image_path, image_number):
    # Open an image file
    image = Image.open(image_path)

    # Get the current dimensions of the image
    width, height = image.size

    # Define the target dimensions
    target_height = 2247
    target_width = 4032

    # Calculate the cropping box
    left = 0
    upper = 0
    right = width
    lower = min(height, target_height)

    # Crop the image
    cropped_image = image.crop((left, upper, right, lower))

    # Save the cropped image
    cropped_image.save(f"images/cropped_images/image_{image_number}.jpg")


# Loop through files in the images directory
image_number = 0
for file in os.listdir("images/original_images"):
    if file.endswith(".jpg"):
        crop_left(os.path.join("images/original_images", file), image_number)
        image_number += 1
