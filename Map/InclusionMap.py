
class TreeNode(object):

    def __init__(self, key):
        self.key = key
        self.forest = []
        self.node_forest = []
        self.forest_iter_index = 0
        self.node_iter_index = 0

    def add_tree(self, tree):
        self.forest.append(tree)

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
        for node in self.node_forest:
            node.reset_iterator()

    def __str__(self):
        return str(self.key)

    def __repr__(self):
        return self.__str__()


class InclusionMap(object):
    """The mapping used to organize and initialize TreeNodes in relation
    to each other.

    Args:
        size (int): The size of the number list used in the Numbers Round.

    """

    def __init__(self, size=6):
        # The main dict map used to store each TreeNode
        self._map = {(): TreeNode(())}

        # Add size of number listing
        self._size = size

        # Initializing the map values and TreeNodes
        self._generate_map(list(range(self._size)))
        self._generate_refs()

    def add(self, new_tree):
        key = tuple(set(list(range(self._size))) - set(new_tree.key))
        if key != ():
            self._map[key].add_tree(new_tree)

    def get_trees(self, key=()):
        tree_list = []
        node = self._map[key]
        node.reset_iterator()
        next_tree = node.next_tree()
        while next_tree is not None:
            tree_list.append(next_tree)
            next_tree = node.next_tree()
        return tree_list

    def _generate_map(self, numbers, s=(), idx=0):
        """Generates the main map used to explore the set of NumberTrees.

        Args:
            numbers (list[int]): The set of numbers that can be used.
            s (tuple): The string that is used as the key for the dictionary
            idx (int): The starting index for reading in numbers

        """
        # If the index is the at the end of the list, exit function
        if idx == len(numbers):
            return

        for i in range(idx, len(numbers)):
            num = numbers[i]

            # For each number, create a new tuple key and new TreeNode object
            s1 = s + (num,)
            self._map[s1] = TreeNode(s1)

            # Create new keys and TreeNodes based on the current key
            self._generate_map(numbers, s1, i+1)

    def _generate_refs(self):
        """Adds references from one TreeNode to another TreeNode

        This method constructs a structure between different TreeNodes with the following properties:

            1. A TreeNode with a key of length n will only reference to other TreeNodes with a key of length n+1.
            2. A TreeNode with a key of set k will only reference other TreeNodes that are a superset of set k.

        Example:

            TreeNode of key (0, 1, 3) connects to TreeNodes of keys (0, 1, 2, 3), (0, 1, 3, 4), (0, 1, 3, 5), etc.
            TreeNode of key (0) connects to TreeNodes of keys (0, 1), (0, 2), etc.
            TreeNode of key (0, 1, 2, 3, ..., n) of max length n will connect to no TreeNodes.

        """
        # Obtain list of keys and sort based on length
        keys = list(self._map.keys())
        keys.sort(key=lambda x: len(x))

        # Add references to each TreeNode in the map
        for key in keys:
            for ref_key in keys:
                # Keys are sorted by length, we have passed all the keys we care about
                if len(ref_key) > (len(key) + 1):
                    break

                # Reference key isn't proper length, skip reference key
                if len(ref_key) != (len(key) + 1):
                    continue

                # Reference key isn't superset of current key, skip reference key
                if not all(item in ref_key for item in key):
                    continue

                # Properties validated; adding reference to specific TreeNode
                self._map[key].node_forest.append(self._map[ref_key])


if __name__ == "__main__":
    test = InclusionMap(6)

    # Test the references in the InclusionMap
    keys = list(test._map.keys())
    keys.sort(key=lambda x: len(x))

    print(len(keys), keys, "\n")

    for key in test._map:
        print(key, test._map[key].node_forest)
