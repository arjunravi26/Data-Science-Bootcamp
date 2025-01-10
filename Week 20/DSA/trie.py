class TrieNode:
    def __init__(self):
        self.child = [None] * 26
        self.wordEnd = False


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word):
        curr = self.trie
        for c in word:
            idx = ord(c) - ord('a')
            if curr.child[idx] is None:
                curr.child[idx] = TrieNode()
            curr = curr.child[idx]
        curr.wordEnd = True

    def delete(self, word):
        def _delete(curr,word,depth):
            if curr is None:
                return False
            if depth == len(word):
                if curr.wordEnd:
                    return not any(curr.child)
                return curr.wordEnd
            idx = ord(word[depth]) - ord('a')
            should_delete = _delete(curr.child[idx],word,depth+1)
            if should_delete:
                curr.child[idx] = None
                return not any(curr.child)
            return False
        return _delete(self.trie,word,0)

    def search(self, word):
        curr = self.trie
        for c in word:
            idx = ord(c) - ord('a')
            if curr.child[idx] is None:
                return False
            curr = curr.child[idx]
            print(chr(idx + ord('a')))
        return curr.wordEnd


trie = Trie()
trie.insert('arjun')
trie.insert('shahan')
trie.insert('Nihal')
trie.insert('shammil')
print(trie.search('shammil'))
print(trie.delete('shammil'))
print(trie.search('shammil'))