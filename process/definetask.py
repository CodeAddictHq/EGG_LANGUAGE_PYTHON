
import sys
import os
sys.path.append(os.path.abspath("../functions"))

sys.path.append(os.path.abspath("../DB"))
from DB import db


from functions import show

def makestr(txt):
  a = txt[1:-1:]
  return a
  
def findvalue(txt):
  value = txt.split("=")
  return value[1].strip()
def findname(txt):
  value = txt.split("=")
  return value[0].strip()
  
def valueconvert(val, tp):
  if tp=="STR" and val.startswith("'") and val.endswith("'"):
    return makestr(val)
  elif tp == "BOOL":
    return bool(makestr(val))
  elif tp == "NUM":
    return float(val)
  elif tp == "NONE":
    val = None
    return val
  
  

def createshow(codes):
  code = codes.split(" ", 1)
  val = code[1]
  if val.startswith("'") and val.endswith("'"):
    show.showcontent(makestr(val))
  elif val.startswith('"') and val.endswith("'"):
    show.showcontent(makestr(val))
  else:
    show.showvar(val)
    
    
def createvar(codes):

  code = codes.split(" ", 2)
  vartype = code[1]
  name = findname(code[-1])
  value = findvalue(code[-1])
  value = valueconvert(value, vartype)
  db.assignvar(name, value)
  
  
  
  
  
    
def genvar(codes):
  vartype = codes[2]
  name = codes[3]
  value = codes[5].strip()
  eggsvars.identifyvar(name, value, vartype)
  

def genshowvar(codes):
  varname = codes[2]
  eggsvars.varshow(varname)

def gentype(codes):
  pass

def genfor(codes):
  pass

  
  