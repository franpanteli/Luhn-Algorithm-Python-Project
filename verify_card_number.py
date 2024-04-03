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

    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

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
