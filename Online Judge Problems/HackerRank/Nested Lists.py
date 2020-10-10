marksheet = []
marks = []
n = int(input())
for i in range(n):
    name = input()
    grade = float(input())
    marksheet += [[name,grade]]
    marks += [grade]
x = (sorted(set(marks))) [1]
for i,j in sorted(marksheet):
    if j == x:
        print(i)
