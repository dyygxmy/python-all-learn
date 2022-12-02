import re

f = open("regex",encoding="utf8")
l = []
pattern = r'[A-Z]\w*' # 筛选所有大小字母开头的单词

for line in f:
    l += re.findall(pattern,line)

print(l)