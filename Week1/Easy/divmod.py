a=int(input())
b=int(input())
def divmod(a,b):
    return int(a/b),a%b
print(*divmod(a,b),divmod(a,b),sep="\n")