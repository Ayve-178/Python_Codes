def count_substring(string,sub_string):
    c = 0
    ls = len(string)
    lss = len(sub_string)
    for i in range(ls-lss+1):
        if string[i:(i+lss)] == sub_string:
            c+=1
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
