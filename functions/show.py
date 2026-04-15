import sys
import os
sys.path.append(os.path.abspath("../functions"))

sys.path.append(os.path.abspath("../DB"))
from DB.db import VARS


def showcontent(code):
  print(code)
  
def showvar(name):
  for var in VARS:
    if var == name:
      print(VARS[name])
      break
    else:
      print("var not found", name)
      break