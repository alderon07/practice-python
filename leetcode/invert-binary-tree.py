from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if root == None:
        return     
    invertTree(root.left)
    invertTree(root.right)
    
    temp = root.left
    root.left = root.right
    root.right = temp
    
    return root

def printLeft(self):
    if not self:
        return

    print(self.val, end=" ")
    printLeft(self.left)


def printTree(self):
    if self:
        if self.left:
            print(self.left.val, end=" ")
        if self.right:
            print(self.right.val, end=" ")
        printTree(self.left)
        printTree(self.right)
    else:
        return  
# make binary tree
binaryTree = TreeNode(4)
binaryTree.left = TreeNode(7)
binaryTree.right = TreeNode(2)
binaryTree.left.left = TreeNode(8)
binaryTree.left.left.left = TreeNode(10)
binaryTree.left.left.right = TreeNode(1)
binaryTree.right.left = TreeNode(6)
binaryTree.right.right = TreeNode(5)

printLeft(binaryTree)
print()

# print old tree
print(binaryTree.val, end=" ")
printTree(binaryTree)
print()

# Print new tree
new = invertTree(binaryTree)
print(new.val, end=" ")
printTree(new)
print()

printLeft(binaryTree)
print()

