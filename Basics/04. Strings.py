name = 'youtube'    #In python we can represent a string using "" or ''
print(name[0])      #First index
print(name[-1])     #In python negative indexing is allowed. It started counting from the end of the string.
print(name[-7])
print(name[0:2])    #name[m:n]  will print the index value from m to n-1
print(name[1:4])
print(name[1:])     #name[m:]  will print the index value from m to end
print(name[:4])     #name[:n]  will print the index value from 0 to n-1

print(len(name))

#changing 'youtube' to 'mytube'

#name[0] = 'm'
#name[1] = 'y'
#or
#name[0:2] = 'my'
#these codes will give you error. In python we can't change the string index value by assining a new value.

name = 'my' + name[3:]
print(name)
print(len(name))
