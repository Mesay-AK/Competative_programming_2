# Problem: Insert Delete GetRandom O(1) - https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet:
    import random
    def __init__(self):
        self.myset={}
        self.mylist=[]
        
    def insert(self, val: int) -> bool:
        if val in self.myset:
            return False
        self.myset[val]=len(self.mylist)
        self.mylist.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.myset:
            return False
        idx=self.myset[val]
        last=self.mylist[-1]
        self.mylist[idx]= last
        self.mylist.pop()
        self.myset[last]=idx
        del(self.myset[val])  
        return True
                                                                                            
    def getRandom(self) -> int:
        return random.choice(self.mylist)
        
    
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()