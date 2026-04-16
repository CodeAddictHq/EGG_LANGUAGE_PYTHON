from process.validation import chekvalidation

print("Welcome to egg interpreter, \n'eggs' to get the cmds \n'about' to know more about this language")
  
  

while True:
  a = input("/>")
  if a == "EXIT":
    break
  else:
    chekvalidation(a)
  
  
  

  

  