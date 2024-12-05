import matplotlib.pyplot as plt

def series_3x_plus_1(x):
    s = [x]
    while x > 1:
        if x % 2 == 1:
            x = 3 * x + 1
        else:
            x = x // 2
        s.append(x)
    return s

# N = 27
# for i in range(N):
#     print(series_3x_plus_1(i + 1))

x = 27
print(series_3x_plus_1(x))
plt.plot(series_3x_plus_1(x))
# plt.yscale("log")
plt.show()
