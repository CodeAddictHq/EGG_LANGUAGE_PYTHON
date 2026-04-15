from . import eggidentifytask
SYNTEX = [
  "EGG SHOW ",
  "EGG SHOW VAR ",
  "EGG VAR ",
  "EGG TYPE ",
  "EGG FOR ",
]
def gencmd(code):
  codes = code.split(" ")
  if codes[1] == "SHOW" and codes[2]=="VAR":
    eggidentifytask.genshowvar(codes)
  elif codes[1] == "SHOW" and codes[2] != "VAR":
    eggidentifytask.genshow(codes)
  elif codes[2] == "VAR":
   eggidentifytask.genshowvar(codes) 
  elif codes[1] == "VAR" :
    li = code.split(" ")
  #  if li != 6:
  #    print("error")
  #  else:
    varcodes = code.split(" ", 6)
    eggidentifytask.genvar(varcodes)
  elif codes[1] == "TYPE":
    eggidentifytask.gentype(codes)
  elif codes[1] == "FOR":
    eggidentifytask.genfor(codes)
  else:
    print("invalid cmd : can't understand what to do")
  
  
  
  
  