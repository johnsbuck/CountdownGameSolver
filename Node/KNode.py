
class KNode(object):

    def __init__(self, key, value=None):
        self.key = key
        self.value = key if value is None else value
        self.children = []

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
