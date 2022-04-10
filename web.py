#coding: utf-8
import time

print("Content-type: text/html; charset=utf-8\n")

html = """
<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <title>IA Python</title>  
    <link rel="stylesheet" href="src/assets/css/normalize.css">
    <link rel='stylesheet prefetch' href='https://fonts.googleapis.com/css?family=Open+Sans'>
    <link rel='stylesheet prefetch' href='https://cdnjs.cloudflare.com/ajax/libs/malihu-custom-scrollbar-plugin/3.1.3/jquery.mCustomScrollbar.min.css'>
    <script type="text/javascript"
        src="https://cdn.jsdelivr.net/npm/brython@3.10.5/brython.min.js">
    </script>
    <script type="text/javascript"
        src="https://cdn.jsdelivr.net/npm/brython@3.10.5/brython_stdlib.js">
    </script>
    <link rel="stylesheet" href="src/assets/css/style.css">
  </head>
  <body>
    <div class="chat">
      <div class="chat-title">
        <h1>John</h1>
        <h2>Bot en ligne</h2>
        <figure class="avatar">
          <img src="https://cdn.discordapp.com/attachments/641713008414031912/962808864846262302/Nouveau_projet.png" />
        </figure>
      </div>
      <div class="messages">
        <div class="messages-content"></div>
      </div>
      <div class="message-box">
        <textarea type="text" class="message-input" placeholder="Ecrire un message..."></textarea>
        <button type="submit" class="message-submit">Envoyer</button>
      </div>
    </div>
    <div class="bg"></div>
    <script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>
    <script src='https://cdnjs.cloudflare.com/ajax/libs/malihu-custom-scrollbar-plugin/3.1.3/jquery.mCustomScrollbar.concat.min.js'></script>
    <script src="src/assets/js/index.js"></script>
  </body>
</html>"""
print(html)