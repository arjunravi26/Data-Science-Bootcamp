class TrieNode:
    def __init__(self) -> None:
        self.words = [None] * 26
        self.wordEnd = False


class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()

    def insert(self, word):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.words[idx]:
                curr.words[idx] = TrieNode()
            curr = curr.words[idx]
        curr.wordEnd = True

    def display(self, word):
        curr = self.root
        for char in word:
            idx = ord(char) - ord('a')
            if not curr.wordEnd:
                print(chr(idx + ord('a')))
                curr = curr.words[idx]

    def prefix_search(self, key):
        if not self.root:
            return False
        curr = self.root
        for char in key:
            idx = ord(char) - ord('a')
            if not curr.words[idx]:
                return False
            curr = curr.words[idx]
        return True

    def search(self, key):
        if not self.root:
            return False
        curr = self.root
        for c in key:
            idx = ord(c) - ord('a')
            if not curr.words[idx]:
                return False
            curr = curr.words[idx]
        return curr.wordEnd

    def delete(self, key):
        if not self.root:
            return False

        def _delete(curr, key, depth):
            if depth == len(key):
                return not curr.wordEnd and not any(curr.words)
            idx = ord(key[depth]) - ord('a')
            print(chr(idx + ord('a')))
            should_delete = _delete(curr.words[idx], key, depth+1)
            if should_delete:
                curr.words[idx] = None
                return not curr.wordEnd and not any(curr.words)
            return False
        return _delete(self.root, key, 0)


trie = Trie()
trie.insert('arjun')
trie.display('arjun')
print(trie.prefix_search('arr'))
print(trie.search('arjun'))
print(trie.delete('ar'))
print(trie.search('arjun'))
