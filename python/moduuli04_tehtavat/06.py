import random

N = int(input("Anna N määrä\n"))
i = 0
n = 0
while i < N:
    i += 1
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        n += 1

print(f"Piin arvo {N} arviolla on {(4 * n) / N}")
