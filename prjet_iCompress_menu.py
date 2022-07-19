# metod pou meni yo
def redwiTay():
    tay=""
    print("Tay fichye w lan se :"+tay)
    print("\n****** KEK OPSYON POUW REDWI TAY LA: ******")
    print("A --> 3 fwa pi piti")
    print("B --> 6 fwa pi piti")
    print("C --> 9 fwa pi piti")
    print("N --> lot opsyon")
    print("\n========================")
    opsyon=input("Antre --> X pouw retounen na meni prensipal la.\n Antre sa w chwazi a: ")
    opsyon=opsyon.upper()

    if (opsyon=="A"):
        print("\n3 fwa pi piti")
    if (opsyon=="B"):
        print("\n6 fwa pi piti")
    if (opsyon=="B"):
        print("\n9 fwa pi piti")
    if (opsyon=="N"):
        print("\n==========================================")
        lotopsyon=input("Antre konbyen fwa pi piti ou vle redwi fichye a: ")
    if (lotopsyon=="X"):
        menu1()

def menuImaj():

    print("\nKonprese imaj la(diminye nan tay li) --> K")
    print("Redwi nan rezolisyon imaj la         --> R")
    print("Konprese epi chanje rezolisyon imaj  --> C")
    print("\n=================================================")
    print("                                                  ")
    chwa2=input("Antre --> X pouw retounen na meni prensipal la.\n Antre sa w chwazi a: ")
    chwa2 = chwa2.upper()

    if (chwa2=="K"):
        print("\nKonprese imaj a")
        redwiTay()
    if (chwa2=="R"):
        print("\nRedwi nan rezolisyon imaj a ")
    if (chwa2 == "C"):
        print("\nKonprese epi chanje imaj video ")

    if chwa2=="X":
        menu1()

def menuVideo():
    print("\nKonprese video a(diminye nan tay li) --> K")
    print("\Redwi nan rezolisyon video a           --> R")
    print("Konprese epi chanje rezolisyon video   --> C")
    print("\n=================================================")
    print("                                                  ")
    chwa3 = input("Antre --> X pouw retounen na meni prensipal la.\n Antre sa w chwazi a: ")
    chwa3 = chwa3.upper()

    if (chwa3=="K"):
        print("\nKonprese video a")
    if (chwa3=="R"):
        print("\nRedwi nan rezolisyon video a ")
    if (chwa3 == "C"):
        print("\nKonprese epi chanje rezolisyon video ")

    if chwa3 == "X":
        menu1()


def menu1():
    print("\n                           __________________________________________________________________________________________")
    print("                           |                                                                                        |")
    print("                           |                                    * I_COMPRESS *                                      |  ")
    print("                           |                                                                                        |")
    print("                           |                               ******* HELLO *******                                    |")
    print("                           |                     Bienvini nan aplikasyon ki ap pemet ou                             |")
    print("                           |                                  KONPRESE FICHYE                                       |")
    print("                           |                                                                                        |")
    print("                           |            Tip fichye wap gen chans pou w konprese yo se--> Image, Video, Audio        |")
    print("                           |                                                                                        |")
    print("                           |________________________________________________________________________________________|")

    print("\nMen sa pou w antre pouw komanse redwi fifye w yo:")
    print("          IMAGE --> I\n"
          "          VIDEO --> V\n"
          "          AUDIO --> A")
    print("===================================")
    chwa1=input("\n Pouw kite pwogram lan antre :--> K \nAntre tip fichye ou vle konprese a: ")
    chwa1=chwa1.upper()

    if(chwa1=="K"):
        print(" AU REVOIR!!!")

    if(chwa1=="I"):
        menuImaj()
    if(chwa1 == "V"):
        menuVideo()

print(menu1())




























