# Problem: Replace Words - https://leetcode.com/problems/replace-words/

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        new = Trie()

        for word in dictionary:
            new.insert(word)
        
        splited = sentence.split()
        result = []
        for word in splited:
            replaced = new.search(word)
            result.append(replaced)
        return " ".join(result)


class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        curr = self.root

        for char in word:
            if char not in curr.child:
                curr.child[char] = TrieNode()

            curr = curr.child[char]

        curr.end = True

    
    def search(self, word):
        curr = self.root
        formed = []

        for char in word:
            if curr.end:
                return "".join(formed)

            if char not in curr.child:
                return word

            formed.append(char)

            curr = curr.child[char]
        return ''.join(formed)
        