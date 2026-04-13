import eggfun


print("Welcome to egg interpreter, \n'eggs' to get the cmds \n'about' to know more about this language")
def eggs():
  print("visit \n")
  
def show(a):
  if a.startswith("'") and a.endswith("'") or a.startswith('"') and a.endswith('"'):
    eggfun.showcontent(a)
    
  
  else:
    eggfun.showvar(a)
  

while True:
  a = input("/>")
  if a == 'eggs':
    eggs()
  elif a == 'about':
    about()
  elif a.startswith("EGG SHOW "):
    b = a.split(" ", 2)[2]
    show(b)
  elif a == "exit":
    break
  elif a.startswith("EGG VAR"):
    print(a.split(" "))
    b = a.split(" ")
    name = b[3]
    value = b[5]
    if value.startswith("'"):
      value = value.replace("'", " ")
    elif value.startswith('"'):
      value = value.replace('"', " ")
    else:
      print(">>VAR SSIGN ERROR")
    value = value.strip()
    vartype = b[2]
    eggfun.storevar(name, value, vartype)
  
    

  

  