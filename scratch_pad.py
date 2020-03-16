from time import perf_counter

# insert to tail
myList = []
start = perf_counter()
for x in range(0, 100000):
    myList.append(x)
end = perf_counter()
print(f'time to add to tail: {end - start}')


# insert  to head
myList = []
start = perf_counter()
for x in range(0, 100000):
    myList.insert(0, x)
end = perf_counter()
print(f'time to add to head: {end - start}')
