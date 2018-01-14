class Zipper(object):

    @staticmethod
    def from_tree(tree):
        new = Zipper()
        new.tree = tree
        new.offsets = []
        return new

    def value(self):
        tree = self.tree
        for offset in self.offsets:
            tree = tree[offset]
        return tree['value']

    def set_(self, key, value):
        tree = self.tree
        for offset in self.offsets:
            tree = tree[offset]
        tree[key] = value
        new = Zipper.from_tree(self.tree)
        new.offsets = self.offsets
        return new

    def set_value(self, value):
        return self.set_('value', value)

    def subtree(self):
        tree = self.tree
        for offset in self.offsets:
            tree = tree[offset]
        return tree

    def left(self):
        new = Zipper.from_tree(self.tree)
        new.offsets = self.offsets + ['left']
        if new.subtree():
            return new
        else:
            return None

    def set_left(self, value):
        return self.set_('left', value)

    def right(self):
        new = Zipper.from_tree(self.tree)
        new.offsets = self.offsets + ['right']
        if new.subtree():
            return new
        else:
            return None

    def set_right(self, value):
        return self.set_('right', value)

    def up(self):
        new = Zipper.from_tree(self.tree)
        if self.offsets:
            new.offsets = self.offsets[:-1]
        return new

    def to_tree(self):
        return self.tree