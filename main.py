from math import trunc
from math import log
from math import ceil

from random import randint

# interesting number check functions:
def digit_trunc(number):
    """
    Parameters:
     - number (int)

    Returns:
     - The last digit of a number (int)
    """
    return int(str(number)[-1])

def is_digit_followed_by_zeroes(number):
    """
    Parameters:
     - number (int)

    Returns:
     - True if number is one digit followed by only zeroes (e.g. 30000, 600, 900000)
     - False if number isn't prime
    """
    if len(str(number)) == 1:
        return False
    try:
        number_str = str(number)
        if number_str[1:] == ("0") * (len(number_str) - 1):
            return True
    except ValueError: return False
    return False

def is_pow_of_given_int(number, base):
    """
    Parameters:
     - number (int)
     - base (int)

    Returns:
     - True if number can be expressed in the form base**x, where: base, x ∈ N
     - False if number can't be expressed in the form base**x, where: base, x ∈ N
    """
    try:
        if ceil(log(number, base)) == log(number, base): # check if float ≡ int
            return True
    except ValueError: return False
    return False

def is_pow_of_int(number, max_base = 9):
    """
    Parameters:
     - number (int)
     - max_base (int)

    Returns:
     - [True, base] if number can be expressed in the form base**x, where: base, x ∈ N
     - False if number can't be expressed in the form base**x, where: base, x ∈ N
    """
    try:
        for base in range(2, max_base + 1): 
            if is_pow_of_given_int(number, base) == True: return [True, base]
    except ValueError: return False
    return False

def is_all_repeated_digit(number):
    """
    Parameters:
     - number (int)

    Returns:
     - True if number is made up of only 1 repeated digit
     - False if number isn't made up of only 1 repeated digit
    """
    number_str = str(number)
    if number_str == number_str[0] * len(number_str):
        return True
    return False

    # The digits are sequential, incementing: 1234

def is_asc_or_dec(number, include_asc = True, include_dec = True):
    """
    Parameters:
     - number (int)
     - include_asc (bool)
     - include_dec (bool)

    Returns:
     - True if number's digits are in ascending or descending order
     - False if number's digits aren't in ascending or descending order
    """
    number_str = str(number)
    if len(number_str) <= 2:
        return False
    if include_asc == True:
        is_asc = True
        prev_i = 0 # placeholder value
        for i in range(len(number_str)):
            if i != 0:
                if digit_trunc(int(prev_i) + 1) != int(number_str[i]):
                    is_asc = False
                    break
            prev_i = number_str[i]
        if is_asc == True:  return True

    if include_dec == True:
        is_dec = True
        prev_i = 0 # placeholder value
        number_str_inverted = number_str[::-1]
        for i in range(len(number_str)):
            if i != 0:
                if digit_trunc(int(prev_i) + 1) != int(number_str_inverted[i]):
                    is_dec = False
                    break
            prev_i = number_str_inverted[i]
        if is_dec == True: return True

    return False

def is_palin(number):
    """
    Parameters:
     - number (int)

    Returns:
     - True if number is palindromic
     - False if number isn't palindromic
    """
    number_str = str(number)
    is_palin = True
    for i in range(trunc(len(number_str) / 2) + 1): # only needs to check halfway through the list (rounded up)
        if number_str[i] != number_str[-(i + 1)]:
            is_palin = False
            break
    if is_palin == True: return True
    return False

def is_prime(number, itterations=5): # Miller-Rabin primality test (credit to https://stackoverflow.com/users/448810/user448810)
    """
    (not 100% accurate)
    Parameters:
     - number (int)
     - itterations (int)

    Returns:
     - True if number is prime
     - False if number isn't prime
    """
    if number < 2: return False
    for prime in [2,3,5,7,11,13,17,19,23,29]:
        if number % prime == 0: return number == prime
    exponent, odd_int = 0, number - 1
    while odd_int % 2 == 0:
        exponent, odd_int = exponent + 1, odd_int // 2
    for i in range(itterations):
        base_value = pow(randint(2, number - 1), odd_int, number)
        if base_value == 1 or base_value == number - 1: continue
        for r in range(1, exponent):
            base_value = (base_value ** 2) % number
            if base_value == 1: return False
            if base_value == number - 1: break
        else: return False
    return True

def is_narc(number):
    """
    Parameters:
     - number (int)

    Returns:
     - True if number is narcissistic (i.e. equal to the sum of its own digits each raised to the power of the number of digits)
     - False if number isn't narcissistic
    """
    number_str = str(number)
    num_length = len(number_str)
    narc_number = 0
    for digit in number_str:
        narc_number += int(digit) ** num_length
    return number == narc_number

def is_happy(number):
    """
    Parameters:
     - number (int)

    Returns:
     - True if number is happy (i.e. a number which eventually reaches 1 when replaced by the sum of the square of each digit)
     - False if number isn't happy
    """

    past_number_str = str(number)
    number_str = 0
    for digit in past_number_str:
        number_str += 
    past_number_str = number_str

