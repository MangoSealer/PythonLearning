import string
import time
import random

target = "Hello World"
letters = string.ascii_letters + " "
result = ""
for letter in target:
    while True:
        i = random.choice(letters)
        print(result + i)
        if i == letter:
            result += i
            break
    time.sleep(0.1)
