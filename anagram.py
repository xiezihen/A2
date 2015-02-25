#**********************************************************
# Assignment2:
# UTOR user_name: xiezihen
# First Name: Zi Heng
# Last Name: Xie
# Student # 1001634332
#
#
#
# Honour Code: I pledge that this program represents my own

from letterManager import *

class AnagramSolver:
    def __init__(self, dictFile):

        self._dictFile = dictFile
        self._wordManage = []
        self._words = []

        for line in self._dictFile:
            self._words.append(line.strip())
            line = LetterManager(line)
            self._wordManage.append(line)
    
    def generateAnagrams(self, s, max):
        words = self.findWords(s)

    def findWords(self, s):

        inputString = LetterManager(s)
        dictWords = self._wordManage[:]
        for word in self._wordManage:
            index = 0
            while index < 26 and word in dictWords:
                if word.counts[index] > inputString.counts[index]:
                    dictIndex = dictWords.index(word)
                    dictWords.remove(word)
                    self._words.pop(dictIndex)
                index += 1
        self._wordManage = dictWords
        return self._words

if __name__ == '__main__':
    file = open('dict.txt',mode = 'r')
    anagram = AnagramSolver(file)
    print(anagram.findWords('frank'))