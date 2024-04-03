"""
    We are defining two functions:
        -> The first verifies the credit card number, by encoding the Luhn algorithm with Python 
        -> The second initialises `card_number` with an example credit card number <- To apply this function 

    -> verify_card_number:
        -> About the algorithm this uses, function input: 
            -> The input of this function is a credit card number 
            -> We want to validate the credit card number, to make sure it's a real ('valid') card number
            -> We are doing this by coding the Luhn algorithm into a function
            -> This is a checksum formula <- and it doesn't just apply to credit cards (the algorithm is for 
                validation)
            -> To make sure that for example, this number that we've just been given is actually a credit card 
                number 
"""

def verify_card_number(card_number):

"""
Initialising variables:
	-> We aren't running any module imports when defining this function 
	-> The first stage of defining this function is to initialise variables <- Three of them 
	-> The first is for the sum of the odd digits of the card number (the function input), initialised at zero 
	-> The credit card number is the input to the function 
	-> The second variable we are initialising is this number backwards (all of the elements, stored in descending 
        order)
	-> Then the third variable is the `odd_digits`
		-> This is the card number going backwards,  but the even integers of this 
		-> This also includes all of the numbers on the card (we aren't slicing out some of these numbers)
	-> So we can now store the sum of the odd digits and the sum of the even ones <- We have variables initialised 
        to do this with the credit card number, which is the input to the function 
"""

    sum_of_odd_digits = 0
    card_number_reversed = card_number[::-1]
    odd_digits = card_number_reversed[::2]

"""
Building the sum_of_odd_digits variable: 
-> `odd_digits` is the variable which contains the odd digits in the credit card number <- The input to the function 
-> We are iterating through each of the digits in this larger number, to calculate the value of the sum this variable 
    stores 
-> We are adding them with each iteration to a counter, called `sum_of_odd_digits`
-> It's a way of taking a longer number which is composed of many digits, iterating through each of those digits and 
    with each iteration adding the number to a counter 
-> So after this, we now have the sum of the odd digits in the credit card, which we store in the `sum_of_odd_digits` 
    variable 
"""

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

"""
Initialising the value of variables (continued): 
-> We have one variable for the sum of the even digits 
-> And then we have another variable, which stores the even digits in the card number (function argument)
-> 'Even digit' means the index that the number is stored at in the function input is even, not that the number which 
    is stored at the index is even 
-> We are now repeating the process we just did for the odd numbers, but for the even numbers
-> Initialising the sum of these numbers as 0, in the `sum_of_even_digits` variable 
-> And then even_digits <- This variable stores those numbers themselves
-> Start from the second number (zero-indexed) in the input string, and then increase in increments of 2 
-> Do this for the entire input string, and now we have a list of all of the numbers in the input string which were 
    stored at even indices in it 
-> This is an example of slicing 
"""

    sum_of_even_digits = 0
    even_digits = card_number_reversed[1::2]



    for digit in even_digits:
        number = int(digit) * 2
        if number >= 10:
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    total = sum_of_odd_digits + sum_of_even_digits
    return total % 10 == 0

def main():
    card_number = '4111-1111-1111-1111'
    card_translation = str.maketrans({'-': '', ' ': ''})
    translated_card_number = card_number.translate(card_translation)

    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')
main()
