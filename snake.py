import os
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
65 97 89.34`str1337`10e4`ski`V
                    "$`A`:899<
'''[1:-1]
s="\n".join(y+' ' for y in s.split("\n"))
frac=False
EOF='E'
box=[[EOF]+[*l]+[EOF]for l in s.split("\n")]
wall=[[EOF]*len(s.split("\n")[0])]
box=wall+box+wall
box=[[box[e][i]for e in range(len(box))]for i in range(len(box[0]))]
#for line in box:print(*line,sep=" ")
direction='right'
string=False
execute=True
List=False
number=False
cat=True
stack=[0]
X=1
Y=1
token=box[X][Y]
def snipe(dir,x,y,b):
  if dir=='right':return b[x+1][y]
  if dir=='left':return b[x-1][y]
  if dir=='down':return b[x][y+1]
  if dir=='up':return b[x][y-1]

while token!=EOF:
  token=box[X][Y]
  if token=='`':
    string=not(string)
    if string and not stack[-1] is str:
      stack.append('')
  if string and token!='`':
    stack[-1]+=token
  if not string and token in '0123456789.e':
    if cat:
      stack[-1]=str(stack[-1])+token
      if not snipe(direction,X,Y,box) in '0123456789.e':
        cat=False
        if not frac:
          if not '.' in stack[-1] and not 'e' in stack[-1]:
            stack[-1]=int(stack[-1])
          else:
            stack[-1]=float(stack[-1])
        else:
          stack[-1]=Fraction(stack[-1])
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
  if not string and token=='"':
    stack.append([stack.pop(-2),stack.pop(-1)])
  if direction=='right':X=X+1
  if direction=='left':X=X-1
  if direction=='down':Y=Y+1
  if direction=='up':Y=Y-1


print(stack)
