#QUESTION
# Given the root to a binary tree, implement serialize(root), which serializes the tree into a string,
# and deserialize(s), which deserializes the string back into the tree.
# For example, given the following Node class
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# The following test should pass:
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'

#SOLUTION

#Serialize: Iterate recursively through the tree, if a node is empty return a string # to determine the nodes with 0/1 edge,
#otherwise return node.val + ','
#Time complexity: O(n) -> traverse each node only once. 

#Deserialize: For each serialized node (separated by ,) rebuild the tree starting from the left.
#When it reaches a # it knows the node has no more children on the left and then repeat on the right.
#Time complexity: O(n) -> Traverse serial list only once.

#Space complexity for the entire algorithm is O(n) as building the tree takes up n space as well the serialization string.

class Node:
     def __init__(self, val, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

def main():
    node = Node('root', Node('left', Node('left.left')), Node('right'))
    assert deserialize(serialize(node)).left.left.val == 'left.left'
    node = Node('root')
    assert deserialize(serialize(node)).left is None
    assert deserialize(serialize(node)).val == 'root'

def serialize(node):

    serial = ""
    if node == None:
        serial += '#,'
        return serial

    serial += node.val + ','
    serial += serialize(node.left)
    serial += serialize(node.right)
    return serial

def deserialize(s):
    s = s[:-1]
    s = s.split(',')
    return DeserializeHelper(s)

def DeserializeHelper(s):

    if not s:
        return None

    node = None
    rootval = s.pop(0)

    if rootval != '#':
        node = Node(rootval)
        node.left = DeserializeHelper(s)
        node.right = DeserializeHelper(s)
    
    return node




if __name__ == '__main__':
    main()