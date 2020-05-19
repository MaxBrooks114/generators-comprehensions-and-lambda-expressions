# In the section on Functions, we looked at 2 different ways to calculate the factorial
# of a number.  We used an iterative approach, and also used a recursive function.
#
# This challenge is to use the timeit module to see which performs better.
#
# The two functions appear below.
#
# Hint: change the number of iterations to 1,000 or 10,000.  The default
# of one million will take a long time to run.
import timeit
from timeit import Timer


def fact(n):
    result = 1
    if n > 1:
        for f in range(2, n + 1):
            result *= f
    return result
 
 
def factorial(n):
    # n! can also be defined as n * (n-1)!
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)


t1 = Timer(lambda: fact(10))
print(t1.timeit(number=100000))

t2 = Timer(lambda: factorial(10))
print(t2.timeit(number=100000))

#
# result_1 = timeit.timeit(fact, setup, number=10000)
# result_2 = timeit.timeit(loop_comp, setup, number=10000)
#
# print("Nested loop:\t{}".format(result_1))
# print("loop comp:\t{}".format(result_2))

