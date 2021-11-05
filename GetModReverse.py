number = int(input("Введіть число:"))
mod = int(input("Введіть модуль:"))


def GetModReverse(number, mod):
    if number % mod == 0:
        print("Оберненого елемента не існує")
    else:
        i = 0
        while (mod * i + 1) % number != 0:
            res = (mod * (i + 1) + 1) / number
            i += 1
            print(f"{i-1} - {res}")
        return res


GetModReverse(number, mod)