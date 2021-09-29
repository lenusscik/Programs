def fibo(n):
    if n == 0:
        num = 0
    elif n == 1:
        num = 1
    else:
        num = fibo(n - 1) + fibo(n - 2)
    return num
# fibo(0) = 0
# fibo(1) = 1
n = input('¬ведите число: ')
for i in range(n - 1):
    print(fibo(i))


