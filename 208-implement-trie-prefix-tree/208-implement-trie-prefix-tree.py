class Trie:

    def __init__(self):
        self.data = {}

    def insert(self, word: str) -> None:
        self.data[word] = True

    def search(self, word: str) -> bool:
        return word in self.data.keys()

    def startsWith(self, prefix: str) -> bool:
        for word in self.data.keys():
            if word.startswith(prefix):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)