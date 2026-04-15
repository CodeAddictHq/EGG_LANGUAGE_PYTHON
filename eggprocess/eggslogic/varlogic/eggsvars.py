from . import varsave
from .eggdb import VARS


def makestr(name, value):
  value = value.split("'")[1]
  value = str(value)
  varsave.savestr(name, value)
  

def identifyvar(name, value, vtype):
  if vtype == "STR" and value.startswith("'") and value.endswith("'"):
    makestr(name, value)
  elif vtype == "STR" and (vtype[0] != "'" or vtype[-1] != "'"):
    print("invalid str ")
  

def varshow(name):
  if name in VARS:
    print(VARS[name])
  else:
    print("var not found")