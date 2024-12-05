N = 27

def series_3x_plus_1(x):
    s = [x]
    while x > 1:
        if x % 2 == 1:
            x = 3 * x + 1
        else:
            x = x // 2
        s.append(x)
    return s

for i in range(N):
    print(series_3x_plus_1(i + 1))
