# for i in range(1,11):
#     for j in range(1,11):
#         print(i, i * j)

for times_tables in [(i, i * j) for j in range(1, 11) for i in range(1,11)]:

    print(times_tables)