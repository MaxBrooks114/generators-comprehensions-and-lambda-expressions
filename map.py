import timeit
setup = """\
text = "what have the romans ever done for us"
"""

text = "what have the romans ever done for us"


def comp_cap():
    capitals = [char.upper() for char in text]
    return capitals


def map_cap():
    capitals = list(map(str.upper, text))
    return capitals


def comp_words():
    words = [word.upper() for word in text.split(" ")]
    return words


def map_words():
    words_map = list(map(str.upper, text.split(' ')))
    return words_map
#
# for x in map(str.upper, text.split(' ')):
#     print(x)


result_1 = timeit.timeit(comp_cap, setup, number=10000)
result_2 = timeit.timeit(map_cap, setup, number=10000)
result_3 = timeit.timeit(comp_words, setup, number=10000)
result_4 = timeit.timeit(map_words, setup, number=10000)

print(result_1)
print(result_2)
print(result_3)
print(result_4)