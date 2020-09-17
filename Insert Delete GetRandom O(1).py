import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = dict()
        self.data_ind = dict()
        self.count = 0
        

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if self.data.get(val) is None:
            self.data[val] = self.count
            self.data_ind[self.count] = val
            self.count += 1
            return True
        else:
            return False
        

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if self.data.get(val) is not None:
            ind_del = self.data[val]
            self.count -= 1
            if ind_del == self.count:
                self.data.pop(val)
                self.data_ind.pop(ind_del)
            else:
                val_last = self.data_ind[self.count]
                self.data[val_last] = ind_del
                self.data_ind[ind_del] = val_last
                self.data.pop(val)
                self.data_ind.pop(self.count)
            return True
        else:
            return False



    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.data_ind[random.randint(0, self.count - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


test = RandomizedSet()
print(test.insert(1))
print(test.remove(2))
print(test.insert(2))
print(test.getRandom())
print(test.remove(1))
print(test.insert(2))
print(test.getRandom())
