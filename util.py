try:
    import pygtrie as trie
except ImportError:
    print("Install dulu pygtrie")

class Trie:
    """
    Trie implementation from pygtrie with search operation. All words made upper case
    """
    def __init__(self, words):    
        self.t = trie.CharTrie()
        for word in words:
            self.t[word.upper()] = True
    def search(self, word):
        word = word.upper()
        if self.t.has_key(word) == False:
            return False
        else:
            return True