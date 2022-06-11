
import pywhatkit as wh
from time import sleep
from datetime import datetime
import pyautogui as pt
import keyboard as k
import random

def frases():
    with open('../frases.txt','r') as f:
        frases = f.readlines()
        frases2 = []
        for i in frases:
            frases2.append(i.strip('\n'))
        frase = random.choice(frases2)
        return frase
def tiempo():
    with open('../tiempo.txt','r') as f:
        tiempo = f.readline()
        tiempo.strip('\n')
        return int(tiempo)
def numeros():
    with open('../numeros.txt','r') as f:
        numeros = f.readlines()
        
        numeros2 = []
        for i in numeros:
            numeros2.append(i.strip('\n'))
        return numeros2
def imagenes():
    with open('../imagenes.txt','r') as f:
        imagenes = f.readlines()
        imagenes2 = []
        for i in imagenes:
            i.strip('\n')
            imagenes2.append( "\\".join(__file__.split("\\")[0:-2]) + "\\" + i)
        imagen = random.choice(imagenes2)
        return imagen

def send(contatos,n,frase,imagen):
    while len(contatos)>=1:
        print(datetime.now().hour,datetime.now().minute+2)
        wh.sendwhatmsg(contatos[0],frase,datetime.now().hour,datetime.now().minute+2)
        sleep(10)
        posi = pt.locateOnScreen("\\".join(__file__.split('\\')[:-2]) + "\clip.png")
        sleep(1)
        pt.click(posi[0],posi[1])

        sleep(2)
        pt.click(posi[0],posi[1] - 40)
        sleep(4)
        k.write(imagen)
        sleep(3)
        k.press_and_release('enter')
        sleep(3)
        k.press_and_release('enter')
        sleep(5)
        k.press_and_release('ctrl + w')
        del contatos[0]
def main():
    send(contatos=numeros(),n=tiempo(),frase=frases(),imagen=imagenes())

main()
