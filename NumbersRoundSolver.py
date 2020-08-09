from Node import NumberTree
from Map import InclusionMap
from collections import deque
from queue import PriorityQueue
import time
import math
import random


class NumbersRoundSolver(object):

    def __init__(self, numbers=None, goal=None):
        self.numbers = self.generate_numbers() if numbers is None else numbers
        self.numbers.sort()
        self.goal = random.randint(100, 999) if goal is None else goal

    @property
    def numbers(self) -> [int, float]:
        return self._numbers

    @property
    def goal(self) -> (int, float):
        return self._goal

    @numbers.setter
    def numbers(self, value: [int, float]):
        if type(value) is not list:
            raise ValueError()
        for item in value:
            if type(item) not in (int, float):
                raise ValueError()
        self._numbers = value
        self._numbers.sort()

    @goal.setter
    def goal(self, value: (int, float)):
        if type(value) not in (int, float):
            raise ValueError()
        self._goal = value

    def g(self, x):
        return abs(x.value - self.goal)

    @staticmethod
    def generate_numbers():
        small_nums = list(range(1, 11)) * 2
        large_nums = [25, 50, 75, 100]

        return [small_nums.pop(random.randrange(0, len(small_nums))) for _ in range(4)] + \
               [large_nums.pop(random.randrange(0, len(large_nums))) for _ in range(2)]

    def get_all_solutions(self):
        return list(self.solve())

    def solve(self, map=None, sub_key=()):
        # Queue for latest tree
        tree_queue = PriorityQueue()

        # Map for finding matching tree listings
        if map is None:
            tree_map = InclusionMap(len(self.numbers))

            # Add elemental trees to the queue and map
            for index, i in enumerate(self.numbers):
                tree = NumberTree(i, (index,))
                tree_map.add(tree)
                tree_queue.put((self.g(tree), tree))
        else:
            tree_map = map

        best = tree_queue.get()[1]
        tree_queue.put((self.g(best), best))

        # Main loop
        while tree_queue.qsize() != 0:
            left_subtree = tree_queue.get()[1]
            # If tree is a solution, yield the answer
            if math.isclose(left_subtree.value, self.goal):
                yield left_subtree
            if abs(best.value - self.goal) > abs(left_subtree.value - self.goal):
                best = left_subtree

            right_selection = tree_map.get_trees(left_subtree.key + sub_key)

            op_str = ["+", "-", "*", "/"]
            solution_found = False
            if len(sub_key) == len(self.numbers):
                for index, op in enumerate([lambda x: x - self.goal, lambda x: x + self.goal, \
                                            lambda x: x / self.goal, lambda x: x * self.goal]):
                    sub_goal = op(left_subtree.value)
                    sub_solver = NumbersRoundSolver(goal=sub_goal)
                    print(left_subtree, left_subtree.key)
                    right_subtree = next(sub_solver.solve(left_subtree.key + sub_key))
                    if self._add_tree(tree_map, tree_queue, left_subtree, right_subtree, op_str[index]):
                        solution_found = True
                        break

            # Find all possible selection with left subtree
            if not solution_found:
                for right_subtree in right_selection:
                    # Skip most symmetrical trees, since addition and multiplication is commutative
                    if left_subtree.value >= right_subtree.value:
                        self._add_tree(tree_map, tree_queue, left_subtree, right_subtree, "+")
                        self._add_tree(tree_map, tree_queue, left_subtree, right_subtree, "*")

                    # Add subtraction tree
                    self._add_tree(tree_map, tree_queue, left_subtree, right_subtree, "-")

                    # Add division tree if right value isn't 0
                    if not math.isclose(right_subtree.value, 0):
                        self._add_tree(tree_map, tree_queue, left_subtree, right_subtree, "/")

        # If there is no solution, return best solution
        if not math.isclose(best.value, self.goal):
            yield best

    def _add_tree(self, tree_map, tree_queue, left, right, operator):
        tree = NumberTree(left, right, operator)
        tree_map.add(tree)
        tree_queue.put((self.g(tree), tree))


if __name__ == "__main__":
    total = 100
    avg = []
    for i in range(total):
        solver = NumbersRoundSolver()
        print(solver.numbers, solver.goal)
        start = time.perf_counter()
        solve = solver.solve()
        sol = next(solve)
        end = time.perf_counter()
        print(i+1, ":", f"{end - start:0.4f} seconds")
        avg.append(end - start)
    print("Average:", sum(avg) / len(avg))
    print("Max Time:", max(avg))
    print("Min Time:", min(avg))
