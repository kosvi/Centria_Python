digits = '0123456789ABCDEFGHIJKLMNO'

def to_decimal(num, base):
    return int(num, base)

# https://stackoverflow.com/a/5797518
def from_decimal(num, base):
    num = int(num)
    if len(digits) < base:
        return "Error!"
    remainder = num % base
    rest = num // base
    if (rest == 0):
        # end of line :)
        return digits[remainder]
    return from_decimal(rest, base) + digits[remainder]
