from PIL import Image
import pytesseract


def give(ax):
    ax = Image.open(ax)
    matn = pytesseract.image_to_string(ax, lang='fas')
    print(matn)
    return matn
