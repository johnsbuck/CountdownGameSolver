
class BTNode(object):

    def __init__(self, key=None, value=None):
        self.key = key
        self.value = key if value is None else value
        self.left = None
        self.right = None

    def print_tree(self, prefix=None, suffix=None):
        output = ""

        if self.left is not None:
            if prefix is not None:
                output += prefix
            output += self.left.print_tree(prefix, suffix)

        output += str(self.value)

        if self.right is not None:
            output += self.right.print_tree(prefix, suffix)
            if suffix is not None:
                output += suffix

        return output

    def __eq__(self, other):
        if other.key == self.key:
            return True
        return False

    def __le__(self, other):
        if self.key <= other.key:
            return True
        return False

    def __ge__(self, other):
        if self.key >= other.key:
            return True
        return False

    def __lt__(self, other):
        if self.key < other.key:
            return True
        return False

    def __gt__(self, other):
        if self.key > other.key:
            return True
        return False

    def __str__(self):
        return "(" + str(self.key) + ", " + str(self.value) + ")"

    def __repr__(self):
        return self.__str__()
