'''
Author: Divya Subramanian
Conversions from and to different Bases
'''

def getInt():
  ''' this function takes in an input from the user and keeps asking for an input until the input is a positive integer'''
  num = input("Please enter a positive integer: ")
  if (num.isdigit() == False) or (int(num) < 0):# if int is positive and if it is an integer
    print("Your input is invalid. ")
    num = getInt()
  return int(num) # returns a valid input


def toBaseTen(inBase, inNum):
    ''' coverting inNum from inBase to base ten '''
    bTen = 0
    power = 1 # keeps track of the power of each particular digit
    inBase = int(inBase)
    inNum = str(inNum)
    for i in range (len(inNum)):  # every digit, starting from the last, is multiplied by power and added to the base ten output
      x = ord(inNum[-(i + 1)]) # starts from last digit in string
      if (x > ord("9") and x < ord("A")) or x < ord("0"): # checks if the number is valid
        return -1
      if (x >= ord("A")): # shifts A to 10, B to 11 and so on
        x = x - ord("A") + ord("9") + 1
      x -= ord("0") # converts to integer
      if x >= inBase or x < 0:
          return -1 # the outside function should recall this with a valid input
      bTen += x * power # include letters also
      power *= inBase
    return bTen

def fromBaseTen(bTen, outBase):
    ''' converting from base 10 to outBase '''
    out = "" # the output of the function
    outBase = int(outBase)
    while bTen > 0: # continuously divides bTen by outBase and saves the remainder in out
        rem = bTen % outBase
        bTen -= rem
        if (rem > 9): # shift 10 to A, 11 to B and so on
          rem += ord("A") - 10
          rem = chr(rem)
        out = str(rem) + out
        bTen = bTen // outBase # integer division
    return out

def baseConverter():
    ''' gets inputs from user and converts base'''
    print("What base would you like to start off with? ")
    inBase = getInt()   # check if num is valid

    inNum = input("\nPlease enter a positive integer within base " + str(inBase) + " that you would like to convert: ")

    print("\nWhat base would you like to convert " + str(inNum) + " to? ")
    outBase = getInt()   # check if num is valid

    bTen = toBaseTen(inBase, inNum)
    if (bTen < 0):
        print("\n" + str(inNum) + " is not in base " + str(inBase) + " Please start over.\n\n  ")
        baseConverter()
        return None
    out = fromBaseTen(bTen, outBase)
    print("\n" + str(inNum) + " in base " + str(inBase) + " is " + str(out) + " in base " + str(outBase))

def funcCall():
    '''Greets and informs user about the code. Calls base converter'''
    print("Hi! Nice to meet you.")
    print("This program takes in a number from any base and converts it to any other base! Both of these bases should be positive integers.")
    print("If you would like to input a number between bases 11 and 36, please use capital letters, not lowercase, if necessary. ")
    print("If you would like to input a number that is in base 37 or higher, please use the ascii key values, which can be found on my website, that come directly after the capital letters.\n")
    inp = input("Would you like to convert a number in this calculator. If so, enter 'yes'. Type any other character for no: ")
    while (inp == 'yes'):
        baseConverter()
        inp = input("Would you like to convert another number in this calculator. If so, enter 'yes'. Type any other character for no: ")
    print("\nGoodbye! See you soon! :)")

funcCall()
