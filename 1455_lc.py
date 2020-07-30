class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str):
        sentence = sentence.split(" ")

        for word in sentence:
            if len(word) < len(searchWord):
                continue
            else:
                if word[:len(searchWord)]== searchWord:
                    return sentence.index(word)+1


        return -1


yz = Solution()
sentence =  "i love eating burger"
searchWord = "burg"
print(yz.isPrefixOfWord(sentence,searchWord))
