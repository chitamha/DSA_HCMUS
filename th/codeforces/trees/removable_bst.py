import sys

write = sys.stdout.write

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)
    
    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        elif node.value < value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    def search(self, value):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursive(node.left, value)
        else:
            return self._search_recursive(node.right, value)
    
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result
    
    def _inorder_recursive(self, node, result):
        if node is not None:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node is not None:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node is not None:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    def delete_node(self, value):
        self.root = self._delete_node_recursive(self.root, value)

    def _delete_node_recursive(self, node, value):
        if node is None:
            return None
        
        if value < node.value:
            node.left = self._delete_node_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_node_recursive(node.right, value)
        else:
            # Trường hợp không có con
            if node.left is None and node.right is None:
                return None
            
            # Trường hợp chỉ có con phải
            if node.left is None:
                return node.right
            
            # Trường hợp chỉ có con trái
            if node.right is None:
                return node.left
            
            # Trường hợp có 2 con: tìm successor (node nhỏ nhất ở cây con phải)
            cur_node = node.right
            while cur_node.left is not None:
                cur_node = cur_node.left
            
            # Sao chép giá trị successor vào node hiện tại
            node.value = cur_node.value
            
            # Xóa successor khỏi cây con phải
            node.right = self._delete_node_recursive(node.right, cur_node.value)
        
        return node

def main():
    data = sys.stdin.read().splitlines()
    Tree = BST()
    for line in data:
        command = line.split()
        if command[0] == '1':
            Tree.insert(int(command[1]))
        elif command[0] == '2':
            traversal = []
            if command[1] == "NLR":
                traversal = Tree.preorder_traversal()
            elif command[1] == "LNR":
                traversal = Tree.inorder_traversal()
            elif command[1] == "LRN":
                traversal = Tree.postorder_traversal()
            write(' '.join(map(str, traversal)) + '\n')
        elif command[0] == '3':
            write('YES\n' if Tree.search(int(command[1])) else 'NO\n')
        elif command[0] == '4':
            Tree.delete_node(int(command[1]))

if __name__ == "__main__":
    main()