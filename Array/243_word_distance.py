"""
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

"""

from collections import defaultdict
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        distance_map = defaultdict(list)
        for index,word in enumerate(wordsDict):
            distance_map[word].append(index)
            
        d1 = distance_map[word1]
        d2 = distance_map[word2]
        ans = float("inf")
        for i in range(len(d1)):
            for j in range(len(d2)):
                d = abs(d1[i]-d2[j])
                ans = min(ans,d)
                
        return ans
            
        
