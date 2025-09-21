
# Complete the solve function below.
def solve(s):
    # return s.title()            # fail case nếu chuỗi bắt đầu bằng số thì skip
    result=''
    # str= s.split()              #fail vì sẽ tự động bỏ luôn space đầu cuối
    for i in s.split(" "):
        # try:                    #fail vì sẽ xảy ra IndexError khi i[0]==" " mà k catch lỗi này
        #     float(i[0])
        # except ValueError:
        #     result+=i.title()+" "
        # else:
        #     result+=i+" "
        if i.isalpha():             
            result+=i.title()+" "
        else:
            result+=i+" "
    return result

#improve code by AI:
# def solve(s):
#     return " ".join(
#         word.capitalize() if word and word[0].isalpha() else word
#         for word in s.split(" ")
#     )
    
if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    # fptr.write(result + '\n')
    print(result + '\n')
    # fptr.close()