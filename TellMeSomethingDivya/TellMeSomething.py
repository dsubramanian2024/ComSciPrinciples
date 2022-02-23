#Author: Divya
# Has a conversation with user about me

def correctInput(array, ans): #takes in an array of the acceptable answers and an inputted answer
    for i in array:
        if i == ans:
            return ans #returns a valid response
    ans2 = input("Your answer is invalid. Please enter a valid response: ")
    return correctInput(array, ans2)

f = open("TellMeSomething.txt", "r")

name = input ("Hi! My name is Divya. What is your name?\n")
print("Nice to meet you " + name + ". Here are some fun facts about me!\n")

b = True #this is to see if every line of the .txt file was read

for line in f: #reads and prints the lines of .txt file
    print(line)
    print(name + ", would you like to learn more about me?\n")
    ans = input("Enter yes or no:  ")
    ans = correctInput(["yes", "no"], ans)
    if ans == "no":
        b = False
        break

if b == True: #when all the lines from the .txt file are read
    print("Oops! I have run out of interesting facts!\n")

print("It was nice meeting you " + name + ". I hope you enjoyed learning about me! Bye:)\n")
