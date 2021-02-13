import random
import string

password = ""

def numPass():
    global password
    password = ""
    for i in range(8):
        randInt = str(random.randint(0, 9))
        password += randInt

def alphaPass():
    global password
    password = ""
    for i in range(8):
        randStr = str(random.choice(string.ascii_letters))
        password += randStr

def alphaNumPass():
    global password
    password = ""
    for i in range(8):
        randInt = random.randint(0, 9)
        randStr = random.choice(string.ascii_letters)
        randList = (randInt, randStr)
        randIntStr = str(random.choice(randList))
        password += randIntStr


if __name__ == "__main__":
    alphaNumPass()
    print(password)