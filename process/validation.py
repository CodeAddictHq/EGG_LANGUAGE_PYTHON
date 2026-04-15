from . import findtask
SYNTEX = [
  "SHOW",
  "VAR",
  "TYPE",
  "FOR",
]



def chekvalidation(code):
  if code.startswith(SYNTEX[0]) or code.startswith(SYNTEX[1]) or code.startswith(SYNTEX[2]) or code.startswith(SYNTEX[3]):
#    print("working", code)
    findtask.find(code)
  else:
    print(f"invalid code : syntexal error '{code}'")