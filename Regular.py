import re
def validate(phone_Number):
  if re.match(r"^[789]\d{9}$", phone_Number):
    return True
  else:
    return False
  
print(validate("1234567890"))
string = "Hello, I am 19 yers old"
s = re.sub(r"[0-9]+", "NUM" , string)
print(s)

txt = "The rain in Spain"
x = re.search(r"Spain", txt)
if(x):
  print("Match")
else:
  print("No Match")
