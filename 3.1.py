import math
x=int(input('Введите координату x'))
y=int(input('Введите координату y'))
z=int(input('Введите координату z'))
u=min((x+y+z)/x,(x+2*y-z)/y)+max(x,y,z) 
print('u=',u)
