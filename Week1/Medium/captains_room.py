# member_in_group=int(input())
# room_number_list=input()
# Input
k = int(input())                     
rooms = list(map(int, input().split()))  

counts = {}
for r in rooms:
    counts[r] = counts.get(r, 0) + 1

for room, freq in counts.items():
    if freq == 1:
        print(room)
        break