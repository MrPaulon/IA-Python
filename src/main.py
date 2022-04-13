import settings
from settings import *
import os
from os import *
import qrcode
from qrcode import *
##### CODE #####

print(settings["language"])

def main(lang):
    question = input(language[lang]['Hello what i can do ?']).lower()
    questionsplit = question.split()
    for i in range(len(questionsplit)):
        if questionsplit[i] == "ping":
          ping_website = questionsplit[i] + " " + questionsplit[i+1]
          os.system(ping_website)
          return
        if questionsplit[i] == language[lang]['create'] and questionsplit[i+1] == "qrcode":
          qrcode_custom = input(language[lang]['qrcode_creation'])
          if qrcode_custom == "simple":
            qrcode_website = input(language[lang]['qrcode_namewebsite'])
            qrcode_img = qrcode.make(qrcode_website)
            qrcode_img.save('qrcode.png')
          if qrcode_custom == "custom":
            qrcode_website = input("Quel est le site internet relié au qrcode ?")


main(settings["language"])
