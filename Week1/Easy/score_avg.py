def score_avg(list: [int]):
    return round(sum(list)/len(list),2)
if __name__=='__main__':
    avg= score_avg([int(i) for i in input("Nhập danh sách điểm:").split()])
    print(f"Điểm trung bình các môn là:{avg}")