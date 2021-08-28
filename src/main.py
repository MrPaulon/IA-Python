import settings
from settings import *
import os
from os import *
import qrcode
from qrcode import *
##### CODE #####

lang = settings["language"]

if lang == 'FR-fr':
  question = input("Que puis-je faire pour vous ?")
  questionsplit = question.split()
  if questionsplit[0] == "ping":
    ping_website = questionsplit[0] + " " + questionsplit[1]
    os.system(ping_website)
  if questionsplit[0] == "Crée" and questionsplit[1] == "raccourci":
    name_shortcut = input("Quel nom voulez vous donnez à votre raccourci ?")
    website_shortcut = input("Quelle est l'adresse du site de votre raccourci ?")
    settings[name_shortcut] = website_shortcut 
    question = input("Que puis-je faire pour vous ?")
  if questionsplit[0] == "Crée" and questionsplit[1] == "qrcode":
    qrcode_custom = input("Souhaitez-vous que je crée un qrcode simple ? Ou préférez vous le personaliser ?")
    if qrcode_custom == "simple":
      qrcode_website = input("Quel est le site internet relié au qrcode ?")
      qrcode_img = qrcode.make(qrcode_website)
      qrcode_file = input("Quel nom voulez vous donnez à votre fichier ?")
      qrcode_img.save(qrcode_file + '.png')
    if qrcode_custom == "custom":
      qrcode_website = input("Quel est le site internet relié au qrcode ?")
  if questionsplit[0] == "Etat" and questionsplit[1] == "réseaux":
    os.system("ipconfig")

