from random import randint

class MarkovLyrics:
    def __init__(self):
        """
        self.chain = {
            #Lists contain possible words that can come after a word (key)
            "baby": ["plays", "crawls", "sleeps", "plays", "plays"],
            "plays": ["toy", "food"]
        }
        """
        self.chain = {}
    
    def populateMarkovChain(self, lyrics):
        for line in lyrics:
            words = line.split(" ")

            for i in range(len(words)-1):
                word = words[i]

                if word in self.chain:
                    self.chain[word].append(words[i+1]) #Append next word
                else:
                    self.chain[word] = [words[i+1]] #Otherwise, create new array

    def generateLyrics(self, length=500):
        n = len(self.chain)

        #Start with random word
        start_index = randint(0, n-1) 
        keys = list(self.chain.keys())
        current_word = keys[start_index].title()
        
        lyrics = current_word + " "
        for i in range(length):
            if current_word not in self.chain: #End line
                lyrics += "\n"
                next_index = randint(0, n-1)
                current_word = keys[next_index]
                lyrics += current_word + " "
            else: #Adding words
                current_list = self.chain[current_word]
                next_index = randint(0, len(current_list)-1)
                next_word = current_list[next_index]
                lyrics += next_word + " "
                current_word = next_word #Set new current word to next word

        return lyrics
"""
data = ["I am Eric", "I am an engineer", "I like to code"]
m = MarkovLyrics()
m.populateMarkovChain(data)
print(m.generateLyrics())
"""