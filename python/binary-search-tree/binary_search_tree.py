class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    def list(self, node=None, vals=None):
        if node == None:
            node = self.root
            vals = []
        if node.left:
            self.list(node.left, vals)
        vals.append(node.value)
        if node.right:
            self.list(node.right, vals)
        return vals

    def add(self, value):
        if self.root == None:
            self.root = TreeNode(value)
        else:
            parent = self.root
            while (value <= parent.value and parent.left or
                   value > parent.value and parent.right):
                parent = parent.left if value <= parent.value else parent.right
            if value > parent.value:
                parent.right = TreeNode(value)
            else:
                parent.left = TreeNode(value)

    def search(self, value):
        return TreeNode(value) if value in self.list() else None