#Function for reversing a word

#Example_1 using reversed returning an object not a string
#
# original_string = "hello"
#
# reversed_string = reversed(original_string)
#
# print(reversed_string)
#Result - <reversed object at 0x7f3673710d00>


#Example_2 using the join method
#
# original_string = "hello"
#
# reversed_string = ''.join(reversed(original_string))
#
# print(reversed_string)
#Result - olleh


#Example_3 combining a string or join method with a for loop
#
# original_string = "hello"
#
# reversed_string = reversed(original_string)
#
# reversed_string_using_loop = ''
#
# for i in reversed_string:
#     reversed_string_using_loop = reversed_string_using_loop + i
#
# print(reversed_string_using_loop)
#Result - olleh
#This operation takes way too long so programmers prefer to just use join instead of loop

#Now that we now the join works best we can define it and use it as a function
def reverse_string(word):
    return ''.join(reversed(word))

def test_reverse_string():
    input_string = "TripleTen"

    reversed_string = reverse_string(input_string)

    assert reversed_string == "neTelpirT"

    print("Test Passed! " + input_string + "'s reverse is " + reversed_string )







#Function for palindromes

def is_palindrome(word):

    reversed_string = ''.join(reversed(word))

    return word == reversed_string

def test_is_palindrome():
    input_string = "racecar"
    result = is_palindrome(input_string)
    assert result == True
    print("Test Passed! " + input_string + " result is a palindrome")






#Function that calculates the factorial of a number
import math
print(math.factorial(5))

import math
def compute_factorial(number):
    return math.factorial(number)

def test_compute_factorial():
    input_number = 5
    result = compute_factorial(input_number)
    assert result == 120
    print("Test Passed! The factorial of " + str(input_number) + " is " + str(result))
