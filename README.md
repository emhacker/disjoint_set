# Disjoint Set
A very simple yet effective library for maintaining disjoint sets.
There are three supported operations:

1. `make_set` Creates a singletone set for a given item. _O(1)_
2. `find_set` Find the set representative of a given set. _O(Log^*(N))_
3. `union` Unions two given sets into one set.

# Limitations
At the moment, the library is agnostic to the representative of a set (_e.g., the user cannot choose the set representative_).
