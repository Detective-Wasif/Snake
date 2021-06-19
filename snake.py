import os
import sys
import math
import random
import requests
import turtle
from fractions import*

#s='''
#1>:CR:R"`. `jV
# ^_xβ=552:›_~<
#'''[1:-1]   

s='''
  1 01 65 97 89.34`str1337`10e4`ski`V
Si`31`W30◊30 72uw~1β=1 1X_∴X$`A`:899<
'''[1:-1]

s="\n".join(y+' ' for y in s.split("\n"))
frac=False
EOF='E'
box=[[EOF]+[*l]+[EOF]for l in s.split("\n")]
wall=[[EOF]*len(s.split("\n")[0])]
box=wall+box+wall
box=[[box[e][i]for e in range(len(box))]for i in range(len(box[0]))]
box.append(box[0])
for line in box:print(*line,sep=" ")
direction='right'
string=False
execute=True
List=False
number=False
cat=True
register=0
skip=0
stack=['0']
variables=dict()
X=1
Y=1
token=box[X][Y]
def snipe(dir,x,y,b):
  if dir=='right':return b[x+1][y]
  if dir=='left':return b[x-1][y]
  if dir=='down':return b[x][y+1]
  if dir=='up':return b[x][y-1]
class fraction(Fraction):
  pass
  def __repr__(self):
    return str(self.numerator)+'/'+str(self.denominator)
while token!=EOF:
  token=box[X][Y]
  if skip in [1,2]:
    skip+=1
  if skip==3:
    skip=0
    execute=True
  if execute:
    if token=='`':
      string=not(string)
      if string and not stack[-1] is str:
        stack.append('')
    if string and token!='`':
      stack[-1]+=token
    if (not string) and (token in '0123456789.e'):
      if cat:
        stack[-1]=stack[-1]+token
        if not snipe(direction,X,Y,box) in '0123456789.e':
          cat=False
          if not frac:
            if (not '.' in stack[-1]) and (not 'e' in stack[-1]):
              stack[-1]=int(stack[-1])
            else:
              stack[-1]=float(stack[-1])
          else:
            stack[-1]=fraction(stack[-1])
      else:
        stack.append(token)
        cat=True
    if not string and token=='x':
      break
    if not string and token in '<>V^':
      direction=['left','right','down','up']['<>V^'.index(token)]
    if not string and token==':':
      stack.append(stack[-1])
    if not string and token=='$':
      stack[-2],stack[-1]=stack[-1],stack[-2]
    if not string and token=='X':
      stack.append([stack.pop(-2),stack.pop(-1)])
    if not string and token=='_':
      del stack[-1]
    if not string and token=='∴':
      stack.extend([stack[-1]]*2)
    if not string and token=='R':
      stack.append(stack[-1][::-1])
    if not string and token=='A':
      stack[-2].append(stack.pop(-1))
    if not string and token=='r':
      stack=stack[::-1]
    if not string and token=='›':
      stack[-1]+=1
    if not string and token=='‹':
      stack[-1]-=1
    if not string and token in '+×÷%':
      exec('res=stack.pop(-2)'+token+'stack.pop(-1)')
      if frac:
        res=fraction(res)
      stack.append(res)
    if not string and token=='-':
      if [type(stack[-1]),type(stack[-2])]==[str,str]:
        stack.append(stack.pop(-2).replace(stack.pop(-1),''))
      else:
        res=stack.pop(-2)-stack.pop(-1)
        if frac:
          res=fraction(res)
        stack.append(res)
    if not string and token=='J':
      join=stack.pop(-1)
      op=stack.pop(-1)
      stack.append(join.join(op))
    if not string and token=='=':
      stack.append(stack.pop(-2)==stack.pop(-1))
    if not string and token=='≠':
      stack.append(stack.pop(-2)!=stack.pop(-1))
    if not string and token=='≤':
      stack.append(stack.pop(-2)<=stack.pop(-1))
    if not string and token=='{':
      stack.append(stack.pop(-2)<stack.pop(-1))
    if not string and token=='}':
      stack.append(stack.pop(-2)>stack.pop(-1)) 
    if not string and token=='≥':
      stack.append(stack.pop(-2)>=stack.pop(-1))
    if not string and token=='~':
      print(stack[-1])
    if not string and token=='p':
      print(stack[-1],end='')
    if not string and token=='P':
      print(stack[-2],end=stack.pop(-1))
    if not string and token=='!':
      raise Exception("Frick")
    if not string and token=='β':
      if stack[-1]:
        execute=True
      else:
        execute=False
      skip+=1
      if (type(stack[-1])==bool) and (stack[-1] in [True,False]):
        del stack[-1]
    if not string and token=='w':
      stack=[stack]
    if not string and token=='u':
      for x in stack.pop(-1):
        stack.append(x)
    if not string and token=='C':
      stack.append(chr(stack.pop(-1)))
    if not string and token=='O':
      stack.append(ord(stack.pop(-1)))
    if not string and token=='f':
      stack.append(open(stack.pop(-1)).read())
    if not string and token=='√':
      res=stack.pop(-1)**0.5
      if frac:
        res=fraction(res)
      stack.append(res)
    if not string and token=='◊':
      root=stack.pop(-1)
      op=stack.pop(-1)
      res=op**(1/root)
      if frac:
        res=fraction(res)
      stack.append(res)
    if not string and token=='m':
      coord=stack.pop(-1)
      X,Y=coord[0],coord[1]
    if not string and token=='*':
      exp=stack.pop(-1)
      base=stack.pop(-1)
      res=base**exp
      if frac:
        res=fraction(res)
      stack.append(res)
    if not string and token=='W':
      wrap=[]
      arity=stack.pop(-1)
      for _ in range(int(arity)):
        wrap.append(stack.pop(-1))
      stack.append(wrap[::-1])
    if not string and token=='i':
      stack.append(int(stack.pop(-1)))
    if not string and token=='s':
      stack.append(str(stack.pop(-1)))
    if not string and token=='S':
      stack.append([stack.pop(-1)])
  if direction=='right':X=X+1
  if direction=='left':X=X-1
  if direction=='down':Y=Y+1
  if direction=='up':Y=Y-1


print(stack)
