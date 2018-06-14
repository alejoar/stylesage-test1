
def translate(number):
    final = []
    trio = number[-3:]
    i = 0

    while trio:
        final.insert(0, trio)
        i += 3
        trio = number[-i-3:-i]

    return ','.join(final)
