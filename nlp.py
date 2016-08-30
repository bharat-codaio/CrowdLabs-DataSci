
from nltk.corpus import wordnet as wn
from nltk.corpus import wordnet_ic
from sklearn.feature_extraction.text import CountVectorizer
from collections import Counter
import numpy as np


brown_ic = wordnet_ic.ic('ic-brown.dat')

def basic_paraphrase_recognizer(sentence1, sentence2, similarityThreshold):

	corpus = [sentence1,sentence2]
	vectorizer = CountVectorizer(min_df=1)
	tf = vectorizer.fit_transform(corpus)

	count_matrix = tf.toarray()
	count_matrix[count_matrix > 0] = 1 #(Set all count values > 1) = 1

	word_list = vectorizer.get_feature_names()
	num = len(word_list)
	W = np.zeros([num,num])

	for i in range(num):
		for j in range(num):

			s1 = wn.synsets(word_list[i])
			s2 = wn.synsets(word_list[j])

			if s1 != [] and s2 != [] and s1[0]._pos == s2[0]._pos:
				W[i][j] = wn.jcn_similarity(s1[0], s2[0], brown_ic)
			else:
				W[i][j] = 0

	num = len(word_list)
	W = [[0 for i in range(num)] for j in range(num)]	
	for i in range(num):
		for j in range(num):
			s1 = wn.synsets(word_list[i])
			s2 = wn.synsets(word_list[j])
			if s1 != [] and s2 != [] and s1[0]._pos == s2[0]._pos:
				W[i][j] = wn.wup_similarity(s1[0], s2[0], brown_ic)
			elif i == j:
				W[i][j] = 1
			else:
				W[i][j] = 0

	W = np.matrix(W)
	cm = np.matrix(count_matrix)

	# Return 1 if similar, return 0 if not similar
	if (cm[0]*W*cm[1].T/(np.linalg.norm(cm[0])*np.linalg.norm(cm[1])) > similarityThreshold):
		return 1
	else:
		return 0



