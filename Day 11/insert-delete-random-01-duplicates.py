import random
from collections import defaultdict
class RandomizedCollection:

    def __init__(self):
        self.hash_map = []
        self.index = defaultdict(set)

    def insert(self, val: int) -> bool:
        self.index[val].add(len(self.hash_map))
        self.hash_map.append(val)
        return len(self.index[val]) == 1

    def remove(self, val: int) -> bool:
        if not self.index[val]:
            return False
        
        r,l = self.index[val].pop(), self.hash_map[-1]
        self.hash_map[r] = l
        self.index[l].add(r)
        self.index[l].discard(len(self.hash_map)-1)
        self.hash_map.pop()
        
        return True

    def getRandom(self) -> int:
        return random.choice(self.hash_map)