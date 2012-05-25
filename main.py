#!/usr/bin/env python
import heapq

def powers_to(n, target):
    i = 0

    while target > n:
        i += 1
        n *= 2

    return i

class Node(object):
    def __init__(self, target, payload):
        self.payload = payload
        self.target = target
        self.highest = payload[-1]
        self.length = len(payload)
        self.estimation = powers_to(self.highest, target)
        if self.highest == target:
            self.estimation = 0
        self.cost = self.length + self.estimation

    def generate_children(self):
        if self.highest == 1:
            return [self.__class__(self.target, (1,2,))]

        if self.estimation < 2:
            remains = self.target - self.highest
            if remains not in self.payload:
                return []
            return [self.__class__(self.target, self.payload + (self.highest + remains,))]

        return [
            self.__class__(self.target, self.payload + (self.highest + i,) )
            for i in self.payload
            if self.highest + i <= self.target
        ]

    # heap wants __lt__ for comparisons.
    def __lt__(self, o):
        return self.cost < o.cost

    def __eq__(self, o):
        return self.target == o.target and self.payload == o.payload

    def __repr__(self):
        return "Node(%s, %s)#%s+%s"%(
            self.target,
            repr(self.payload),
            self.length,
            self.cost-self.length,
        )

def hit_the_number(n):
    if n < 1:
        raise ValueError('n must be a positive integer')

    heap = [Node(n, (1,))]

    while len(heap) > 0:
        next_ = heapq.heappop(heap)

        if next_.highest == n:
            return next_.payload

        for c in next_.generate_children():
            heapq.heappush(heap, c)

def hack(aa):
  d, i = aa
  d[i] = len(hit_the_number(i))

if __name__ == '__main__':
    from sys import argv, exit
    if len(argv) > 1:
        for i in argv[1:]:
            try:
                i = int(i)
            except:
                print "%s doesn0t seem like an int."%(i,)
            print hit_the_number(i)
        exit()
    from multiprocessing import Pool, Manager
    manager = Manager()
    pool = Pool(processes=4)

    d = manager.dict()

    try:
        from itertools import izip_longest
        pool.map_async(
            hack,
            izip_longest([], xrange(1,601), fillvalue=d),
        )
    finally:
        pool.close()
        pool.join()

    from pprint import pprint
    pprint(dict(d))
