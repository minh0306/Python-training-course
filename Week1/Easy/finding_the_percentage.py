number_student=int(input())
student={}

for i in range (number_student):
    string = input().split()
    student[string[0]]=[]
    for mark in string[1:]:
            student[string[0]].append(float(mark))
query_name=input()
avg=sum(student[query_name])/len(student[query_name])
print(f"{avg:.2f}")

#imporve code by using comprehense dict (ask AI):
# n = int(input())
# students = {
#     data[0]: list(map(float, data[1:]))
#     for data in (input().split() for _ in range(n))
# }

#use library for calculate avarage (learn on CS50):
# import statistics
# print(f"{statistics.mean(student[query_name]):.2f}")