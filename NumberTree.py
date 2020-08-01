class NumberTree(object):

    def __init__(self, *args):
        if len(args) == 1:
            self.left_tree = None
            self.right_tree = None
            self.operator = None
            self._val = args[0]
        else:
            self.left_tree = args[0]
            self.right_tree = args[1]
            self.operator = args[2]
            self._val = self.operator(self.left_tree.value, self.right_tree.value)

    @property
    def value(self):
        return self._val

    # Needs work
    # def print_tree(self, prefix=None, suffix=None):
    #     output = ""
    #
    #     if self.left is not None:
    #         if prefix is not None:
    #             output += prefix
    #         output += self.left.print_tree(prefix, suffix)
    #
    #     output += str(self.value)
    #
    #     if self.right is not None:
    #         output += self.right.print_tree(prefix, suffix)
    #         if suffix is not None:
    #             output += suffix
    #
    #     return output

    def __eq__(self, other):
        if self.value == other.value:
            return True
        return False

    def __le__(self, other):
        if self.value <= other.value:
            return True
        return False

    def __ge__(self, other):
        if self.value >= other.value:
            return True
        return False

    def __lt__(self, other):
        if self.value < other.value:
            return True
        return False

    def __gt__(self, other):
        if self.value > other.value:
            return True
        return False

    def __str__(self):
        return "(" + str(self.value) + ", " + str(self.value) + ")"

    def __repr__(self):
        return self.__str__()