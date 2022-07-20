import subprocess
import PIL
from PIL import Image
from tkinter.filedialog import *


def register_extension(id, extension):
    Image.EXTENSION[extension.lower()] = id.upper()


Image.register_extension = register_extension


def register_extensions(id, extensions):
    for extension in extensions:
        register_extension(id, extension)


Image.register_extensions = register_extensions

file_path = askopenfilename()
img = PIL.Image.open(file_path)
myHeight, myWidth = img.size

# img = img.resize((myHeight,myWidth), PIL.Image.ANTIALAS)
save_path = asksaveasfilename()

img.save(save_path + "_compressed.jpg")
