import socket
import urllib.request

#узнать локальный ip
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])

#узнать внешний ip
external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
print(external_ip)