from Map import TreeNode


class InclusionMap(object):
    """The mapping used to organize and initialize TreeNodes in relation
    to each other.

    Args:
        numbers (list[int]): The numbers used in the Numbers Round.

    """

    def __init__(self, numbers=[i for i in range(6)]):
        # The main dict map used to store each TreeNode
        self.map = {}

        # Initializing the map values and TreeNodes
        self._generate_map(numbers)
        self._generate_refs()

    def add(self, new_tree):
        key = tuple(new_tree.numbers)
        self.map[key].add_tree(new_tree)

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
            self.map[s1] = TreeNode(s1)

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
        keys = list(self.map.keys())
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
                self.map[key].node_forest.append(self.map[ref_key])


if __name__ == "__main__":
    test = InclusionMap([1, 2, 3, 4, 5, 6])
    keys = list(test.map.keys())
    keys.sort(key=lambda x: len(x))
    print(len(keys), keys)
    print()
    for key in test.map:
        print(key, test.map[key].node_forest)
