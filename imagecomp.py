"""import subprocess
import tkinter.filedialog

import PIL
from PIL import Image
#from tkinter.filedialog import*
import tkinter.filedialog



def anrejistreExtension(id, extension):
    Image.EXTENSION[extension.lower()] = id.upper()
Image.anrejistreExtension = anrejistreExtension

def anrejistreExtensions(id, extensions):
    for extension in extensions:
        anrejistreExtension(id, extension)
Image.anrejistreExtensions = anrejistreExtensions



#file_path = askopenfilename()
file_path = tkinter.filedialog.askopenfilename()
img =PIL.Image.open(file_path)
myHeight,myWidth = img.size

print(myHeight,myWidth)
img=img.resize
img = img.resize((myHeight,myWidth), PIL.Image.ANTIALAS)
#save_path = tkinter.filedialog.asksaveasfilename()
#save_path = asksaveasfilename()

#img.save(save_path+"_compressed.jpg")
"""

from PIL import Image

# Opens a image in RGB mode
im = Image.open(r"C:\Users\Nicodem LAURORE\Desktop\jd_compressed.jpg")

# Size of the image in pixels (size of original image)
# (This is not mandatory)
width, height = im.size

# Setting the points for cropped image
left = 6
top = height / 4
right = 174
bottom = 3 * height / 4

# Cropped image of above dimension
# (It will not change original image)
im1 = im.crop((left, top, right, bottom))
newsize = (336, 163)
im1 = im1.resize(newsize)
# Shows the image in image viewer
name=""
#im1.save(f"C:/Users/Nicodem LAURORE/Desktop/")
im1.show()

