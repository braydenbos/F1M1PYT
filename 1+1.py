import time
question = '21'
ask = 1
if ask ==1:
    sum1=input("number 1: ")
    sum2=input("number 2: ")
    ask = '21'

while question != '21':
    question=input("What is "+sum1+"+ "+sum2+": ")
    time.sleep(1.0)
else:
    print("congrats")