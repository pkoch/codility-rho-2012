import heapq

def powers_to(n, target):
    i = 0

    while target >= n:
        i += 1
        n *= 2

    return i

class Node(object):
    def __init__(self, target, payload):
        self.payload = tuple(sorted(payload))
        self.target = target
        self.highest = payload[-1]
        self.length = len(payload)
        self.cost = self.length + min(
          ([
            (target - self.highest)/i
            for i in payload
            if i + self.highest <= target
          ] or [0]) + [powers_to(self.highest, target)]
        )

    def generate_children(self):
        if self.highest == 1:
            return [self.__class__(self.target, (1,2,))]

        result = []
        increments = set(
            i + j
            for i in self.payload
            for j in self.payload
            if i + j not in self.payload and
              i + j <= self.target
        )

        for i in increments:
                result.append(self.__class__(self.target, self.payload + (i,) ))

        return result

    # heap wants __lt__ for comparisons.
    def __lt__(self, o):
        return self.cost < o.cost

    def __eq__(self, o):
        return self.target == o.target and self.payload == o.payload

    def __hash__(self):
        return hash(self.payload)

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

    discarded_solutions = set()

    while len(heap) > 0:
        next_ = heapq.heappop(heap)
        discarded_solutions.add(next_.payload)

        if next_.highest == n:
            return next_.payload

        for c in next_.generate_children():
            if c.payload in discarded_solutions:
                continue
            heapq.heappush(heap, c)

def hack(aa):
  d, i = aa
  d[i] = len(hit_the_number(i))

if __name__ == '__main__':
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
