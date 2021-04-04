L = [None, 1, 2, 3, -4, 0, 1.1, 2.0, "a", -2.0, 1.56, complex(), True, False]
D = {1: 2, "a": 3, -1: 1, 0: 5}

isNumber = lambda num: True if type(num) is int or type(num) is float else False
task1 = lambda: [elem for elem in L if isNumber(elem) and elem % 2 == 0]
task2 = lambda: L[::2]
task3 = lambda: [elem for elem in L if isNumber(elem) and elem > 0]
task5 = lambda: [key + value for key, value in D.items() if isNumber(key) and isNumber(value)]
task6 = lambda: [(tmp[i], tmp[j]) for tmp in (list(sorted(filter(isNumber, L))),) for i in range(0, len(tmp)-1)
                 for j in range(i+1, len(tmp)) if tmp[i] < tmp[j]]
task7 = lambda: {L[i]: L[i+1] for i in range(0, len(L)-1, 2)}


def task4(m):
    d = dict()
    for elem in filter(isNumber, L):
        remains = abs(elem) % m
        if remains in d:
            d[remains].add(elem)
        else:
            d[remains] = set([elem])
    return list(d.values())


print("Task 1: ", task1(), "\nTask 2: ", task2(), "\nTask 3: ", task3(), "\nTask 4: ", task4(3), "\nTask 5: ", task5(),
      "\nTask 6: ", task6(), "\nTask 7: ", task7())
