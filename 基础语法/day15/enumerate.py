# 此示例示意enumerate的用法

names = ["中国移动","中国电信","中国联通"]
for t in enumerate(names):
    print(t)    # (0, '中国移动')
                # (1, '中国电信')
                # (2, '中国联通')