#QUESTION:
# A unival tree (which stands for "universal value") is a tree where all nodes under it have the same value.
# Given the root to a binary tree, count the number of unival subtrees.
# For example, the following tree has 5 unival subtrees:
#    0
#   / \
#  1   0
#     / \
#    1   0
#   / \
#  1   1

#SOLUTION:
#3 cases where a tree is a universal tree:
    #Where a node is a leaf node
    #Where both left and right node val = root val    
    #Where a node has one branch and the val is = root.val

#Recurse through each node going from bottom up and evaluate those 3 conditions.

#Time Complexity: O(N) -> Going through each node only once.
#Space Complexity: O(1)

class Node:
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def unival(node):

    uni = 0
    if node is None:
        return 0

    if node.left is None and node.right is None:
        return 1

    uni += unival(node.left)
    uni += unival(node.right)

    if node.left is not None and node.right is not None:        
        if node.left.val == node.val and node.right.val == node.val:
            uni += 1

    if node.left is None or node.right is None:
        if node.left is None:
            if node.right.val == node.val:
                uni += 1
        else:
            if node.left.val == node.val:
                uni += 1        
    
    return uni 

def main():
    assert unival(Node(1, Node(0, Node(0)), Node(1))) == 3
    assert unival(Node(1)) == 1

if __name__ == '__main__':
    main()
