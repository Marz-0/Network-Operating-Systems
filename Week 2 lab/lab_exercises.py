

#Revision - Basic math operations


def add():
    num1 = 10
    num2 = 20
    return num1 + num2

#print(add())


def subtract():
    num1 = 10
    num2 = 20
    return num2 - num1

#print(subtract())


def multiply():
    num1 = 10
    num2 = 20
    return num1 * num2

#print(multiply())

def div():
    num1 = 10
    num2 = 20
    return num2 / num1

#print(div())

def remainder():
    num1 = 15
    num2 = 20
    return num2 % num1

#print(remainder())

def power():
    num1 = 2
    num2 = 5
    return num1 ** num2

#print (power())


#Exercise 2 - Python data types

fruitlist = ['apple', 'banna', 'watermelon', 'pear', 'grape']
#print(fruitlist)

#for value in fruitlist:
    #print(value)



thistuple = ('cat', 'horse', 'lion')
#print(thistuple)


thisdict = {'python': 1991,
            'java': 1995,
            'HTML': 1993}

#print(thisdict)


thisset = {'green', 'blue', 'pruple'}
#print(thisset)


sentence1 = "Python is an easy-to-learn programming language."
#print(sentence1)



#Exercise 3 - Conditionals

def checknum():
    user_num_input = int(input("Enter a number: "))
    if user_num_input > 0:
        print("The number is positive.")
    elif user_num_input < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

#checknum()


def checkvoul():
    user_char_input = input("Enter a word: ").lower()
    
    if user_char_input[0] in 'aeiou':
        print("The word starts with a vowel.")
    else:
        print("The word starts with a consonant.")

#checkvoul()

def equalornot():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num1 == num2:
        print("The numbers are equal.")
    else:
        print("The numbers are not equal.")
        
#equalornot()


#Exercise 4 - Loops


def one_to_ten():
    for i in range(1, 11):
        print(i)

#one_to_ten()


def two_to_ten_even():
    for i in range(2, 11, 2):
        print(i)

#two_to_ten_even()



def five_fib():

    a, b = 0, 1
    count = 0

    while count < 5:
        print(a)
        a, b = b, a + b
        count += 1

#five_fib()

