"""
Module for demonstrating division and modulo operations.

This module implements a custom divmod function that returns
the quotient and remainder of two integers.
"""

a = int(input())
b = int(input())

def divmod2(arg1, arg2) -> tuple[int, int]:
    """
    Calculate the quotient and remainder of two integers.
    
    Args:
        arg1 (int): The dividend
        arg2 (int): The divisor
        
    Returns:
        tuple[int, int]: A tuple containing (quotient, remainder)
    """
    return int(arg1/arg2), arg1%arg2

result = divmod2(a, b)
print(*result)
print(result)