if __name__ == '__main__':
    n = int(input())
    myList = []
    for i in range(n):
        x = input().split(" ")
        command = x[0]
        if command == "insert":
            myList.insert(int(x[1]),int(x[2]))
        elif command == "remove":
            myList.remove(int(x[1]))
        elif command == "append":
            myList.append(int(x[1]))
        elif command =="print":
            print(myList)
        elif command == "pop":
            myList.pop()
        elif command == "sort":
            myList.sort()
        elif command == "reverse":
            myList.reverse()
