
m = int(input("Введіть кількість простих чисел:"))
arr = [2, 3,4, 5, 6, 7] # факторна база
k = 0
s_tst = 0

for i in arr:
    if k > 0 and k < i-1:
        if i % k != 0:
            s_tst += 1
    if s_tst != 1:
        print(f"{i}-gladke")
    k += 1
    # print(k)
