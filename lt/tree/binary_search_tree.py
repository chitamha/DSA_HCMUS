class Node():
    def __init__(self, data = None):
        self.data = data
        self.left = None
        self.right = None

class Tree():
    def __init__(self):
        self.root = None

    def insertNode(self, new_data, node = None):
        if self.root == None:
            self.root = Node(new_data)
            return
        
        if node == None:
            node = self.root

        if node.data > new_data:
            if node.left != None:
                self.insertNode(new_data, node.left)
            else:
                node.left = Node(new_data)
        else:
            if node.right != None:
                self.insertNode(new_data, node.right)
            else:
                node.right = Node(new_data)

    def findNode(self, value, node = None):
        if self.root == None:
            return "Not found"
    
        if node == None:
            node = self.root

        if node.data == value:
            return "Found this value"

        if value < node.data:
            if node.left != None:
                return self.findNode(value, node.left)
            else:
                return "Not found"
        else:
            if node.right != None:
                return self.findNode(value, node.right)
            else:
                return "Not found"
            
    def deleteNode(self, value, node = None):
        if self.root == None:
            return

        if node == None:
            node = self.root

        if value < node.data:
            self.deleteNode(value, node.left)
        elif value > node.data:
            self.deleteNode(value, node.right)
        else:
            if node.left == None and node.right == None:
                node = None
                return
            elif node.left != None and node.right != None:
                tmp = node.left
                while tmp.right != None:
                    tmp = tmp.right
                node.data = tmp.data
                self.deleteNode(tmp.data, tmp)
            else:
                if node.left == None:
                    node = node.right
                else:
                    node = node.left

    def printTree(self, node = None):
        if self.root == None:
            return
        if node == None:
            node = self.root

        if node.left != None:
            self.printTree(node.left)
        print(node.data)
        if node.right != None:
            self.printTree(node.right)

def main():
    # arr = list(map(int, input().split()))
    arr = [4, 3, 2, 5, 6, 7, 1, 9, 8, 10, 11, 12]

    binaTree = Tree()
    for i in range(len(arr)):
        binaTree.insertNode(arr[i])

    binaTree.printTree()
    print(binaTree.findNode(13))
    print(binaTree.findNode(12))
    print(binaTree.findNode(15))
    print(binaTree.findNode(0))
    print(binaTree.findNode(4))
    print(binaTree.findNode(100))

main()
