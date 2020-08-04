
class KNode(object):

    def __init__(self, key):
        self.key = key
        self.value = []
        self.children = {}

    def add_child(self, key):
        if key not in self.children:
            self.children[key] = KNode(key)

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
        output = '"' + str(self.key) + '"' + ": ("
        for key in self.children:
            output += str(key) + ", "
        output += ")"
        return output

    def __repr__(self):
        return self.__str__()
