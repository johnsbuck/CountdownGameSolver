class TreeNode(object):

    def __init__(self, key):
        self.key = key
        self.forest = []
        self.node_forest = []
        self.super_list = []
        self.iter_index = 0

    def get_trees(self):
        pass

    def init_iterator(self):
        self.super_list = self.forest + self.node_forest

    def next_tree(self):
        if self.iter_index < len(self.super_list):
            self.iter_index += 1
            if isinstance(self.super_list[self.iter_index - 1], TreeNode):
                return self.super_list[self.iter_index - 1].next_tree()
            else:
                return self.super_list[self.iter_index - 1]
        else:
            return None

    def reset_iterator(self):
        self.iter_index = 0
