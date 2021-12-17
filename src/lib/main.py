import math as m
import time

a=range(10)
b=[el*2 for el in a]
print(b)


I=[1,2]
I2=['a','b']
I3=[4,5]
f=[]
for e1 in I:
  for e2 in I2:
    for e3 in I3:
      f.append(e1,e2,e3)

I=list(range(1000000000))
v=list(range(1000000))
T1=time.clock()
s=I+v
print(T1)
T2=time.clock()
print('+ execution time: :',T2-T1,'s')


stack=[1,2,3,4]
print(stack)
for i in range(5,7):
  stack.append(i)

print(stack)

i=0
while(i<100):
  if(i>50):
    break
  else:
    print(i)
  i=i+1


a={1:'a',2:'b'}
for el in a.keys():
  print(el)

