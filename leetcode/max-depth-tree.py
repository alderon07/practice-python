
from typing import Optional
from collections import deque

# DFS and BFS on a tree take O(n) time and O(n) space complexity because or the queue and 

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def printTree(root):
    if not root:
        return 
    print(root.val, end=" ")
    printTree(root.left)
    printTree(root.right)


# Space: O(n) because of the stack taken up by n function calls 
# Time: O(n) since all nodes need to be visited 
def recursive_dfs(root):
        if not root:
            return 0
        left_depth, right_depth = recursive_dfs(root.left), recursive_dfs(root.right)
        return max(left_depth, right_depth) + 1


def iterative_bfs(root):
    q = deque([root])
    level = 0
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        level += 1
    return level

def maxDepth(root: Optional[TreeNode]) -> int:
    return iterative_bfs(root)
    # return iterative_bfs(root)

binaryTree = TreeNode(4, TreeNode(2, None, None), TreeNode(7, TreeNode(6, None, None), TreeNode(9, None, None)))
print(maxDepth(binaryTree))