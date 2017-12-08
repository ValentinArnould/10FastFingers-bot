from org.sikuli.natives import Vision
Vision.setParameter("MinTargetSize", 8) # A small value such as 6 makes the matching algorithm be faster.
click("1512739134865.png")
#screenshot de selection du bloc note (ici sur linux)

type("a", KEY_CTRL)
type("c", KEY_CTRL)

yolo = Env.getClipboard()

stop = 0
mot = []
yoh = 0
hey = 0
hee = 0
how = 0
hou = 0
i = 0


for value in yolo:
    #popup("val " + yolo[i:(i+2)])
    if(value == str(yoh) or yolo[i:(i+2)] == str(yoh) or yolo[i:(i+3)] == str(yoh)):
        yolo = yolo.replace(str(yoh),"",1)
        hey = 0
        hee = hey + 1
        how = yolo.index("!",hey)
        mot.append(yolo[hey:how])
        yolo = yolo.replace(yolo[hey:(how+1)],"",1)
        yoh = yoh + 1
        i = -1
    i = i + 1

#for a,doom in enumerate(mot):
    #paste(doom)
    #type(" " + Key.BACKSPACE)
    
click("1512742055724.png")
#screenshot de selection du site 10fastfingers
sleep(2)
click("1512742150464.png")
#screenshot de selection de la barre du test

for a,doom in enumerate(mot):
    paste(doom)
    type(" " + Key.BACKSPACE)
    #sleep(0.1)