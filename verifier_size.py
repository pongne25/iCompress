import PIL
from PIL import Image
import tkinter.filedialog

# afficher imaj la ak tay li
#chemin = "C:/Users/THINKPAD/Documents/"
chemin = tkinter.filedialog.askopenfilename()
#fichier = input("ki non fichye imaj ou a:")
fichier = chemin

im = Image.open(fichier)

L,H = im.size
im=im.resize()
print("laje imaj la se= ",L,"longe imaj la se= ",H)

im.show()



