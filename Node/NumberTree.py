import math
import operator as op


class NumberTree(object):

    def __init__(self, *args):
        """
            Creates a NumberTree.

            Constructor for Leaves
            -------------------
            :param args[0]: The value of the tree
            :param args[1]: The key tuple for this tree
            :type args[0]: int

            Constructor for Operation Trees
            -------------------
            :param args[0]: The left side sub-tree
            :param args[1]: The right side sub-tree
            :param args[2]: The function to apply to the values of the two sub-trees
            :type args[0]: NumberTree
            :type args[1]: NumberTree
            :type args[2]: lambda

            :return: A NumberTree
            :rtype: NumberTree

            :Example:

            >>> left_leaf = new NumberTree(7)
            >>> right_leaf = new NumberTree(4)
            >>> tree = new NumberTree(left_leaf, right_leaf, lambda x,y: x+y)
            """
        self._env = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv}

        if len(args) == 2:
            self.left_tree = None
            self.right_tree = None
            self.operator = None
            self._val = args[0]
            self._key = args[1]
        elif len(args) == 3:
            self.left_tree = args[0]
            self.right_tree = args[1]
            self.operator = args[2]
            self._get_value()
            key_list = list(args[0].key) + list(args[1].key)
            key_list.sort()
            self._key = tuple(key_list)

    @property
    def value(self):
        return self._val

    @property
    def key(self):
        return self._key

    def _get_value(self):
        if self.operator in self._env:
            self._val = self._env[self.operator](self.left_tree.value, self.right_tree.value)

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
        if self.left_tree is None:
            if self.right_tree is None:
                return str(self.value)
            return "(" + str(self.value) + " " + self.operator + " " + str(self.right_tree) + ")"
        if self.right_tree is None:
            return "(" + str(self.left_tree) + " " + self.operator + " " + str(self.value) + ")"

        return "(" + str(self.left_tree) + " " + self.operator + " " + str(self.right_tree) + ")"

    def __repr__(self):
        return self.__str__()
