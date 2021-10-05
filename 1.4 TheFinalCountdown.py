import time
from PIL import Image
image = Image.open('C:\\Users\\bosbr\\OneDrive\\Afbeeldingen\\obama.png')
i = 1000
while i > 0:
  print(i)
  i -= 1
  time.sleep(0.1)
if i == 0:
    print("0")
    time.sleep(1.0)
    image.show()
    print("NOOO")
    print("Its Obama")
    time.sleep(5.0)