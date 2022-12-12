import random
import math


def operationAS():
    signs = ['+', '-']
    rdSign = random.choice(signs)

    counter = 0

    for i in range(300):
        rdSign = random.choice(signs)
        fN = random.randint(0, 100) * 2 - 3
        sN = random.randint(0, 100) * 2 + 1

        if fN - sN > 0:
            if counter < 100:
                result = print(fN, rdSign, sN, '=')
            counter += 1
    return result


operationAS()
