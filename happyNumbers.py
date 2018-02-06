def userInput():
    while True:
        x = raw_input("Enter number")

        try:
            number = int(x)
            if number > 0:
                return number
            else:
                print "Enter a valid number"
        except ValueError:
            print "Enter a number"

def splitNumber(no):
    numStr = str(no)
    listNumber = []
    for n in numStr:
        listNumber.append(int(n))
    return listNumber

def calc(listNumber):
    sum = 0
    for n in listNumber:
        sum+=n ** 2
    return sum

def main():
    no = userInput()
    sum = no
    prevNumbers = []
    while sum != 1:
        sum = calc(splitNumber(sum))
        print sum
        if sum in prevNumbers:
            break
        prevNumbers.append(sum)


    if sum == 1:
        print "Entered number is a Happy number"
    else:
        print "Entered number is not a Happy number"

if __name__ == "__main__":
    main()