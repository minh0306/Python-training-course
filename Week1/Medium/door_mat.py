# n, m = input().split()
# n = int(n)
# m = int(m)
n, m = map(int, input().split()) #dùng map để chuyển đổi ngắn gọn hơn
def print_welcome(m):
    print("-" * m + "WELCOME" + "-" * m)
def print_up_and_down(i,mid,m):
    if i<mid:
        pipe=i*2+1
        # dot=pipe*2
        hyphen=int((m-3*pipe)/2)
        print("-"*hyphen + ".|."*pipe + "-"*hyphen)
    elif i==mid:
        print_welcome(int((m-7)/2))
    else:
        pipe=(mid*2-i)*2+1
        hyphen=int((m-3*pipe)/2)
        print("-"*hyphen + ".|."*pipe + "-"*hyphen)


# mid=int((n-1)/2) => dùng phép tính n//2
for i in range (n):
    print_up_and_down(i,n//2,m)

#improve by AI:
# for i in range(n):
#     if i < n // 2:
#         pattern = ".|." * (2 * i + 1)
#     elif i == n // 2:
#         pattern = "WELCOME"
#     else:
#         pattern = ".|." * (2 * (n - i - 1) + 1)

#     print(pattern.center(m, "-"))

