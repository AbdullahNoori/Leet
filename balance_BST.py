'''Given a binary search tree, return a balanced binary search tree with the same node values.
A binary search tree is balanced if and only if the depth of the two subtrees of every node never differ by more than 1.
If there is more than one answer, return any of them'''




# psudocode:

# create a class Solution
# creata a balanced_BST function that takes in self, root:TreeNode
# convert the tree to a sorted arrya using an in-order traversal
# construct a new balanced tree from the sorted array recurively 



def is_balanced_helper(root):
    # a None tree is balanced
    if root is None:
        return 0
    left_height = is_balanced_helper(root.left)
    # if the left subtree is not balanced, then:
    # this tree is also not balanced
    if left_height == -1:
        return -1
    # if the right subtree is not balanced, then:
    # this tree is also not balanced
    right_height = is_balanced_helper(root.right)
    if right_height == -1:
        return -1
    # if the diffrence in heights is greater than 1, then:
    # this tree is not balanced
    if abs(left_height - right_height) > 1:
        return -1
    # this tree is balanced, return its height
    return max(left_height, right_height) + 1



