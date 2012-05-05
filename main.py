import heapq

def powers_to(n, target):
    i = 0

    while target >= n:
        i += 1
        n *= 2

    return i

class Node(object):
    def __init__(self, target, payload):
        self.payload = payload
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

