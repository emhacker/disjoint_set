# Disjoint Set
A very simple yet effective library for maintaining disjoint sets.
There are three supported operations:

1. `make_set` Creates a singleton set for a given item. _O(1)_
2. `find_set` Find the set representative of a given set. _O(Log^*(N))_
3. `union` Unions two given sets into one set _O(Log^*(N))_.

# Example
Creating a list of singleton sets, each with a number as representative.
```
nodes = [make_set(i) for i in range(5))
```

Unifying sets 0 and 3, agnostic to the representative item.
```
union(sets[0], sets[3])
```

Now that set 0 and set 3 are unified, the following applies:
```
find_set(sets[0]) == find_set(sets[3])
```

One can also union two sets, while choosing the representative item,
so the following also applies.
```
union(sets[1], sets[4], lambda (x, y): (x, y) if x > y else (y, x))
4 == find_set(sets[1]).item
```

The function passed as the third parameter for `union` places the bigger item on the first position of
the returned tuple thus making sure it will be chosen as the representative item.
