"""
def findNumber(number):
    myNumber = 72
    if(number < myNumber):
        return "Please retry my number is above yours"
    elif number == myNumber:
        return "Well Done!"
    else:
        return "Your number is bigger than mine"



number = int(input("Please enter a number between 0 and 100: "))

while(number <0 or number > 100):
    number = int(input("Please enter a number between 0 and 100"))
while number:
    if findNumber(number) == "Well Done!":
        print(findNumber(number))
        number = 0
    else:
        print(findNumber(number))
        number = int(input("Please enter a number between 0 and 100: "))"""

#örnek Mülakat sorusu çözümü

myList =  [1,2,3,4,5,6,7,1]

def cozumFonk():
    myHashSet  = set()

    for num in myList:
        if num in myHashSet:
            return True
        myHashSet.add(num)
    return False

def cozum2():
    return len(myList) != len(set(myList))
print(cozum2())