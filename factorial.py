import time
import sys

def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta = respuesta * n
        n = n - 1

    return respuesta


def factorial_re(n):
    if n == 1:
        return 1

    return n * factorial_re(n - 1)


if __name__ == '__main__':
    n = 1000
    sys.setrecursionlimit(n + 10)

    comienzo = time.time()
    factorial(n)
    final = time.time()
    print(f"tiempo con bucle\t{final - comienzo}");

    comienzo = time.time()
    factorial_re(n)
    final = time.time()
    print(f"tiempo recursivo \t{final - stacomienzortingTime}");