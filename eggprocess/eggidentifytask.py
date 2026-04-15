from .eggslogic.funlogic import basicfun
from .eggslogic.varlogic.dictlogic import dicts
from .eggslogic.varlogic.listlogic import lists
from .eggslogic.varlogic import eggsvars
def genshow(codes):
  content = str(codes[2].split("'")[1])
  basicfun.showcontent(content)

def genvar(codes):
  vartype = codes[2]
  name = codes[3]
  value = codes[5].strip()
  eggsvars.identifyvar(name, value, vartype)
  

def genshowvar(codes):
  varname = codes[3]
  eggsvars.varshow(varname)

def gentype(codes):
  pass

def genfor(codes):
  pass

  
  