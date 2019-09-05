class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'{self.value}'


class LRUCache:
    """Optimized solution, add and remove are O(1)"""

    def __init__(self, size):
        self.size = size
        self.cache = dict()
        self.head = None
        self.tail = None

    def __contains__(self, key):
        return key in self.cache

    # If key already exists, need to remove node...
    def __setitem__(self, key, value):
        node = ListNode((key, value))
        self._pushHead(node)
        self.cache[key] = node
        if len(self.cache) > self.size:
            self._evict_lru()

    def _pushHead(self, node):
        if node is self.head:
            return
        node.next = self.head
        if self.head:
            self.head.prev = node
        self.head = node
        if self.tail is None:
            self.tail = self.head

    def _popTail(self):
        self._removeNode(self.tail)

    def _removeNode(self, node):
        if node is None:
            return
        if node is self.tail:
            self.tail = self.tail.prev
            return
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev

    def __getitem__(self, key):
        node = self.cache[key]
        self._removeNode(node)
        self._pushHead(node)
        return node.value

    def _evict_lru(self):
        key = self.tail.value[0]
        self.tail = self.tail.prev
        del self.cache[key]


cache = LRUCache(3)
for k, v in zip(range(3), 'abc'):
    cache[k] = v

cache[0]
cache[3] = 'd'
print(cache.cache)
