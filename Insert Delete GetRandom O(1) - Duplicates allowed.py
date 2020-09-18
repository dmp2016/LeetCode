import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        self.data_ind = dict()
        self.count = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        if not val in self.data:
            self.data[val] = set([self.count])
            res = True
        else:
            self.data[val].add(self.count)
            res = False
        self.data_ind[self.count] = val
        self.count += 1
        return res


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val in self.data:
            self.count -= 1
            ind = self.data[val].pop()
            if ind != self.count:
                val_t = self.data_ind[self.count]
                self.data[val_t].remove(self.count)
                self.data[val_t].add(ind)
                self.data_ind[ind] = val_t
            del self.data_ind[self.count]
            if len(self.data[val]) == 0:
                del self.data[val]
            return True
        else:
            return False

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return self.data_ind[random.randint(0, self.count - 1)]

test = RandomizedCollection()
test.insert(1)
test.insert(1)
test.insert(2)
test.remove(1)
test.remove(1)
print(test.data)