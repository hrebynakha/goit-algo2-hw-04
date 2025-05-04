"""
Task 2

Створіть клас LongestCommonWord, який наслідує клас Trie,
 та реалізуйте метод find_longest_common_word,
 який знаходить найдовший спільний префікс для всіх слів
 у вхідному масиві рядків strings.



Технічні умови

- Клас LongestCommonWord має успадковувати Trie.
- Вхідний параметр методу find_longest_common_word, strings
     — масив рядків.
- Метод find_longest_common_word має повертати рядок
    — найдовший спільний префікс.
- Час виконання —O(S), де S — сумарна довжина всіх рядків.
"""

from trie import Trie, TrieNode


class LongestCommonWord(Trie):
    """Longest common word"""

    def find_longest_common_word(self, strings) -> str:
        """Find longest common word"""

        if not isinstance(strings, list):
            raise TypeError(
                f"Illegal argument: expected list of strings, got {type(strings).__name__}"
            )

        for string in strings:
            if not isinstance(string, str) or not string:
                raise TypeError(
                    f"Illegal argument: expected string, got {type(string).__name__}"
                )
        if not strings:
            return ""

        self.clean_trie()
        self.seed_trie(strings)

        return self.find_longest_common_prefix()

    def seed_trie(self, strings):
        """Seed trie"""
        for i, word in enumerate(strings):
            self.put(word, i)

    def find_longest_common_prefix(self):
        """Find longest common prefix"""
        current, prefix = self.root, ""

        while len(current.children) == 1:
            # for fully inserted words
            if current.value is not None:
                break

            # while only one child, continue to next node
            char = next(iter(current.children))
            current = current.children[char]
            prefix += char

        return prefix

    def clean_trie(self):
        """Clean trie"""
        self.root = TrieNode()
        self.size = 0


def run_test(trie: LongestCommonWord, strings: list[str], expected: str):
    """Run test for longest common word"""
    assert trie.find_longest_common_word(strings) == expected


def main():
    """Main function"""
    trie = LongestCommonWord()
    run_test(trie, ["flower", "flow", "flight"], "fl")
    run_test(trie, ["interspecies", "interstellar", "interstate"], "inters")
    run_test(trie, ["dog", "racecar", "car"], "")


if __name__ == "__main__":
    main()
