from PIL import Image
import pytesseract
from pytesseract import image_to_string

def main():
    """
    Testing image_to_string
    """
    print(image_to_string(Image.open('sourceimg/Dxcc7S0WwAEqfd5.jpg large.jpg')))


if __name__ == "__main__":
    main()