numbers = [10086,10000,10010,95588]
name = ["中国移动","中国电信","中国联通"]
for t in zip(range(1,100000),numbers,name):
    print(t)