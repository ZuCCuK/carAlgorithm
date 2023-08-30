import random 
import string 

class carClass():
    def __init__(self,name):
     self.name = name
     self.indx = 0
    def ind(self):
       self.indx += 1

a = carClass("a")
b = carClass("b")
c = carClass("c")
d = carClass("d")
e = carClass("e")
f = carClass("f")
g = carClass("g")
h = carClass("h")
i = carClass("i")
j = carClass("j")
z = carClass("z")
totrt=z
carList = [a, b, c, d, e, f, g, h, i, j]

def randCar(x):
    return random.choice(x)
       
while True:
    for i in carList:
       print(i.name,i.indx)
    print("new epoch \n")   
    currentCar = randCar(carList)
    currentCar.ind()
    if currentCar.indx == 3:
        if  totrt != currentCar:
           totrt.indx = 0
        totrt = currentCar 
    if currentCar.indx == 4:
       print(f"giriş yapan 4.{currentCar.name} model araç")
       break
        
       

