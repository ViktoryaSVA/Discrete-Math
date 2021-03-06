arr = []
buff = []

n1 = int(input("Введіть перше число:"))
n2 = int(input("Введіть друге число:"))

def class_algor_evklida(num1, num2):
    print('Класичний алгоритм Евкліда')
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            res = num1//num2
            a = num1
            num1 %= num2
            buff.append(f"{a} = {num2} * {res} + {num1 % num2}")
            print(f"{a} = {num2} * {res} + {num1 % num2}")

        else:
            a = num2
            res = num2//num1

            num2 %= num1
            buff.append(f"{a} = {num1} * {res} + {num2 % num1}")
            print(f"{a} = {num1} * {res} + {num2 % num1}")

    return num1 or num2
print(class_algor_evklida(n1, n2))

def bin_ev(num1, num2):
    print('Бінарний алгоритм Евкліда')
    k = 1
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    while num1 != 0 and num2 != 0:
        while num1 % 2 == 0 and num2 % 2 == 0:
            num1 = num1 / 2
            num2 = num2 / 2
            k *= 2
        while num1 % 2 == 0:
            num1 /= 2
        while num2 % 2 == 0:
            num2 /= 2
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
    return num2 * k

print(f"НСД({n1}, {n2})= {bin_ev(n1, n2)} \n")


print('Розширений алгоритм Евкліда')
def ext_ev(num1, num2):
    if num2 == 0:
        print(f"НСД({n1}, {n2})= 1")
    else:
        rest = num1 % num2
        wh = num1 // num2
        print(f"{num1}={num2}*{wh}+{rest}")
        x, xx, y, yy = 1, 0, 0, 1
        x, xx = xx, x - xx * wh
        y, yy = yy, y - yy * wh
        while rest != 0:
            num1 = num2
            num2 = rest
            wh = num1 // num2
            rest = num1 % num2
            x, xx = xx, x - xx * wh
            y, yy = yy, y - yy * wh
            print(f"{num1}={num2}*{wh}+{rest}")
        print(f"НСД({n1}, {n2})= {num2} = {n1}*({x})+{n2}*({y})")


ext_ev(n1, n2)


