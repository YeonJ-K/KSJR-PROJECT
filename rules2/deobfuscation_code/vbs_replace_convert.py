import re
str = ''
a = re.compile("^(E|e)[\\w]{1,12}[\\S][\\w]{1,}", re.I)
find = a.match(str)
if find:
    a = (find.group()).lower().replace("execute", "write")
print(a)