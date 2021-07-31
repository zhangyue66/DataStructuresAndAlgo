class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end_word = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        cur = self.root
        for char in word:
            index = ord(char)-ord("a")
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.is_end_word = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        cur = self.root
        for char in word:
            index = ord(char)-ord("a")
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
        if cur.is_end_word is False:
            return False
        return True
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        cur = self.root
        for char in prefix:
            index = ord(char)-ord("a")
            if cur.children[index] is None:
                return False
            cur = cur.children[index]
            
        return True
