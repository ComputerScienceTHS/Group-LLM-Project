import numpy as np
import math


v1 = np.array([1, 1, 1, 1, 1, 1])
v2 = np.array([3, 3, 3, 4, 2, 2])
v3 = np.array([25, 32, 6, 4, 10, 18])


# Calculates term frequency
def tf(term, document):
    terms = document.split()
    num_of_terms = len(terms)
    frequency = terms.count(term)
    return frequency/num_of_terms
    
# Calculates inverse document frequency
def idf(term, corpus):
    corp_freq = 0
    for sent in corpus:
        if term in sent:
            corp_freq ++
    return math.log(corp_freq/len(corpus))


def word2sent(vectors, words, corpus):
    # Arr of modified vectors
    comp_arr = []

    # Weights the vecotrs by tf-idf
    for index, vector in enumerate(vectors):
        tf_idf = idf(words[index], corpus) * tf(words[index], words)
        mod_vec = vector * tf_idf
        comp_arr.append(mod_vec)
    
    # Converts to numpy arr
    comp_arr = np.array(comp_arr)

    # Gets average of all vectors (Can now use similarity to compare
    return np.average(comp_arr)
    
    
def magnitude(vector):
    mg = 0
    for number in vector:
        mg += number**2
    return math.sqrt(abs(mg))


# Calculates the similarity between two vectors (scores range between 0 and 1, higher means more similar)
def cos_similarity(vector1, vector2):
    denominator = magnitude(vector1) * magnitude(vector2)
    numerator = np.sum(abs(vector1) * abs(vector2))
    return math.acos((numerator/denominator))