# main function:
def interesting_properties(number, interesting_numbers = {}):
    """
    (see README.md for a definition of an interesting number)\n
    Parameters:
     - number (int)
     - interesting_numbers (list, set, tuple, int)

    Returns:
     - a set containing the number's interesting properties if number is interesting
     - False if number isn't interesting
    """
    number_properties = set(())
    try:
        # normalising parameters:
        number = int(number)
        if type(interesting_numbers) == type(1) or type(interesting_numbers) == type("1"): # if int or str
            int(interesting_numbers)
            interesting_numbers = set([interesting_numbers])
        else: set(interesting_numbers)
        
        # interesting number qualifiers:
        if is_digit_followed_by_zeroes(number) == True: number_properties.add("followed by zeroes")
        if is_all_repeated_digit(number) == True: number_properties.add("all repeated digit")
        if is_asc_or_dec(number) == True: number_properties.add("ascending or descending")
        if is_palin(number) == True: number_properties.add("palindromic")
        if is_prime(number) == True: number_properties.add("prime")
        pow_of_int_property = is_pow_of_int(number)
        if pow_of_int_property != False: number_properties.add(f"power of {pow_of_int_property[1]}")
        if is_narc(number) == True: number_properties.add("narcissistic")
        if number in interesting_numbers: number_properties.add("in interesting_numbers")
        if number_properties == set(()):
            number_properties = None
        return number_properties
    except ValueError: ValueError
    return False

def is_int_interesting(number, interesting_numbers = {}):
    """
    (see README.md for a definition of an interesting number)\n
    Parameters:
     - number (int)
     - interesting_numbers (list, set, tuple, int)

    Returns:
     - True if number is interesting
     - False if number isn't interesting
    """
    if interesting_properties(number, interesting_numbers) == None or interesting_properties(number) == False: return False
    return True


# random tests:
def random_test(interval_start = 1, interval_end = 2**64):
    """
    Parameters:
     - interval_start (int), inclusive
     - interval_end (int), inclusive
    
    Returns:
     - True if the random number is interesting
     - False if the random number isn't interesting
    """
    if is_int_interesting(randint(interval_start, interval_end)):
        return True
    return False

def random_test_until_true(interval_start = 1, interval_end = 2**64, max_randints_generated = 2**8):
    """    
    Parameters:
     - interval_start (int), inclusive
     - interval_end (int), inclusive
     - max_randints_generated (int), reccomended to be no higher than 2**8

    Returns:
     - [number, "randints generated = " + str(count)] if an interesting random number is found
     - ["no interesting number found", "randints generated = " + str(count)] False if an interesting random number isn't found
    """
    interesting_int_found = False
    count = 1
    while count <= max_randints_generated and interesting_int_found == False:
        number = randint(interval_start, interval_end)
        if is_int_interesting(number) == True:
            return [number, "randints generated = " + str(count)]
        count += 1
    return ["no interesting number found", "randints generated = " + str(count - 1)] # (count - 1) b/c the final count += 1 at the end of the while loop overestimates the count by 1


# asserts:
assert digit_trunc(10) == 0
assert digit_trunc(24356) == 6

assert is_digit_followed_by_zeroes(4000) == True
assert is_digit_followed_by_zeroes(12000) == False
assert is_digit_followed_by_zeroes(6) == False

assert is_pow_of_given_int(19**3, 19) == True
assert is_pow_of_given_int(3**5 + 1, 3) == False

assert is_pow_of_int(3**9) == [True, 3]
assert is_pow_of_int(5**6, 3) == False

assert is_all_repeated_digit(88888888) == True
assert is_all_repeated_digit(55543233) == False

assert is_asc_or_dec(90123) == True
assert is_asc_or_dec(2109876) == True
assert is_asc_or_dec(4333333) == False
assert is_asc_or_dec(11112) == False
assert is_asc_or_dec(456, include_asc = True, include_dec = False) == True
assert is_asc_or_dec(76543, include_asc = False, include_dec = True) == True
assert is_asc_or_dec(289340, include_asc = True, include_dec = True) == False
assert is_asc_or_dec(76543, include_asc = True, include_dec = False) == False
assert is_asc_or_dec(78901, include_asc = False, include_dec = True) == False
assert is_asc_or_dec(78901, include_asc = False, include_dec = True) == False

assert is_palin(644232446) == True
assert is_palin(345345) == False

assert is_prime(80941897) == True
assert is_prime(739*103) == False

assert is_narc(9474) == True
assert is_narc(150) == False

assert interesting_properties(56) == None
assert interesting_properties(2**6) == {'power of 2'}

assert is_int_interesting(1) == True
assert is_int_interesting(3443) == True
assert is_int_interesting(500) == True
assert is_int_interesting(283) == True
assert is_int_interesting("boop oop soup") == False

assert is_int_interesting(12312, [12312, 234987234, 131023]) == True
assert is_int_interesting("testing", {"testing"}) == False # only accepts ints
assert is_int_interesting(14.7, {14.7}) == False # only accepts ints
assert is_int_interesting(314159, 314159) == True
