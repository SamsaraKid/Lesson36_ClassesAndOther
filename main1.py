class Stek:
    def __init__(self):
        self.steklist = []

    def add(self, val):
        self.steklist.append(val)
        return self.steklist

    def next(self):
        return self.steklist.pop()


class Ochered:
    def __init__(self):
        self.ocheredlist = []

    def add(self, val):
        self.ocheredlist.append(val)
        return self.ocheredlist

    def next(self):
        return self.ocheredlist.pop(0)


stek1 = Stek()
stek1.add('5r')
stek1.add('10r')
print(stek1.add('2r'))

stek2 = Stek()
stek2.add('50r')
stek2.add('1r')
print(stek2.add('21r'))

print(stek1.next())
print(stek1.next())
print(stek1.next())

ochered1 = Ochered()
ochered1.add('5e')
ochered1.add('10e')
print(ochered1.add('2e'))

print(ochered1.next())
print(ochered1.next())
print(ochered1.next())

print('###############################')
class Sumstek(Stek):
    def __init__(self):
        super().__init__()
        # Stek.__init__(self)
        self.sum = 0

    def checksum(self):
        for m in self.steklist:
            num = int(m[:-1])
            self.sum += num
        return self.sum




stek3 = Sumstek()
stek3.add('10r')
stek3.add('5r')
print(stek3.add('2r'))
print(stek3.checksum())

print('###############################')
class Stringstek(Stek):
    def __init__(self):
        super().__init__()
        self.sumsim = 0

    def checksumsim(self):
        for s in self.steklist:
            num = len(s)
            self.sumsim += num
        return self.sumsim


stek4 = Stringstek()
stek4.add('qwerty')
stek4.add('asdfgh')
print(stek4.add('zxcvbn'))
print(stek4.checksumsim())