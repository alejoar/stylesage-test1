def translate(number):
    """Generates a string representation of an integer with commas separating
    groups of 3 digits
    """

    try:
        number = str(int(number))
    except ValueError:
        raise ValueError('Not a number!')

    final = []
    trio = number[-3:]
    i = 0

    while trio:
        final.insert(0, trio)
        i += 3
        trio = number[-i-3:-i]

    return ','.join(final)
