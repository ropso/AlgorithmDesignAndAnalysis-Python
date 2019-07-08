import re, threading
import math
print(math.factorial(3))
a="the red1233 and the gold"
print(re.sub(r"red(\d{3})",r"REDAND GOLD\1",a))
# () packin is used to pack and unpack the varibaes

threading.Thread()
def my_fun():
    global a
    print("directly from the gloabal land",a)

my_fun()