# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word
        self.sorted_word = sorted(self.word)
    
    
    def is_anagram(self, other_word):
        return sorted(other_word.lower()) == self.sorted_word
        
    def match(self, words):
        return [word for word in words if self.is_anagram(word)]