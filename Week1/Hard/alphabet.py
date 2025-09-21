alphabet = [
    "a","b","c","d","e","f","g","h","i","j",
    "k","l","m","n","o","p","q","r","s","t",
    "u","v","w","x","y","z"
    ]
def get_pattern(size,i):
    if i<size:
        arr=alphabet[(size-i-1):size]
        # arr1=list(reversed(arr))+arr[1:]     =>[::-1] là cú pháp đảo ngược
    else:
        arr=alphabet[(i-size):size][1:]
    return "-".join(arr[::-1] +arr[1:] )

    
def print_rangoli(size):
    for i in range(size*2-1):
        print(get_pattern(size,i).center(size*4-3,"-"))

# improve by AI
# import string
# alphabet = list(string.ascii_lowercase)

# def print_rangoli(size):
#     for i in range(2*size - 1):
#         idx = size - 1 - abs(size - 1 - i)   #dùng abs trị tuyệt đối để trừ bỏ if else
#         arr = alphabet[size-idx-1:size]
#         row = arr[::-1] + arr[1:]
#         print("-".join(row).center(4*size - 3, "-"))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)