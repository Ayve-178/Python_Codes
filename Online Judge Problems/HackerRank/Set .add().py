if __name__ == "__main__":
    n = int(input())
    s = set([])
    for i in range(n):
        x = input()
        s.add(x)
    print(len(s))
