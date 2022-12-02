
class OrderSet:
    def __init__(self,lit):
        self.data = lit

    def __repr__(self):
        return 'OrderSet(%r)'%self.data

    def __and__(self, other):
        result = []
        for a in self.data:
            for b in other.data:
                if a == b:
                    result.append(b)
        return OrderSet(result)

    def __or__(self, other):
        result = []
        for a in self.data:
            for b in other.data:
                if a == b:
                    result.append(b)
        list_b = [x for x in other.data]
        for a in result:
            for b in other.data:
                if a == b:
                    list_b.remove(b)
        result = self.data + list_b
        return OrderSet(result)

    def __xor__(self, other):
        result = []
        print(self.data,other.data)
        for a in self.data:
            for b in other.data:
                if a == b:
                    result.append(b)
        list_a = [x for x in self.data]
        list_b = [x for x in other.data]
        for a in result:
            for b in self.data:
                if a == b:
                    list_a.remove(b)
        for a in result:
            for b in other.data:
                if a == b:
                    list_b.remove(b)
        result = list_a + list_b
        return OrderSet(result)

    def __ne__(self, other):
        print("调用ne")
        if len(self.data) != len(other.data):
            return True
        for x in range(len(self.data)):
            if self.data[x] != other.data[x]:
                return True
        return False



s1 = OrderSet([1,2,3,4])
s2 = OrderSet([3,4,5])
print(s1 & s2) # OrderSet([3,4])
print(s1 | s2) # OrderSet([1,2,3,4,5])
print(s1 ^ s2) # OrderSet([1,2,5])
if OrderSet([1,2,3,4]) != OrderSet([1,2,3,4]):
    print("不相同")
else:
    print("相同")