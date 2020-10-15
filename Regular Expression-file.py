import re
# mystr = "Hi Tata fass iin innbye +915555, +916666, +910123456789"
# patt = re.finditer('^inn',mystr)
# patt = re.compile(r"[+91]{3} [0-9]{10}")
# patt = re.compile(r'.adm')
# patt = re.compile(r'^Tata')
# patt = re.compile(r'iin$')
# patt = re.compile(r'ai{2}')
# patt = re.compile(r'(ai){1}')
# patt = re.compile(r'ai{1}|Fax')



# Special Sequences
# patt = re.compile(r'Fax\b')
# patt = re.compile(r'27\b')
# patt = re.compile(r'\d{5}-\d{4}')
# Task
# Given a string with a lot of indian phone numbers starting from +91

# matches = patt.finditer(mystr)
# for match in matches:
#     print(match)


# For mobile number extractor
# x = re.findall(r"[+91]{3}[0-9]{10}",mystr)
# print(x)

# For email extractor
str = "saurabhpal25@@@gmail .com hi saurabh oak@yah  jio@coo.com sfs  o@g.c sfd s gaga@gmail.com gs a s s s fsdfd fsd fsdffd"
x=re.findall(r'\w+@\S+\w',str)
print(x)

f = open("email.txt","a")
j=1
for i in x:
    f.write(f"Email{j}- {i}\n")
    j+=1
f.close()

print(f"Email's are :{x}")
print(f"Total Email are: {j-1}")
