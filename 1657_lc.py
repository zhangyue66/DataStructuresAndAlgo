class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        #only need to calculate the letter frequency. and order doesnot matters.
        if len(word1) != len(word2):
            return False

        dict1,dict2 = {},{}

        def countLetter(dict,word):
            keys = []
            letters = []
            for i in word:
                if i not in dict:
                    dict[i] = 1
                else:
                    dict[i] += 1

            for k,v in dict.items():
                keys.append(v)
                letters.append(k)

            keys.sort()
            letters.sort()
            return letters,keys

        letter1,key1 = countLetter(dict1,word1)
        letter2,key2 = countLetter(dict2,word2)

        return letter1 == letter2 and key1 == key2
