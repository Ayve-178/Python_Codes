eng = int(input())
eng_roll = set(map(int,input().split()))
fren = int(input())
fren_roll = set(map(int,input().split()))

print(len(eng_roll & fren_roll))
