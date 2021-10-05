import time
from os import system, name

def clear():
    if name == "nt":
        _ = system("cls")
    else:
        _=system("clear")
factory = ["phone"]
distributor = []
shop = []
i=1

while i==1:
    string=' '.join([str(item) for item in factory])
    clear()
    print("Factory: ["+string+"]")
    print("Distributor: []")
    print("Shop: []")
    time.sleep(2)
    clear()
    print("Factory: []")
    print("Distributor: ["+string+"]")
    print("Shop: []") 
    time.sleep(2)
    clear()
    print("Factory: []")
    print("Distributor: []")
    print("Shop: ["+string+"]")
    time.sleep(2)
    i=0
while i==0:
    restart=input("Restart Y/N: ")
    if restart=='N':
        break
    elif restart =='Y':
        i=1
    else:
        print("not correct input")