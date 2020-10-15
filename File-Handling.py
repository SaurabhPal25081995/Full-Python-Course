# Reading a file

# f = open("check.txt")
# content = f.read()
# print(content)
#
# f.close()

# f = open("check.txt")
# #content = f.read()
# for line in f:
#     print(line,end=" ")
# #print(content)


# f = open("check.txt")
# content = f.readline()
# contents = f.readlines()
# print(content)
# print(contents)
# f.close()
#
# # Writing a file
# f = open("check2.txt","w")
# f.write("Writing new line to this file\n")
# f.write("Writing new line to this file")
# f.close()
#
# fr = open("check2.txt","r")
# content = fr.read()
# print(content)
# fr.close()

# Read and Write by single mode
# f = open("check2.txt","r+")
# print(f.read())
# f.write("\nadding new line by using r+ mode")
# print(f.read())
# f.close()

# Use of seek() and tell()
# f = open("check2.txt")
# print(f.tell())
# print(f.readline())
# print(f.tell())
# print(f.readline())
# print(f.tell())
#
# print("Now pointer is on this position ie ",f.seek(0))
# print("Now pointer is on this position ie ",f.seek(7))
# f.close()

# Another eg of seek and tell
# f = open("check2.txt")
# print(f.readlines())
# print(f.tell())
# print(f.seek(0))
# print(f.readline())

# Open File by using with block
with open("check.txt") as f:
    a = f.readlines()
    print("By readlines---",a)

f = open("check.txt")
print("By read()---",f.read())