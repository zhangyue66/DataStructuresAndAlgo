class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        l = len(beginWord)
        wordList = set(wordList)
        queue = [[beginWord,1]]
        while queue:
            word,length = queue.pop(0)
            if word == endWord:
                return length
            
            for i in range(l):
                for j in range(26):
                    if word[i] == chr(97+j):
                        continue
                    new_word = word[:i]+chr(97+j)+word[i+1:]
                    if new_word in wordList:
                        wordList.remove(new_word)
                        queue.append([new_word,length+1])
                    
        return 0
            
