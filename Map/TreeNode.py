class TreeNode(object):

    def __init__(self, key):
        self.key = key
        self.forest = []
        self.node_forest = []
        self.forest_iter_index = 0
        self.node_iter_index = 0

    def add_tree(self, tree):
        self.forest.add(tree)

    def init_iterator(self, start_index=0):
        self.node_iter_index = start_index

    def next_tree(self):
        if self.forest_iter_index < len(self.forest):
            self.forest_iter_index += 1
            return self.forest[self.forest_iter_index - 1]
        elif self.node_iter_index < len(self.node_forest):
            next_node = self.node_forest[self.node_iter_index]
            next_node.init_iterator(self.node_iter_index)
            tree = next_node.next_tree()
            if tree is None:
                self.node_iter_index += 1
                return self.next_tree()
            else:
                return tree
        else:
            return None

    def reset_iterator(self):
        self.forest_iter_index = 0
        self.node_iter_index = 0

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return self.__str__()
