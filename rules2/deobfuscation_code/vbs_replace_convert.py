import re
str = 'ExecutEglobAl(Tr) :'
a = re.compile("(?=(E|e)[\w]{1,12}[\S][\w]{1,}[\W])(?=(E|e)[\w]{3,}[\S]*[\s]{1,}).*")
find = re.match(a, str)
if find:
    a = (find.group()).lower()
    a= a.replace('executeglobal','Wscript.Echo')
print(a)
