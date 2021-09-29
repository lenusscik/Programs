import itertools as it
def exp_sum(n):
    num = []
    res = []
    for i in range(1, n):
        num.append(i)
    for x in range(n):
        for combo in it.combinations_with_replacement(num, x + 1):
            if sum(combo) == n:
                res.append(combo)
 
    return len(res)+1

print(exp_sum(15))

