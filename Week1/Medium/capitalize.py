import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    # return s.title()
    result=''
    # str= s.split()
    for i in s.split(" "):
        # result+=i.capitalize()+" "
        try: 
            float(i[0])
        except ValueError:
            result+=i.title()+" "
        else:
            result+=i+" "
    return result
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()