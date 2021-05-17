import pandas as pd
import re
import numpy as np
import string


class computeTextSimilarity():

    def __init__(self, sentence1: str, sentence2: str):
        self.sentence1 = sentence1 
        self.sentence2 = sentence2 
        
    def get_stopwords(self):
        stopwords = []
        with open("stopwords.txt", "r") as stop_word:
            stopwords = set(stop_word.read().replace('\n', ' ').split(" "))
        return {i for i in stopwords if i != ""}
    
    def generate_ngrams(self, s, n, option):
        #get stopwords
        stopwords = self.get_stopwords()

        # Convert to lowercases
        s = s.lower()
        # Replace all none alphanumeric characters with spaces
        s = re.sub(r'[^a-zA-Z0-9\s]', '', s)
        # Remove punctuation
        translator = str.maketrans('', '', string.punctuation)
        s = s.translate(translator)
        # remove empty value 
        # remove stopwords if specify option as True 
        if option == True: 
            tokens = [token for token in s.split(" ") if (token != "") & (token not in stopwords)]
        else: 
            tokens = [token for token in s.split(" ") if (token != "")]
        # generate n-gram
        ngrams = zip(*[tokens[i:] for i in range(n)])
        
        return [" ".join(ngram) for ngram in ngrams]
    
    def word_dict(self, tokensA, tokensB):

        total_words = set(tokensA).union(set(tokensB))
        dic_A, dic_B = dict.fromkeys(total_words, 0), dict.fromkeys(total_words, 0)

        for word in tokensA:
            dic_A[word] += 1
        for word in tokensB:
            dic_B[word] += 1
        return dic_A, dic_B

    def cos_dist(self, vec1,vec2):
        return float(np.dot(vec1,vec2)/(np.linalg.norm(vec1)*np.linalg.norm(vec2)))
    
    def similarity(self, n, option=False):
        ngram_a = self.generate_ngrams(self.sentence1, n, option)
        ngram_b = self.generate_ngrams(self.sentence2, n, option)    
        vec1, vec2 = self.word_dict(ngram_a,ngram_b)
        return self.cos_dist(list(vec1.values()),list(vec2.values()))  
