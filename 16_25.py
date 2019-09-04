class LRUCache:
    """Naive solution, __setitem__ is O(size)"""

    def __init__(self, size):
        self.size = size
        self.cache = dict()
        self.time = 0

    def __contains__(self, key):
        return key in self.cache

    def __setitem__(self, key, value):
        self.cache[key] = (value, self.time)
        self.time += 1
        if len(self.cache) > self.size:
            self.evict_lru()

    def __getitem__(self, key):
        value, _old_time = self.cache[key]
        self.cache[key] = (value, self.time)
        self.time += 1
        return value

    def evict_lru(self):
        lru = min(self.cache.items(), key=lambda i: i[1][1])
        del self.cache[lru[0]]


cache = LRUCache(3)
for k, v in zip(range(3), 'abc'):
    cache[k] = v

cache[0]
cache[3] = 'd'

print(cache.cache)
