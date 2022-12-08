import re

'''
"."      Matches any character except a newline.
"^"      Matches the start of the string.
"$"      Matches the end of the string or just before the newline at
         the end of the string.
"*"      Matches 0 or more (greedy) repetitions of the preceding RE.
         Greedy means that it will match as many repetitions as possible.
"+"      Matches 1 or more (greedy) repetitions of the preceding RE.
"?"      Matches 0 or 1 (greedy) of the preceding RE.
*?,+?,?? Non-greedy versions of the previous three special characters.
{m,n}    Matches from m to n repetitions of the preceding RE.
{m,n}?   Non-greedy version of the above.
"\\"     Either escapes special characters or signals a special sequence.
[]       Indicates a set of characters.
         A "^" as the first character indicates a complementing set.
"|"      A|B, creates an RE that will match either A or B.
(...)    Matches the RE inside the parentheses.
         The contents can be retrieved or matched later in the string.
(?aiLmsux) The letters set the corresponding flags defined below.
(?:...)  Non-grouping version of regular parentheses.
(?P<name>...) The substring matched by the group is accessible by name.
(?P=name)     Matches the text matched earlier by the group named name.
(?#...)  A comment; ignored.
(?=...)  Matches if ... matches next, but doesn't consume the string.
(?!...)  Matches if ... doesn't match next.
(?<=...) Matches if preceded by ... (must be fixed length).
(?<!...) Matches if not preceded by ... (must be fixed length).
(?(id/name)yes|no) Matches yes pattern if the group with id/name matched,
                   the (optional) no pattern otherwise.

'''

# flags 参数
# 作用 : 辅助正则表达式，丰富匹配结果
'''
A  ASCII       For string patterns, make \w, \W, \b, \B, \d, \D
               match the corresponding ASCII character categories
               (rather than the whole Unicode categories, which is the
               default).
               For bytes patterns, this flag is the only available
               behaviour and needn't be specified.
I  IGNORECASE  Perform case-insensitive matching.
L  LOCALE      Make \w, \W, \b, \B, dependent on the current locale.
M  MULTILINE   "^" matches the beginning of lines (after a newline)
               as well as the string.
               "$" matches the end of lines (before a newline) as well
               as the end of the string.
S  DOTALL      "." matches any character at all, including the newline.
X  VERBOSE     Ignore whitespace and comments for nicer looking RE's.
U  UNICODE     For compatibility only. Ignored for string patterns (it
               is the default), and forbidden for bytes patterns.
'''
s = "Hello World"
s2 = '''hello world
nihao beijing'''
# re.compile()
# l = re.findall('L\\w+',s) # 匹配不到
# re.I 忽略大小写
# l = re.findall('L\w+',s,re.I) # ['llo', 'ld']
# re.M 可以匹配换行符前后的头尾也就是每行都可以匹配，而不仅仅是整个字符串
# l = re.findall('^ni',s2,re.M) # ['ni']
# l = re.findall('world$',s2,re.M) # ['world']
# re.S 对元字符.起作用，让其可以匹配换行
# l = re.findall('.*',s2) # ['hello world', '', 'nihao beijing', '']
# l = re.findall('.*',s2,re.S) # ['hello world\nnihao beijing', '']
# l = re.findall('.+',s2,re.S) # ['hello world\nnihao beijing']
# re.X 为正则添加注释 (实际几乎没人用)
pattern = '''(?P<dog>hello) # dog组
\s # 空字符
(world) # 第2组用来匹配world
'''
l = re.findall(pattern,s2,re.X) # [('hello', 'world')]
l = re.findall(pattern,s2,re.X | re.I) # 多个flags同时使用
# re.search()
# re.match()
# re.finditer()
# re.fullmatch()
# re.sub()
# re.subn()
# re.split()
print(l)

'''
# 读取一个文件的内容，将文件中所有以大写字母开头的单词匹配出来
f = open("regex",encoding="utf8")
l = []
pattern = r'[A-Z]\w*' # 筛选所有大小字母开头的单词
pattern = r'[A-Z][_.\-0-9a-zA-Z]*' # 升级版 带点、杠、数字、下划线这类

for line in f:
    l += re.findall(pattern,line)

print(l)
'''
