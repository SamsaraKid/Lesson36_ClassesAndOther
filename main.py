stek = []
ochered = []


def add(mas, val):
    mas.append(val)
    return mas

def next(mas):
    if mas == stek:
        return stek.pop()
    elif mas == ochered:
        return ochered.pop(0)


add(stek, 10)
add(stek, 20)
print(add(stek, 30))
print(next(stek))
print(next(stek))
print(next(stek))


add(ochered, 11)
add(ochered, 22)
print(add(ochered, 33))
print(next(ochered))
print(next(ochered))
print(next(ochered))