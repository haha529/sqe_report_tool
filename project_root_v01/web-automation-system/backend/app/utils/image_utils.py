import os
from shutil import copyfile

from PIL import Image

def resize_image(image_path, width=0, height=0):
    resized_image_path = f"{image_path[:-4]}_resized{image_path[-4:]}"
    img = Image.open(image_path)
    if width == 0 and height == 0:
        width, height = img.size
    elif width == 0:
        width = int(height * img.width / img.height)
    elif height == 0:
        height = int(width * img.height / img.width)

    img = img.resize((width, height), Image.Resampling.LANCZOS)
    img.save(resized_image_path)
    return resized_image_path