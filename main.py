##### SETTINGS #####
settings = {"language": "FR-fr"}

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
      nameshortcut = input("Quel nom voulez vous donnez à votre raccourci ?")
      websiteshortcut = input("Quelle est l'adresse du site de votre raccourci ?")
      settings[nameshortcut] = websiteshortcut 
      question = input("Que puis-je faire pour vous ?")
      
      
if '__name__' == '__main__':
    main(settings["language"])
