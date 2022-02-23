'''
Divya Subramanian
Iterative and Recursive Functions

'''


def reverseStr_i(inp):
  ''' This function takes in a string and copies its values backwards into a new string '''
  out = ""
  index = len(inp) - 1
  while index >= 0:
      out += inp[index]
      index -= 1
  return out

def reverseStr_r(inp):
    ''' This function takes in a string and returns the last element and recursively calls itself with the string up untill the second to last element'''
    if len(inp) <= 1: #base case
        return inp
    return inp[-1] + reverseStr_r(inp[0:-1])


def sumOfDigits_i(int):
    '''This function takes in an integer, makes it positive, counts the sum of the digits, and then returns the sum '''
    sum = 0
    if (int < 0):
        int *= -1
    while int > 0: # counts each digit by finding the remainder when dividing by 10
        num = int % 10
        int = (int - num) / 10
        sum += num
    return sum

def sumOfDigits_r(int):
    '''takes in an integer and returns the last digit and then calls itself with the int without the last digit. Function stops calling itself when the int == 0'''
    if (int == 0): # base case
        return int
    if (int < 0):
        int *= -1
    return (int % 10) + sumOfDigits_r((int - (int % 10)) / 10)


def binaryStr_i(num):
    '''This function takes in an integer and returns the binary form of that number in a string my repeatedly dividing by 2 and saving the remainder'''
    bin = ''
    if ((isinstance(num, int) == False) or (num <= 0)): # if num is negative or not a base 10 integer
        return 'Input is not valid. It must be a positive decimal integer'
    while (num > 0):
        rem = num % 2
        num -= rem
        bin = str(rem) + bin
        num = num // 2 # integer division
    return bin

def binaryStr_r(num):
    '''This function takes in an integer, checks that it is valid, recursively calls itself with the number divided by 2, and returns the binary number'''
    if (num < 0): # if num is negative or not a base 10 integer
      return 'Input is not valid. It must be a positive decimal integer'
    if (num == 0): # base case
      return ''
    return str(binaryStr_r((num - (num % 2)) // 2)) + str(num % 2)


def consecutivePairs_i(str):
    '''This function goes through the inputted string to see if a character is repeated by checking two characters at a time and returns the number of consecutive pairs there are in the string'''
    count = 0
    i = 0
    while (i < len(str)):
        if (str[i] == str[i+1]):
            i += 2
            count += 1
        i += 1
    return count

def consecutivePairs_r(str):
    '''This function takes in a string and recursively checks two charachters at a time to see if there are any consecutive pairs. It returns the number of consecutive pairs of characters.'''
    if (len(str) <= 1):
        return 0
    if (str[0] == str[1]):
        return consecutivePairs_r(str[2:]) + 1
    return consecutivePairs_r(str[1:])


def bsearch_i(list, key):
    '''This function searches through a sorted list by checking the midpoint and moving up or down accordingly. It returns the index of the key'''
    low = 0
    high = len(list) - 1
    while (low <= high): # makes sure the element is in the list
        midpt = (low + high) // 2
        if (key > list[midpt]):
            low = midpt + 1
        elif (key < list[midpt]):
            high = midpt - 1
        elif(key == list[midpt]):
            return midpt
    return -1

def bsearch_r(list, key, low, high):
    '''This function takes in a list, a key, and the start and end of the list. By finding the midpoint and comparing the key to this element, the function recursively finds and returns which element in the list the key is in. If the key is not present, -1 is returned.'''
    midpt = (low + high) // 2
    if (high >= low):
        if (key > list[midpt]):
            return bsearch_r(list, key, midpt + 1, high)
        if (key < list[midpt]):
            return bsearch_r(list, key, low, midpt - 1)
        if (key == list[midpt]):
            return midpt
    return -1


def testCases0():
    print("This is question 0")
    print("This is the iterative way:")
    print(reverseStr_i("Hello Divya!"))
    print(reverseStr_i(""))
    print(reverseStr_i("H1!"))
    print("-----------------------------")
    print("This is the recursive way:")
    print(reverseStr_r("Hello Divya!"))
    print(reverseStr_r(""))
    print(reverseStr_r("H1!"))
    print('\n')

def testCases1():
    print("This is question 1")
    print("This is the iterative way:")
    print(sumOfDigits_i(104853))
    print(sumOfDigits_i(-528))
    print(sumOfDigits_i(1))
    print("-----------------------------")
    print("This is the recursive way:")
    print(sumOfDigits_r(104853))
    print(sumOfDigits_r(-528))
    print(sumOfDigits_r(1))
    print('\n')

def testCases2():
    print("This is question 2")
    print("This is the iterative way:")
    print(binaryStr_i(1079))
    print(binaryStr_i(-98))
    print(binaryStr_i(3))
    print("-----------------------------")
    print("This is the recursive way:")
    print(binaryStr_r(1079))
    print(binaryStr_r(-98))
    print(binaryStr_r(3))
    print('\n')

def testCases3():
    print("This is question 3")
    print("This is the iterative way:")
    print(consecutivePairs_i(""))
    print(consecutivePairs_i("2aabbbcdda"))
    print(consecutivePairs_i("aab"))
    print("-----------------------------")
    print("This is the recursive way:")
    print(consecutivePairs_r(""))
    print(consecutivePairs_r("2aabbbcdda"))
    print(consecutivePairs_r("aab"))
    print('\n')

def testCases4():
    print("This is question 4")
    print("This is the iterative way:")
    list = [-1, 2, 3, 4, 7, 43]
    print(bsearch_i(list, 56))
    print(bsearch_i(list, 43))
    print(bsearch_i(list, 0))
    print("-----------------------------")
    print("This is the recursive way:")
    print(bsearch_r(list, 56, 0, len(list) - 1))
    print(bsearch_r(list, 43, 0, len(list) - 1))
    print(bsearch_r(list, 0, 0, len(list) - 1))
    print('\n')

def main():
    testCases0()
    testCases1()
    testCases2()
    testCases3()
    testCases4()

main()
