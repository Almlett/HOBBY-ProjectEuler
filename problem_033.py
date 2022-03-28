# Digit cancelling fractions
"""
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

for first_digit in range(10, 100):
    for second_digit in range(10, 100):
        tmp = str(first_digit)
        first_digit_split = [item for item in tmp]
        tmp = str(second_digit)
        second_digit_split = [item for item in tmp]
        # if first_digit_split[0] != first_digit_split[1] and second_digit_split[0] != second_digit_split[1] and first_digit_split[1] != "0" and second_digit_split[1] != "0":

        for item in first_digit_split:
            num1 = 0
            num2 = 0
            if item in second_digit_split:
                second_digit_split.remove(item)
                first_digit_split.remove(item)
                num1 = int(first_digit_split[0])
                num2 = int(second_digit_split[0])
                try:
                    if first_digit/second_digit == num1/num2 and num1 != num2 and num1 != 0 and num1 != 1 and num2 != 0 and num2 != 1 and int(item) != 0 and int(item) != 1:

                        print("{}/{}".format(second_digit, first_digit))
                except Exception:
                    pass

        ''' try:
            if first_digit/second_digit == int(first_digit_split[0])/int(second_digit_split[0]) and first_digit != second_digit and first_digit != 0 and second_digit != 0 and first_digit != 1 and second_digit != 1:
                print(first_digit, second_digit)
                print("ASDas")
                print(int(first_digit_split),
                        int(second_digit_split))
        except Exception:
            pass '''
