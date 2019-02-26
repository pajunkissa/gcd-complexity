# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

def badGCD(n, m):
    """
    A naive and unintuitive algorithm that calculates the greatest common
    divisor of two numbers. 
    Arguments: non-negative integers n and m
    Returns: gcd(n, m) and the number of iterations (~ nmber of subtractions
    and comparisons) needed.
    """
    rounds = 0
    while n > 0 and m > 0:
        if n > m:
            n -= m
        else:
            m -= n
        rounds += 1
    return((n, rounds))


def GCD(n, m):
    """
    The classic Euclidean algorithm
    Arguments: non-negative integers n and m
    Returns: the gcd of n and m and the number of iterations needed
    """
    q = max(n, m)
    r = min(n, m)
    rounds = 0
    print (rounds, q, r)
    while r != 0:
        q, r = r, q % r
        rounds += 1
        print (rounds, q, r)
    return (q, r, rounds)