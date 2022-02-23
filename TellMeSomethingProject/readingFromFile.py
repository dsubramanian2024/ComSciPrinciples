'''
author: Ms. Thuzar
This is a program that reads one line at a time from a file
'''

f = open("textfile.txt", "r")

for line in f:
    print(line)
    print("Do you want to continue?")
    answer = input("Please type y or n: ")
    if answer == 'n':
        break

print("bye")
