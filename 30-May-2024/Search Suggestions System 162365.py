# Problem: Search Suggestions System - https://leetcode.com/problems/search-suggestions-system/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.word = ''
        
                
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        
        for char in word:
            
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.is_end = True
        curr.word = word
                
    def search(self, word: str) -> bool:

        now = self.root
        for char in word:
            if char in now.children:
                now = now.children[char]
            else:
                return []
            
        res = []

        def backtrack(node):

            if len(res) == 3:
                return

            if node.is_end:
                res.append(node.word)

            for i in node.children:
                backtrack(node.children[i])

        backtrack(now)
        return res
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        
        trie = Trie()

        products.sort()

        for word in products:
            trie.insert(word)

        answer = []
        for i in range(len(searchWord)):
            answer.append(trie.search(searchWord[:i+1]))

        return answer


        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)