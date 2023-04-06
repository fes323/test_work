from collections.abc import Iterable

def intersection(*lists: Iterable[int]) -> list[int]:
    setLists = []
    for i in lists:
        setLists.append(set(i))
    finalSet = list(set.intersection(*[set(i) for i in setLists]))
    finalSet.sort()
    print(finalSet)
    return finalSet

test = [
     [1, 2, 3],
     [3, 4, 5],
     [3],
     [3, 8, 10, 400]
]
assert intersection(*test) == [3]

test = [
    range(-50, 50),
    range(-100, 100, 2),
    range(-1000, 1000, 8),
]
assert intersection(*test) == [-48, -40, -32, -24, -16, -8, 0, 8, 16, 24, 32, 40, 48]

test = [
    [1, 2, 3],
    [1, 2, 3],
    [],
]
assert intersection(*test) == []

test = [
    [1, 1, 1, 1, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0],
]
assert intersection(*test) == [0, 1]