"""
Task 1
Реалізуйте два додаткових методи для класу Trie:

count_words_with_suffix(pattern)
для підрахунку кількості слів, що закінчуються заданим шаблоном;
has_prefix(prefix)
для перевірки наявності слів із заданим префіксом.


Технічні умови

- Клас Homework має успадковувати базовий клас Trie.
- Методи повинні опрацьовувати помилки введення некоректних даних.
- Вхідні параметри обох методів мають бути рядками.
- Метод count_words_with_suffix має повертати ціле число.
- Метод has_prefix має повертати булеве значення.

"""

from trie import Trie


class HomeWork(Trie):
    """For home work"""

    def __init__(self):
        super().__init__()
        self.reversed_trie = Trie()

    def put(self, key, value=None):
        super().put(key, value)
        self.reversed_trie.put(key[::-1], value)

    def keys_with_suffix(self, suffix) -> list[str]:
        """Find all keys with suffix"""
        return self.reversed_trie.keys_with_prefix(suffix[::-1])

    def count_words_with_suffix(self, pattern) -> int:
        """
        Count words with pattern suffix
        """
        if not isinstance(pattern, str):
            raise TypeError(
                f"Illegal argument for countWordsWithSuffix: pattern = {pattern} must be a string"
            )
        return len(self.keys_with_suffix(pattern))

    def has_prefix(self, prefix) -> bool:
        """Check prefix exist in trie"""
        if not isinstance(prefix, str):
            raise TypeError(
                f"Illegal argument for hasPrefix: prefix = {prefix} must be a string"
            )

        current = self.root
        for char in prefix:
            if char not in current.children:
                return False
            current = current.children[char]

        return True


def run_test(trie: HomeWork):
    """Run test for home work"""
    # Перевірка кількості слів, що закінчуються на заданий суфікс
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat
    assert trie.count_words_with_suffix("") == 4  # all words
    assert trie.count_words_with_suffix("non") == 0  # no words
    assert trie.count_words_with_suffix("E") == 0  # no words
    assert trie.keys_with_prefix("App") == []  # no words
    assert trie.keys_with_prefix("app") == ["apple", "application"]

    # Перевірка наявності префікса
    assert trie.has_prefix("app") is True  # apple, application
    assert trie.has_prefix("bat") is False
    assert trie.has_prefix("ban") is True  # banana
    assert trie.has_prefix("ca") is True  # cat
    assert trie.has_prefix("") is True  # all words

    # TypeValue Test

    try:
        trie.count_words_with_suffix(10)
    except TypeError as e:
        assert (
            str(e)
            == "Illegal argument for countWordsWithSuffix: pattern = 10 must be a string"
        )
    try:
        trie.has_prefix(10)
    except TypeError as e:
        assert str(e) == "Illegal argument for hasPrefix: prefix = 10 must be a string"


def seed_trie(trie: HomeWork, words: list[str]):
    """Seed trie with words"""
    for i, word in enumerate(words):
        trie.put(word, i)


def main():
    """Main function"""
    trie = HomeWork()
    seed_trie(trie, ["apple", "application", "banana", "cat"])
    run_test(trie)


if __name__ == "__main__":
    main()
