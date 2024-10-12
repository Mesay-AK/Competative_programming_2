# Problem: Merge Intervals (Optional) - https://leetcode.com/problems/merge-intervals/

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
                
        intervals.sort()

        Tree = BST()
        for value in intervals:
            Tree.insert(value)

        return Tree.traverse(Tree.root, [])
        
class Node:
    def __init__(self, value):
        self.start = value[0]
        self.end = value[-1]
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None
        self.count = 0

    def insert(self, value):
        if not self.root:
            self.root = Node(value)
            self.count += 1

        else:
            return self.inserting(self.root, value)

    def inserting(self, curr, value):
        if curr.start <= value[0] <= curr.end:
            if curr.end < value[1]:
                curr.end = value[1]

        elif curr.start > value[1]:
            if not curr.left:
                curr.left = Node(value)
                self.count += 1
            else:
                return self.inserting(curr.left, value)
        elif curr.end < value[0]:
            if not curr.right:
                curr.right = Node(value)
                self.count += 1

            else:
                return self.inserting(curr.right, value)


    def traverse(self,node, result):
        if not node:
            return result

        result.append([node.start, node.end])
        if node.left:
            self.traverse(node.left, result)

        if node.right:
            self.traverse(node.right, result)

        return result

            

        
                        