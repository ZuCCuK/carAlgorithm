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
    try:
        chs = int(input("0 = A\n1 = B\n2=C\n3 = D\n4 = E\n5 = F\n6 = G\n7 = H\n 8 = İ\n9 = JListedeki araçlardan hangisini seçmek istiyorsanız ona karşılık gelen rakamı yazın."))#randCar(carList)
        currentCar = carList[chs]
    except:
       print("Doğru değeri girdiğinizden emin olunuz")
    currentCar.ind()
    if currentCar.indx == 3:
        if  totrt != currentCar:
           totrt.indx = 0
        totrt = currentCar 
    if currentCar.indx == 4:
       print(f"giriş yapan 4.{currentCar.name} model araç")
       break
        

