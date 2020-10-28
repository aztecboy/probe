
import socket
import urllib.request
def probe():
  print("pls typ the url you want to 
    probe")
  print("ex: www.google.com")
  url1 = input("~:")
  url2 = "https://" + url1
  print(f"{url2} has compiled")
  print("running scans")
  ip = socket.gethostbyname(url1)
  print(ip)
  print(f"{ip} is {url1} ip address")
  open = urllib.request.urlopen(url2)
  red = open.read()
  code = open.code
  print(f" access code is {code}")
  print("do you want to see the html?")
  option = input("/:")
  if option == "yes":
    print(red.decode("utf-8"))
    print("closing")
  else:
    print("ok")
  
  
probe()

