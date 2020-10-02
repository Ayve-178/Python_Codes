if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        x = input().split(" ")
        name = x[0]
        m1 = float(x[1])
        m2 = float(x[2])
        m3 = float(x[3])
        avg = (m1+m2+m3)/3
        student_marks[name] = avg
    name = input()
    out = "{:.2f}".format(student_marks[name])
    print(out)
