from Node import KNode
import random
import re


class LettersRoundSolver(object):

    def __init__(self, letters=None):
        self.tree = KNode("")

        self.letters = self.generate_letters() if letters is None else letters
        self.letters.sort()

        i = 0
        with open("wordlist.txt", "r+") as f:
            lines = f.readlines()
            for word in lines:
                word = word[:-1]
                if re.match("^[a-z]+$", word) is None:
                    continue
                i += 1
                line = [char for char in word]
                line.sort()
                node = self.tree
                for char in line:
                    node.add_child(char)
                    node = node.children[char]
                node.value = word
        print(i)

    @staticmethod
    def generate_letters():
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = list(set([chr(i) for i in range(ord('a'), ord('z') + 1)]) - set(vowels))
        consonants.sort()

        return [vowels.pop(random.randrange(0, len(vowels))) for _ in range(3)] + \
               [consonants.pop(random.randrange(0, len(consonants))) for _ in range(6)]

    def solve_all(self):
        output = []

        letters = self.letters[:]
        for i in range(len(letters)):
            if i > 0 and letters[i] == letters[i - 1]:
                continue
            if letters[i] not in self.tree.children:
                continue
            char = letters.pop(i)
            output += self._solve_all(self.tree.children[char], letters)
            letters.insert(i, char)

        output.sort(key=lambda x: len(x), reverse=True)
        return output

    def _solve_all(self, node, letters):
        output = [] if node.value is None else [node.value]
        for i in range(len(letters)):
            if i > 0 and letters[i] == letters[i - 1]:
                continue
            if letters[i] not in node.children:
                continue
            char = letters.pop(i)
            output += self._solve_all(node.children[char], letters)
            letters.insert(i, char)
        return output


if __name__ == "__main__":
    solver = LettersRoundSolver()
    print(solver.letters)
    print(solver.solve_all())
