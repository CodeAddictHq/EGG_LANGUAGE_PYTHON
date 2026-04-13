VARS = {
  "age":16
}


def showcontent(a):
  
  if a.startswith("'"):
    b = a.split("'")
    print(b[1])
  elif a.startswith('"'):
    b = a.split('"')
    print(b[1])
 
def showvar(a):
  keys = VARS.keys()
  for key in keys:
    if str(a) == key:
      print(VARS[str(a)])
    else:
      print(f"No variable named {str(a)}")


def storevar(vname, vvalue, vtype):
  if vtype == "STR":
    VARS[str(vname)] = str(vvalue)
  elif vtype == "NUMBER":
    VARS[str(vname)] = float(vvalue)
  elif vtype == "BOOL":
    VARS[str(vname)] = bool(vvalue)
  
    
    
    
  
  