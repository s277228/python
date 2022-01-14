
import sys


while(True):
  print('PLEASE INSERT AN INTEGER NUMBER IN THE RANGE 0-10')
  param1 = input()
  if int(param1) in range(11): 
    while(True):
      print( 'PLEASE INSERT A CHAR PARAMETER IN [A,B,C]')
      param2 = input()
      if param2 in ['A','B','C']:
        print('uso I due parametri passati dall utente: ',param1,param2)
        sys.exit()
      else: print('TRY AGAIN PLEASE')
  else: print('TRY AGAIN PLEASE')


infile='mydata.dat'
outfile='myout.dat'

def f(y):
  if y >= 0.0:
    return y**5*math.exp(-y)
  else:
    return 0.0

indata = open( infile, 'r')
linee=indata.readlines()
indata.close()
processati=[]
x=[]
for el in linee:
  valori = el.split()
  x.append(float(valori[0])); y = float(valori[1])
  processati.append(f(y))

outdata = open(outfile, 'w')
i=0
for el in processati:
  outdata.write('%g %12.5e\n' % (x[i],el))
  i+=1
outdata.close()




l = []
with open('input1.txt', 'r') as f:
  for line in f:
    line = line.strip()
    if len(line) > 0:
      l.append(list(map(int, line.split(','))))
print(l)

fin = open('input.txt','r')
a=[]
for line in fin.readlines():
  a.append( [ int (x) for x in line.split(',') ] )


a=3
b=[[3,6,9],[1,2,3],[2,4,8]]

def matrix_per_scalar(matrix, scalar):
  result=[]
  for i in range(len(matrix)):
    tmp=[]
    for j in range(len(matrix[i])):
      tmp.append(matrix[i][j]*scalar)
    result.append(tmp)
  return result

  def print_matrix(matrix):
    for i in range(len(matrix)):
      for j in range(len(matrix[i])):
        print(str((matrix[i][j]))+"\t", end='')
      print("\n")


print("Input:")
print("Scalar=" + str(a))
print("Matrix=")
print_matrix(b)

print("Matrix x scalar multiplication result:")
print_matrix(matrix_per_scalar(b,a))

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
print(p1.name)
print(p1.age)






    