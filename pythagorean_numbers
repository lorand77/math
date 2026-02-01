import math
import time

# pythagorean_numbers = []
# for a in range(1, 100):
#     for b in range(1, 100):
#         for c in range(1, 100):
#             if a**2+b**2 == c**2:
#                 if a < b:
#                     pythagorean_numbers.append([a, b, c])

# print(pythagorean_numbers)
# print(len(pythagorean_numbers))


# N = 1000
# pythagorean_numbers = []
# for a in range(1, N):
#     for b in range(a + 1, N):
#         c = math.sqrt(a**2+b**2)
#         if c == int(c) and c < N:
#             pythagorean_numbers.append([a, b, int(c)])

# print(pythagorean_numbers)
# print(len(pythagorean_numbers))


# N = 1000
# pythagorean_numbers = []
# start_time = time.time()
# for a in range(1, N):
#     for b in range(a + 1, N):
#         c = math.sqrt(a**2+b**2)
#         if c == int(c) and c < N and math.gcd(a, b, int(c)) == 1:
#             pythagorean_numbers.append([a, b, int(c)])
# elapsed_time = time.time() - start_time

# print(pythagorean_numbers)
# print(len(pythagorean_numbers))
# print(f"Method 1 time: {elapsed_time:.4f} seconds")


N = 1000000
pythagorean_numbers = []
start_time = time.time()
for m in range(1, int(math.sqrt(N)) + 1):
    for n in range(1, m):
        if ((n % 2 == 0 and m % 2 == 1) or (n % 2 == 1 and m % 2 == 0)) and math.gcd(n, m) == 1:
            a = m**2 - n**2
            b = 2*m*n
            c = m**2 + n**2
            if c < N:
                pythagorean_numbers.append(sorted([a, b, c]))
elapsed_time2 = time.time() - start_time

# print(sorted(pythagorean_numbers))
print(len(pythagorean_numbers))
print(len(pythagorean_numbers) / N)
print(1 / (2 * math.pi))

# print(f"Method 1 time: {elapsed_time:.4f} seconds")
print(f"Method 2 time: {elapsed_time2:.4f} seconds")
