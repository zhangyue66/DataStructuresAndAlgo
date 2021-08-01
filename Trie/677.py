class TrieNode:
    def __init__(self):
        self.children = [None]*26
        self.is_end_word = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.ans = []
    
    def insert_to_trie(self,word):
        cur = self.root
        for char in word:
            index = ord(char) - ord("a")
            if cur.children[index] is None:
                cur.children[index] = TrieNode()           
            cur = cur.children[index]
        cur.is_end_word = True
        
#     def search_word_in_trie(self,word):
#         cur = self.root
        
#     def start_with_in_trie(self,prefix):
#         pass

    def search_words_prefix_in_trie(self,prefix):
        cur = self.root
        for char in prefix:
            index = ord(char) - ord("a")
            if cur.children[index] is None:
                return self.ans
            cur = cur.children[index]
        # we prove that in Trie there is words with prefix. Now find the words
        self.dfs_in_trie(cur,prefix,"")
        
        #return self.ans
        
    def dfs_in_trie(self,node,prefix,cand=""):
        if node.is_end_word:
            self.ans.append(prefix+cand)
        if not node:
            return
        for i in range(26):
            if node.children[i] is not None:
                string = chr(ord("a")+i)
                self.dfs_in_trie(node.children[i],prefix,cand+string)
            
        
class MapSum(object):
    def __init__(self):
        self.trie = Trie()
        self.dic = {}
        
    def insert(self, key, val):
        if key not in self.dic:
            self.trie.insert_to_trie(key)
        self.dic[key] = val
        
    def sum(self, prefix):
        score = 0
        self.trie.ans = []
        self.trie.search_words_prefix_in_trie(prefix)
        if not self.trie.ans:
            return score
        #print(self.trie.ans)
        print(self.dic)
        for node in self.trie.ans:
            score += (self.dic[node])
        return score

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
