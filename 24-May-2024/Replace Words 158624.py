# Problem: Replace Words - https://leetcode.com/problems/replace-words/

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
        prefix = []
        for char in word:
            num = ord(char) - 97 
            if curr != self.root and curr.is_end:
                return ''.join(prefix) 
            else:
                prefix.append(char)
            if not curr.children[num]:
                return ''
            curr = curr.children[num]
        return ''.join(prefix) if curr.is_end else ''
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        
        words = sentence.split(' ')
        tree = Trie()

        # building the trie
        for word in dictionary:
            tree.insert(word)

        result = []
        # searching for prefix
        for word in words:
            curr = tree.search(word)

            if curr:
                result.append(curr)
            else:
                result.append(word)

        print(result)
        
        return ' '.join(result)





























