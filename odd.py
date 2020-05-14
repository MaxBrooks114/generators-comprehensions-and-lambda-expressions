def odds():
    start = 1
    while True:
        yield start
        start += 2


def pi():
    odd = odds()
    approx = 0
    while True:
        approx += (4 / next(odd))
        yield approx
        approx -= (4 / next(odd))
        yield approx

approx_pi = pi()

for x in range(10000000):
    print(next(approx_pi))