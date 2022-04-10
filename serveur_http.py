#coding: utf-8
import http.server
import socketserver

port = 80
adress = ("", port)

handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(adress, handler)

print(f"Serveur démarré avec succès sur le PORT {port}")
httpd.serve_forever()