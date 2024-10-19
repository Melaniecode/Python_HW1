def gen(n):
    for i in range(0, n+1):
        if i % 3 == 0 and i % 5 != 0:
            yield i


n = int(input("請輸入一個整數: "))

print(list(gen(n)))

