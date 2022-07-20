import os
import imghdr
import subprocess
import PIL
import tkinter.filedialog
from PIL import Image


class downiszepress:

    def __init__(self):
        self.myWidth = 0
        self.myHeight = 0
        self.myWidthtreedown = 0
        self.myHeighttreedown = 0
        self.myWidthsixdown = 0
        self.myHeightsixdown = 0
        self.myWidthninedown = 0
        self.myHeightninedown = 0
        self.img = ''
        self.file_path = ''
        self.save_path = ''
        self.newsizetree=''
        self.newsizesix = ''
        self.newsizenine = ''

    def anrejistreExtension(self, id, extension):
        Image.EXTENSION[extension.lower()] = id.upper()

    Image.anrejistreExtension = anrejistreExtension

    def anrejistreExtensions(self, id, extensions):
        for extension in extensions:
            l.anrejistreExtension(id, extension)

    Image.anrejistreExtensions = anrejistreExtensions

    def tay(self):
        self.file_path = tkinter.filedialog.askopenfilename()
        self.img = PIL.Image.open(self.file_path)
        self.myHeight, self.myWidth = self.img.size
        print("Tay fichyew la se", self.myHeight, self.myWidth)

        return self.myHeight, self.myWidth

    def redwiTay(self):
        tay = ""
        print("Tay fichye w lan se :" + tay)
        ##############################################
        l.tay()
        self.myHeighttreedown = round(self.myHeight / 3)
        self.myWidthtreedown = round(self.myWidth / 3)
        self.myHeightsixdown = round(self.myHeight / 6)
        self.myWidthsixdown = round(self.myWidth / 6)
        self.myHeightninedowndown = round(self.myHeight / 9)
        self.myWidthninedowndown = round(self.myWidth / 9)

        print("\n****** KEK OPSYON POUW REDWI TAY LA: ******")
        print("A --> ", self.myHeighttreedown, " ", self.myWidthtreedown)
        print("B -->", self.myHeightsixdown, " ", self.myWidthsixdown)
        print("C -->", self.myHeightninedown, " ", self.myWidthninedowndown)
        self.newsizetree=(self.myHeighttreedown, self.myWidthtreedown)
        self.newsizesix=(self.myHeightsixdown,self.myWidthsixdown)
        self.newsizenine=((self.myHeightninedown,self.myWidthninedowndown))
        print("N --> lot opsyon")
        print("\n========================")
        opsyon = input("Antre --> X pouw retounen na meni prensipal la.\n Antre sa w chwazi a: ")
        opsyon = opsyon.upper()
        try:
            if (opsyon == "A"):
                print("\nSuccès")
                self.img = self.img.resize(self.newsizetree)
                self.save_path = tkinter.filedialog.asksaveasfilename()

                self.img.save(self.save_path+ "_nouvo.jpg")
            if (opsyon == "B"):
                print("\nSuccès")
                self.img = self.img.resize(self.newsizesix)
                self.save_path = tkinter.filedialog.asksaveasfilename()

                self.img.save(self.save_path+ "_nouvo.jpg")
            if (opsyon == "B"):
                print("\nSuccès")
                self.img = self.img.resize(self.newsizenine)
                self.save_path = tkinter.filedialog.asksaveasfilename()

                self.img.save(self.save_path+ "_nouvo.jpg")
            if (opsyon == "N"):
                print("\n==========================================")
                lotopsyon = input("Antre konbyen fwa pi piti ou vle redwi fichye a: ")
            if (lotopsyon == "X"):
                l.menu1()
        except (UnboundLocalError,ValueError):
            pass

    def menuImaj(self):

        print("\nKonprese imaj la(diminye nan tay li) --> K")
        print("Redwi nan rezolisyon imaj la         --> R")
        print("Konprese epi chanje rezolisyon imaj  --> C")
        print("\n=================================================")
        print("                                                  ")
        chwa2 = input("Antre --> X pouw retounen na meni prensipal la.\n Antre sa w chwazi a: ")
        chwa2 = chwa2.upper()

        if (chwa2 == "K"):
            print("\nKonprese imaj a")
            l.redwiTay()
        if (chwa2 == "R"):
            print("\nRedwi nan rezolisyon imaj a ")
        if (chwa2 == "C"):
            print("\nKonprese epi chanje imaj video ")

        if chwa2 == "X":
            l.menu1()

    def menuVideo(self):
        print("\nKonprese video a(diminye nan tay li) --> K")
        print("\Redwi nan rezolisyon video a           --> R")
        print("Konprese epi chanje rezolisyon video   --> C")
        print("\n=================================================")
        print("                                                  ")
        chwa3 = input("Antre --> X pouw retounen na meni prensipal la.\n Antre sa w chwazi a: ")
        chwa3 = chwa3.upper()

        if (chwa3 == "K"):
            print("\nKonprese video a")
        if (chwa3 == "R"):
            print("\nRedwi nan rezolisyon video a ")
        if (chwa3 == "C"):
            print("\nKonprese epi chanje rezolisyon video ")

        if chwa3 == "X":
            l.menu1()

    def menu1(self):
        print(
            "\n                           __________________________________________________________________________________________")
        print(
            "                           |                                                                                        |")
        print(
            "                           |                                    * I_COMPRESS *                                      |  ")
        print(
            "                           |                                                                                        |")
        print(
            "                           |                               ******* HELLO *******                                    |")
        print(
            "                           |                     Bienvini nan aplikasyon ki ap pemet ou                             |")
        print(
            "                           |                                  KONPRESE FICHYE                                       |")
        print(
            "                           |                                                                                        |")
        print(
            "                           |            Tip fichye wap gen chans pou w konprese yo se--> Image, Video, Audio        |")
        print(
            "                           |                                                                                        |")
        print(
            "                           |________________________________________________________________________________________|")

        print("\nMen sa pou w antre pouw komanse redwi fifye w yo:")
        print("          IMAGE --> I\n"
              "          VIDEO --> V\n"
              "          AUDIO --> A")
        print("===================================")
        chwa1 = input("\n Pouw kite pwogram lan antre :--> K \nAntre tip fichye ou vle konprese a: ")
        chwa1 = chwa1.upper()

        if (chwa1 == "K"):
            print(" AU REVOIR!!!")

        if (chwa1 == "I"):
            l.menuImaj()
        if (chwa1 == "V"):
            l.menuVideo()


l = downiszepress()
l.menu1()
