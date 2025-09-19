# def split_and_join(line):
#     return "-".join(line.split())

#not use build-in funct:
def split_and_join(line):
    str=''
    for i in line:
        if i ==" ":
            str+="-"
        else:
            str+=i
    return str


if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)