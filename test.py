import math
import re

def checkBooleanDivisible(input_str, divisor):
    binary_list = re.split(r'\d+', input_str)
    valid_binaries = []

    for binary_string in binary_list:
        base10_value = int(binary_string, 2)
        try:
            if base10_value % divisor == 0:
                valid_binaries.append(binary_string)
        except ValueError:
            pass

    print(','.join(valid_binaries))


def countDigitNumber(sentence):
    letters = sum(1 for char in sentence if char.isalpha())
    digits = sum(1 for char in sentence if char.isdigit())
    print(f"LETTERS {letters}")
    print(f"DIGITS {digits}")


def compute_factorials(input_string):
    results = [str(math.factorial(int(x.strip()))) for x in re.findall(r'\d+', input_string)]
    print(','.join(results))


checkBooleanDivisible("0100,0011/1010$1001", 5)
countDigitNumber("hello world! 123")
compute_factorials("8 , 5, 3, 2")



