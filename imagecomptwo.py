import subprocess
import PIL
from PIL import Image
import tkinter.filedialog
#from tkinter.filedialog import*




def register_extension(id, extension):
    Image.EXTENSION[extension.lower()] = id.upper()
Image.register_extension = register_extension
def register_extensions(id, extensions):
    for extension in extensions:
        register_extension(id, extension)
Image.register_extensions = register_extensions



#file_path = askopenfilename()
file_path = tkinter.filedialog.askopenfilename()
img =PIL.Image.open(file_path)

myHeight,myWidth = img.size
size= (myHeight,myWidth)
newsize = (300, 300)
#img = img.resize(size, Image.ANTIALAS)
img = img.resize(newsize)
#save_path = asksaveasfilename()
save_path = tkinter.filedialog.asksaveasfilename()

img.save(save_path+"_compressed.jpg")
#img.save(save_path+"_compressed.png")
print("Operasyon pou diminye tay image ou a fèt ak Siksè ")

