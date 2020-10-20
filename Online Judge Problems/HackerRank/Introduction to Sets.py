def average(array):
    # your code goes here
    s = set(array)
    n = len(s)
    x = sum(s)
    res = x/n
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
