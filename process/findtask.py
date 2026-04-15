from . import definetask
SYNTEX = [
  "SHOW ",
  "VAR STR ",
  "VAR NUM ",
  "VAR BOOL ",
  "TYPE ",
  "FOR ",
]
def find(code):
  if code.startswith(SYNTEX[0]):
    definetask.createshow(code)
  elif code.startswith(SYNTEX[1]) or code.startswith(SYNTEX[2]) or code.startswith(SYNTEX[3]):
    
    definetask.createvar(code)
  
  
  
  
  