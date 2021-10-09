class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end_of_word = False

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self,word):
        cur = self.root
        for char in word:
            index = ord(char)-ord("a")
            if cur.children[index] is None:
                cur.children[index] = TrieNode()
            cur = cur.children[index]
        cur.is_end_of_word = True
        
    def blur_search(self,word):
        
        def dfs(pos,trienode):
            if pos > len(word):
                return False
            if pos == len(word):
                if trienode and trienode.is_end_of_word:
                    return True
                return False
            if word[pos] == ".":
                for child in trienode.children:
                    if child and dfs(pos+1,child):
                        return True
            else:
                index = ord(word[pos]) - ord("a")
                if trienode and trienode.children[index]:
                    if dfs(pos+1,trienode.children[index]):
                        return True

                return False
        
        return dfs(0,self.root)
        


class WordDictionary(Trie):

    def __init__(self):
        super().__init__()

    def addWord(self, word: str) -> None:
        super().insert(word)
        

    def search(self, word: str) -> bool:
        return super().blur_search(word)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
