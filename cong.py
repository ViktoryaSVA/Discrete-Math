import math

print("a*x=b(mod m)")
a = int(input("a="))
b = int(input("b="))
mod = int(input("mod ="))
i = 1

S = {2, 3, 5, 7}
k = 1
rangeForK = mod - 1


def Factor(n):
    Ans = []
    d = 2
    while d * d <= n:
        if n % d == 0:
            Ans.append(d)
            n //= d
        else:
            d += 1
    if n > 1:
        Ans.append(n)
    return Ans


dict = {}
for k in range(11):
    res = divmod(a ** k, mod)
    if len(Factor(res[1])) > 1:
        resFactor = Factor(res[1])
        # print(Factor(res[1]))
        for i in S:
            if i == resFactor[1]:
                dict[k] = resFactor
                # print(resFactor, k)

    k += 1
# print(buff)
i = 0
print(dict)
# for el in dict:
#     value = dict.get(el)
#
#     for i in value:
#         countLog = math.log(i, a)
#         sumLog = countLog
#         sumLog += sumLog
#         print(f"sumLog - {sumLog} = {el}")
#         # print(f"countLog - {countLog}, i = {i} ")
#     i += 1

