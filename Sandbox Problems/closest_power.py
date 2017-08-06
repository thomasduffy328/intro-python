def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base ** exponent is closest to num.
    Note that the base ** exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    if base > num:
        return 0
    power = 0
    while base ** power < num:
        power += 1
    lower = base ** (power - 1)
    upper = base ** power
    if abs(num - lower) <= abs(num - upper):
        return power - 1
    else:
        return power
