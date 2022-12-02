# 此示例示意enumerate的用法

names = ["中国移动","中国电信","中国联通"]
for k,n in enumerate(names):
    print("序号 :",k,"-->",n)
print("-----------------------------------------")
it = iter(enumerate(names))
while True:
    try:
        k,n = next(it)
        print("序号 :", k, "-->", n)
    except StopIteration:
        break