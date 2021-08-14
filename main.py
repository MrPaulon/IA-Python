##### SETTINGS #####
settings = {"language": "FR-fr"}

##### APPS #####
import qrcode
##### CODE #####
question = input("Que puis-je faire pour vous ?")

def main(lang):
  questionsplit = question.split()
  if lang == "FR-fr":
    if questionsplit[0] == "ping":
      url = questionsplit[1]
      status_website = urllib.request.urlopen(url).getcode()
      website_is_up = status_website == 200
      print(website_is_up)
      question = input("Que puis-je faire pour vous ?")
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
        qrcode_img.save('qrcode.png')
      if qrcode_custom == "custom":
        
      
if '__name__' == '__main__':
    main(settings["language"])
