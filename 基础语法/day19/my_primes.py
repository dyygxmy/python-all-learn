# 自己做的
class Primes:
    def __init__(self, b, n):
        self.start = b
        self.step = n

    def pri(self):
        lit = []
        while True:
            if len(lit) >= self.step:
                break
            isPri = True
            for x in range(2,self.start,1):
                if self.start % x == 0:
                    isPri = False
                    break
            if isPri:
                lit.append(self.start)
            self.start += 1
        return lit


for x in Primes(10,4).pri():
    print(x)


# 老师做的
class Primes2:
    def __init__(self, b, n):
        self.start = b
        self.count = n

    @staticmethod
    def __isPrime(self, x):
        for x in range(2, self.cur_pos):
            if self.cur_pos % x == 0:
                return False
        return True

    def __iter__(self):
        self.cur_pos = self.start
        self.cur_count = self.count
        return self

    def __next__(self):
        if self.cur_count >= self.count:
            raise StopIteration

        self.cur_count += 1
        while True:
            if self.__isPrime(self.cur_pos):
                v = self.cur_pos
                self.cur_pos += 1
                return v
            self.cur_pos += 1


print("Primes2(10,4):",Primes2(10,4))
for x in Primes2(10,4):
    print(x)