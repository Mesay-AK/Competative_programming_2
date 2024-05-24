# Problem: Longest Word in Dictionary - https://leetcode.com/problems/longest-word-in-dictionary/

class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
                
class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        count = 0
        for char in word:
            num = ord(char) - 97
            
            if not curr.children[num]:
                curr.children[num] = TrieNode()
            if curr.is_end:
                count += 1  
            curr = curr.children[num]

        curr.is_end = True
        count += 1
        return count == len(word)
   

class Solution:
    def longestWord(self, words: List[str]) -> str:

        tree = Trie()

        words.sort()
        longs = []
        for word in words:
            now = tree.insert(word)
            if now:
                if not longs:
                    longs.append(word)
                elif len(word) > len(longs[0]):
                    longs = []
                    longs.append(word)
                elif len(word) == len(longs[0]):
                    longs.append(word)

        longs.sort()

        return longs[0] if longs else ''