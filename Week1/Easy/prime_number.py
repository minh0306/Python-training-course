def prime_number_checker(number:int):
    if number < 2:
        return False
    if number % 2 == 0:
        return False
    if number == 2:
        return True
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    return True
if __name__ == '__main__':
    n = int(input("Nhập số kiểm tra: "))
    print(f"{n} là số nguyên tố" if prime_number_checker(n) else f"{n} không phải là số nguyên tố")
