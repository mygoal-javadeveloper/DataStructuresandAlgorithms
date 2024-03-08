"""
A string of brackets is considered correctly matched if every opening bracket in the string can be paired up with a later closing bracket, and vice versa. For instance, “(())()” is correctly matched, whereas “)(“ and “((” aren’t. For instance, “((” could become correctly matched by adding two closing brackets at the end, so you’d return 2.

Given a string that consists of brackets, write a function bracketMatch that takes a bracket string as an input and returns the minimum number of brackets you’d need to add to the input in order to make it correctly matched.

Explain the correctness of your code, and analyze its time and space complexities.

"""



def bracket_match(text):
  text = text.strip()
  openbracketcount =  0
  closebracketcount = 0
  remaining = 0
  flag = False
  for x in text:
    if x == '(' and flag == False:
      openbracketcount += 1
    elif  x == '(' and flag == True:
      remaining = remaining + openbracketcount + closebracketcount
      closebracketcount = 0
      openbracketcount += 1
      flag = False
    elif x == ')':
      if openbracketcount > 0:
        openbracketcount -= 1
      elif openbracketcount == 0:
        closebracketcount += 1
      flag = True
  return remaining + openbracketcount + closebracketcount

print(bracket_match("(()"))
print(bracket_match(")"))
print(bracket_match("(())"))
print(bracket_match("())("))