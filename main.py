import tkinter as tk
from tkinter import filedialog
from ocr import give
from voice_fa import voice


def get_image():
    file_path = filedialog.askopenfilename()
    return file_path


root = tk.Tk()
root.withdraw()

image = get_image()

root.destroy()

if __name__ == "__main__":
    matn = give(image)
    voice(matn)

