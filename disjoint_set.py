# A simple (yet effective) way to maintain disjoint sets.
# S1 and S2 are disjoints, if no element 'e' exists that is both in S1 and in S2.
class Set:
    def __init__(self, itm):
        self.item = itm
        self.parent = self
        self.rank = 1


# Create a set from the given item.
def make_set(itm):
    return Set(itm)


# Find the representative set to which the set 's' belongs to.
def find_set(s):
    if s.parent != s:
        s.parent = find_set(s.parent)
    return s.parent


# Unions the given two sets.
def union(x, y, choose=None):
    def _link(s1, s2):
        if s1.rank > s2.rank:
            s2.parent = s1
            if choose:
                (s1.item, s2.item) = choose(s1.item, s2.item)
        else:
            s1.parent = s2
            if s1.rank == s2.rank:
                s2.rank += 1
            if choose:
                (s2.item , s1.item) = choose(s2.item, s1.item)
    _link(find_set(x), find_set(y))


# Testing util.
def expect_true(s, tf):
    print('Testing {0}...'.format(s))
    if tf():
        print('Passed')
    else:
        print('Failed')

if __name__ == '__main__':
    # Representative agnostic test.
    sets = [make_set(i) for i in range(5)]
    union(sets[0], sets[2])
    expect_true("set 0 <-> 2", lambda: find_set(sets[0]) == find_set(sets[2])) 
    union(sets[1], sets[3])
    expect_true("set 1 <-> 3", lambda: find_set(sets[1]) == find_set(sets[3])) 
    expect_true("set 0 <> 3", lambda: find_set(sets[0]) != find_set(sets[3])) 
    union(sets[1], sets[2])
    expect_true("set 1 <-> 2", lambda: find_set(sets[1]) == find_set(sets[2])) 
    expect_true("set 0 <-> 3", lambda: find_set(sets[1]) == find_set(sets[2])) 
    expect_true("set 0 <> 4", lambda: find_set(sets[0]) != find_set(sets[4])) 

    # Representative importance testing.
    smaller = lambda x, y: (x, y) if x < y else (y, x)
    sets = [make_set(i) for i in range(5)]
    # Set (0, 2)
    union(sets[0], sets[2], smaller)
    expect_true("set 0 <-> 2", lambda: find_set(sets[0]) == find_set(sets[2]))
    expect_true("rep 0 is 0", lambda: find_set(sets[0]).item == 0) 
    # Set (3, 1)
    union(sets[3], sets[1], smaller)
    expect_true("set 3 <-> 1", lambda: find_set(sets[3]) == find_set(sets[1]))
    expect_true("rep of 3 is 1", lambda: find_set(sets[3]).item == 1)
    # Set (3, 0)
    union(sets[3], sets[0], smaller)
    expect_true("set 3 <-> 0", lambda: find_set(sets[3]) == find_set(sets[0]))
    expect_true("rep of 3 is 0", lambda: find_set(sets[3]).item == 0)
