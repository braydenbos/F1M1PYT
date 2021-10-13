import time
from PIL import Image
image = Image.open('C:\\Users\\bosbr\\OneDrive\\Bureaublad\\MA\\Bewijzenmap\\Periode 1.1\\PYT\\obama.png')
i = 10
while i > 0:
  print(i)
  i -= 1
  time.sleep(1.0)
if i == 0:
    print("0")
    time.sleep(1.0)
    image.show()
    print("NOOO")
    print("Its Obama")
    time.sleep(5.0)