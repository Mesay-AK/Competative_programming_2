# Problem: Design Add and Search Words Data Structure - https://leetcode.com/problems/design-add-and-search-words-data-structure/

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

    def search(self, word: str, idx: int, root: TrieNode) -> bool:
        curr = root
        for i in range(idx, len(word)):
            char = word[i]

            if char == '.':
                for child in curr.children:

                    if child and self.search(word, i + 1, child):
                        return True

                return False
            else:
                num = ord(char) - 97

                if not curr.children[num]:
                    return False
                    
                curr = curr.children[num]
        return curr.is_end

class WordDictionary:

    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        self.root.insert(word)

    def search(self, word: str) -> bool:
        return self.root.search(word, 0, self.root.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
