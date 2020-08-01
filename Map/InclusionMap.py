from Node import NumberTree


class InclusionMap(object):

    def __init__(self, numbers):
        self.map = {}
        self._generate_map(numbers[:])

    def _generate_map(self, numbers, s="", idx=0):
        """Generates the main map used to explore the set of NumberTrees.

        Args:
            numbers (list[int]): The set of numbers that can be used.
            s (str): The string that is used as the key for the dictionary
            idx (int): The starting index for reading in numbers
        """
        if idx == len(numbers):
            self.map[s] = []
            return
        for i in range(idx, len(numbers)):
            num = numbers[i]
            s1 = s + str(num)
            self.map[s1] = []
            self._generate_map(numbers, s1, i+1)


if __name__ == "__main__":
    test = InclusionMap([1, 2, 3, 4, 5, 6])
    keys = list(test.map.keys())
    keys.sort(key=lambda x: len(x))
    print(len(keys), keys)
