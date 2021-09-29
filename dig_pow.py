def dig_pow(n, p):
    am = 0
    num = str(n)
    st = ''
    for i in range(0, len(num)):
        am = am + int(num[i])**(p + i)
    if am % n == 0:
        return am / n
    else:
        return -1
print(dig_pow(695, 2))