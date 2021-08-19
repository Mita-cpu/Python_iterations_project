#Python Iteration activities

#  A method that takes in a string word and returns the true if the word is a palindrome, false otherwise.
def is_palindrome(word):
    characters = list(word)
    is_palindrome = True

    for character in characters:
        if character[0] == characters[-1]:
            characters.pop()
        else:
            is_palindrome= False
            break

    print(is_palindrome)

is_palindrome("took")


#  A method that takes an array of numbers and returns a new array ,
# where every element of the original array is multiplied by 2.

def doubler(numbers):
    my_list = []
    for i in numbers:
        my_list.append(i * 2)

    print(my_list)

doubler([3,4,2,5])


# A method that takes in a string name and returns a string saying bye to that name.

def goodbye(name):

    print("Good bye",name)

goodbye("Mita")


# A method that returns the average of three numbers

def average_of_three(num1, num2, num3):
    total_average= (num1 + num2 + num3) // 3

    print(total_average)

average_of_three(20,43,2)


# A method that takes in a number and returns an array containing all numbers greater than 0 and 
# less the number that are divisible by either 4 or 6, but not both.

def fizz_buzz(max):
    nums = []
    i = 0
    while i < max:
        
        if (i % 4 == 0 or i % 6 == 0) and not(i % 4 == 0 and i % 6 == 0):
            nums.append(i)
        i += 1 

    print(nums)

fizz_buzz(100)


###### END    

