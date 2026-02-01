"""
# 백준
# No. 5052
# Python 3.11.9
# by "nno0obb"
"""

import sys
from collections import defaultdict


class TrieNode:
    def __init__(self, is_end: bool = False):
        self.is_end = is_end
        self.children = defaultdict(TrieNode)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            curr_node = curr_node.children[char]
        curr_node.is_end = True

    def search(self, word: str) -> bool:
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
        return curr_node.is_end

    def has_prefix(self, word: str) -> bool:
        curr_node = self.root
        for char in word[:-1]:
            if char not in curr_node.children:
                return False
            curr_node = curr_node.children[char]
            if curr_node.is_end:
                return True
        return False


def main():
    # Input
    T = int(input())
    for _ in range(T):
        N = int(input())
        L = [sys.stdin.readline().strip() for _ in range(N)]

        # Logic
        trie = Trie()
        for word in L:
            trie.insert(word)

        is_consistent = True
        for word in L:
            if trie.has_prefix(word):
                is_consistent = False
                break

        # Output
        print("YES" if is_consistent else "NO")


if __name__ == "__main__":
    main()
