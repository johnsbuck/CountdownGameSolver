from Map import TreeNode


class InclusionMap(object):

    def __init__(self, numbers):
        self.map = {}
        self._generate_map([i for i in range(len(numbers))])
        self._generate_refs()

    def _generate_map(self, numbers, s=(), idx=0):
        """Generates the main map used to explore the set of NumberTrees.

        Args:
            numbers (list[int]): The set of numbers that can be used.
            s (tuple): The string that is used as the key for the dictionary
            idx (int): The starting index for reading in numbers
        """
        if idx == len(numbers):
            return []

        keys = []
        for i in range(idx, len(numbers)):
            num = numbers[i]
            s1 = s + (num,)
            self.map[s1] = TreeNode(s1)
            keys.append(s1)
            keys += self._generate_map(numbers, s1, i+1)
        return keys

    def _generate_refs(self):
        keys = list(self.map.keys())
        keys.sort(key=lambda x: len(x))

        for key in keys:
            for ref_key in keys:
                if len(ref_key) > (len(key) + 1):
                    break
                if len(ref_key) != (len(key) + 1):
                    continue
                if not all(item in ref_key for item in key):
                    continue
                self.map[key].node_forest.append(self.map[ref_key])


if __name__ == "__main__":
    test = InclusionMap([1, 2, 3, 4, 5, 6])
    keys = list(test.map.keys())
    keys.sort(key=lambda x: len(x))
    print(len(keys), keys)
    print()
    for key in test.map:
        print(key, test.map[key].node_forest)
