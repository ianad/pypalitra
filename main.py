import os
from os import path, listdir

from PIL import Image
import pytesseract
from pytesseract import image_to_string

def main():
    """
    Testing image_to_string
    """
    img_paths = [path.join('sourceimg',img) for img in listdir(path.join('sourceimg'))]
    for img in img_paths:
        print(img)
        print(image_to_string(Image.open(img).encode('utf-8')))


if __name__ == "__main__":
    main()