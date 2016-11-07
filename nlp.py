from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
import numpy as np
brown_ic = wordnet_ic.ic('ic-brown.dat')



def basic_paraphrase_recognizer(sentence1, list_of_sentences, similarityThreshold):
    index = -1
    max_sim = 0
    for count,sentence2 in enumerate(list_of_sentences):
        corpus = [sentence1,sentence2]
        vectorizer = CountVectorizer(min_df=1)
        tf = vectorizer.fit_transform(corpus)

        count_matrix = tf.toarray()
        count_matrix[count_matrix > 0] = 1 #(Set all count values > 1) = 1

        word_list = vectorizer.get_feature_names()
        ##print(word_list)
        num = len(word_list)
        W = [[0 for i in range(num)] for j in range(num)]
        
        for i in range(num):
            for j in range(num):
                s1 = wn.synsets(word_list[i])
                s2 = wn.synsets(word_list[j])
  
                if s1 != [] and s2 != [] and s1[0]._pos == s2[0]._pos:
                    W[i][j] = wn.jcn_similarity(s1[0], s2[0], brown_ic)
                else:
                    W[i][j] = 0
                if i == j:
                    W[i][j] = 1

        
        W = np.matrix(W)
        cm = np.matrix(count_matrix)
        top =  cm[0]*W*cm[1].T
        similarity = top/(np.linalg.norm(cm[0])*np.linalg.norm(cm[1]))
        if similarity > max_sim:
            max_sim = similarity
            index = count

    if float(max_sim) > float(similarityThreshold):
        return index
    else:
        return -1




