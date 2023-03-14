def ebob (a,b):
    for i in range(a,0,-1):
        for y in range(b,0,-1):
            if a % i == 0 and b % y == 0 and i == y:
                return i
def ekok (a,b):
    return a * b // ebob(a,b)

while True:
    a=int(input("Sayı 1: "))
    b=int(input("Sayı2: "))
    print(ekok(a,b))


