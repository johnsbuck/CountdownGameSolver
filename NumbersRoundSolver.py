from Node import NumberTree
from Map import InclusionMap
import sys
import time
import random
from collections import deque


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

    def get_all_solutions(self):
        return list(self.solve())

    def solve(self):
        # Queue for latest tree
        tree_queue = deque()

        # Map for finding matching tree listings
        tree_map = InclusionMap(len(self.numbers))

        # Add elemental trees to the queue and map
        for index, i in enumerate(self.numbers):
            tree = NumberTree(i, (index,))
            tree_map.add(tree)
            tree_queue.append(tree)

        # Main loop
        while len(tree_queue) != 0:
            left_subtree = tree_queue.popleft()
            # If tree is a solution, yield the answer
            if abs(left_subtree.value - self.goal) < sys.float_info.epsilon:
                yield left_subtree

            # Find all possible selection with left subtree
            right_selection = tree_map.get_trees(left_subtree.key)
            for right_subtree in right_selection:
                # Skip most symmetrical trees, since addition and multiplication is commutative
                if left_subtree.value >= right_subtree.value:
                    self._add_tree(tree_map, tree_queue, left_subtree, right_subtree, "+")
                    self._add_tree(tree_map, tree_queue, left_subtree, right_subtree, "*")

                # Add subtraction tree
                self._add_tree(tree_map, tree_queue, left_subtree, right_subtree, "-")

                # Add division tree if right value isn't 0
                if abs(right_subtree.value) > sys.float_info.epsilon:
                    self._add_tree(tree_map, tree_queue, left_subtree, right_subtree, "/")

    def _add_tree(self, tree_map, tree_queue, left, right, operator):
        tree = NumberTree(left, right, operator)
        tree_map.add(tree)
        tree_queue.append(tree)


if __name__ == "__main__":
    solver = NumbersRoundSolver()
    print(solver.numbers, solver.goal)
    solve_gen = list(solver.solve())
