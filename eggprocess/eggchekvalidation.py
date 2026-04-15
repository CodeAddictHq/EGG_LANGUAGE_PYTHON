from .eggcmdgen import gencmd
SYNTEX = [
  "EGG SHOW",
  "EGG SHOW VAR",
  "EGG VAR",
  "EGG TYPE",
  "EGG FOR",
]



def chekvalidation(code):
  if code.startswith(SYNTEX[0]) or code.startswith(SYNTEX[1]) or code.startswith(SYNTEX[2]) or code.startswith(SYNTEX[3])  or code.startswith(SYNTEX[4]):
#    print("working", code)
    gencmd(code)
  else:
    print(f"invalid code : syntexal error '{code}'")