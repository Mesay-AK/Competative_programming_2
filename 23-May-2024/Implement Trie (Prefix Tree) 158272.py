# Problem: Implement Trie (Prefix Tree) - https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.count = 0
                
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            num = ord(char) - 97
            
            if not curr.children[num]:
                curr.children[num] = TrieNode()
            curr.count += 1  
            curr = curr.children[num]

        curr.is_end = True
                
    def search(self, word: str) -> bool:

        curr = self.root
        for char in word:
            num = ord(char) - 97  
            if not curr.children[num]:
                return False
            curr = curr.children[num]
        return curr.is_end
        

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for char in prefix:
            num = ord(char) - 97
            if not curr.children[num]:
                return False
            curr = curr.children[num]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)