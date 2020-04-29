# greatest common divisor function
def gcd(m, n):
    while m % n != 0:
        m, n = n, m % n
    return n
