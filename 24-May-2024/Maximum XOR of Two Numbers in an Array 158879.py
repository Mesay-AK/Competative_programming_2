# Problem: Maximum XOR of Two Numbers in an Array - https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

class TrieNode:
    def __init__(self):
        self.children = [None, None]

        
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root

        for char in word:
            n = int(char) 
            if not curr.children[n]:
                curr.children[n] = TrieNode()
                
            curr = curr.children[n]

class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        Tree = Trie()
        def build(nums):

            for num in nums:
                number = bin(num)[2:]
                Tree.insert(number.zfill(32))

        def finding(num):
            curr = Tree.root
            maximum = 0
            binary = bin(num)[2:].zfill(32)  

            for char in binary:
                opposite = 1 ^ int(char)  
                if curr.children[opposite]:
                    maximum = (maximum << 1) | 1
                    curr = curr.children[opposite]
                else:
                    maximum = (maximum << 1)
                    curr = curr.children[int(char)]

            return maximum

        build(nums)

        maximum = 0
        for num in nums:
            maximum = max(maximum, finding(num))

        return maximum