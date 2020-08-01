class TreeNode(object):

    def __init__(self, key):
        self.key = key
        self.forest = []
        self.node_forest = []
        self.super_list = []
        self.iter_index = 0

    def add_tree(self, tree):
        self.forest.add(tree)

    def init_iterator(self):
        for node in self.node_forest:
            node.init_iterator()
        self.super_list = self.forest + self.node_forest

    def next_tree(self):
        if self.iter_index < len(self.super_list):
            if isinstance(self.super_list[self.iter_index], TreeNode):
                tree = self.super_list[self.iter_index].next_tree()
                if tree == None:
                    self.iter_index += 1
                    return self.next_tree()
                else:
                    return tree
            else:
                self.iter_index += 1
                return self.super_list[self.iter_index - 1]
        else:
            return None

    def reset_iterator(self):
        self.iter_index = 0

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return self.__str__()
