import re
str = 'ExEcuTe'
a = re.compile("(/^(E|e)[\\w]{1,12}[\\S][\\w]{1,}", re.I)
find = p.findall("execute")
replace(find, "write")