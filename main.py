from pathlib import Path
from os import listdir

from PIL import Image
import pytesseract
from pytesseract import image_to_string

def main():
    """
    Testing image_to_string
    """
    source = Path(r'sourceimg').absolute()
    img_paths = [(source / img) for img in listdir(source)]
    for img in img_paths:
        print(img)
        print(image_to_string(Image.open(img)))


if __name__ == "__main__":
    main()