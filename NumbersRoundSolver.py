from Node import NumberTree
from Map import InclusionMap
import sys
import random


class NumbersRoundSolver(object):

    def __init__(self, numbers=None, solve_num=None):
        self.numbers = self.generate_numbers() if numbers is None else numbers
        self.numbers.sort()
        self.goal = random.randint(100, 999) if solve_num is None else solve_num

    @staticmethod
    def generate_numbers():
        small_nums = list(range(1, 11)) * 2
        large_nums = [25, 50, 75, 100]

        return [small_nums.pop(random.randrange(0, len(small_nums))) for _ in range(4)] + \
               [large_nums.pop(random.randrange(0, len(large_nums))) for _ in range(2)]

    # @staticmethod
    # def formula_reader(bt: BTNode):
    #     formula = bt.print_tree(prefix="(", suffix=")")
    #
    #     print(formula)

    def solve(self):
        print(self.numbers, self.goal)

        tree_map = InclusionMap(len(self.numbers))

        for index, i in enumerate(self.numbers):
            tree_map.add(NumberTree(i, (index,)))
        all_trees = tree_map.all_trees()
        for left_subtree in all_trees:
            key = left_subtree.key
            right_selection = tree_map.get_trees(key)
            for right_subtree in right_selection:
                if left_subtree.value >= right_subtree.value:
                    tree_map.add(NumberTree(left_subtree, right_subtree, "+"))
                    tree_map.add(NumberTree(left_subtree, right_subtree, "*"))

                tree_map.add(NumberTree(left_subtree, right_subtree, "-"))

                if right_subtree.value != 0:
                    tree_map.add(NumberTree(left_subtree, right_subtree, "/"))

        for tree in tree_map.all_trees():
            if abs(tree.value - self.goal) < sys.float_info.epsilon:
                print(tree, tree.value)
        print(self.numbers, self.goal)


if __name__ == "__main__":
    solver = NumbersRoundSolver()
    solver.solve()
