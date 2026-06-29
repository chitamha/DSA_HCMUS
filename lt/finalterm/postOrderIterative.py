import sys

def postOrderIterative(root):
    if not root:
        return []
    stack = []
    result = []
    stack.append(root)
    while stack:
        node = stack.pop()
        result.append(node.val)
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)
    return result[::-1]