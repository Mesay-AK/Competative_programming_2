# Problem: Longest Common Prefix - https://leetcode.com/problems/longest-common-prefix/

from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')  

            if idx not in curr.children:
                curr.children[idx] = TrieNode()

            curr = curr.children[idx]

        curr.end = True

    def searchPrefix(self) -> str:
        curr = self.root
        prefix = ""
        
        while curr and len(curr.children) == 1 and not curr.end:
            next_char_idx, next_node = list(curr.children.items())[0]
            
            prefix += chr(next_char_idx + ord('a'))
            curr = next_node
            
        return prefix

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        trie = Trie()

        for word in strs:
            if word == '':
                return ''
            trie.insert(word)

        return trie.searchPrefix()

