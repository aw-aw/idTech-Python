# Examples taken from https://www.w3schools.com/python/python_for_loops.asp


def forEachLoop():
    fruits = ["apple", "banana", "cherry"]
    for fruit in fruits:
      print(fruit)


def stringLoop():
    for x in "banana":
        print(x)


def breakLoop1():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        print(x)
        if x == "banana":
            break


def breakLoop2():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            break
        print(x)

def continueLoop():
    fruits = ["apple", "banana", "cherry"]
    for x in fruits:
        if x == "banana":
            continue
        print(x)

def forRange():
    for x in range(6):
        print(x)

def forRangeStart():
    for x in range(2, 6):
        print(x)

def forRangeJump():
    for x in range(2, 30, 3):
        print(x)

def nestedLoops():
    adjs = ["red", "big", "tasty"]
    fruits = ["apple", "banana", "cherry"]
    for adj in adjs:
        for fruit in fruits:
            print(adj, fruit)



def printName(name1, name2):
    print(name1, name2)


printName("A.W.", "Thomas")
