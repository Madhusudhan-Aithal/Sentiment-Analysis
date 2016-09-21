import string
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import wordnet as wn

def negate(l):
	sentences=sent_tokenize(l)	
	neg_words=["not","no"]
	# res_list=[]	
	for s in sentences:
		res_sent=[]
		# print(s)
		words = word_tokenize(s)
		print (words)
		antonyms_list=[]
		for w1,w2 in zip(words[:-1],words[1:]):			
			invalidChars = set(string.punctuation.replace("_", ""))
			if any(char in invalidChars for char in w1):
				continue
			if any(char in invalidChars for char in w2):
				continue
			if w1 in neg_words:
				temp_syn=wn.synsets(w2)
				for temp_w in temp_syn[0].lemmas():
					if temp_w.antonyms():
						antonyms_list.append(temp_w.antonyms()[0].name())
				min_sim=1.01
				min_word=""
				# print (antonyms_list)
				for ant in antonyms_list:
					if w2.wup_similarity(ant)<min_sim:
						min_sim=w2.wup_similarity(ant)
						min_word=ant
				print (min_word)
				res_sent.append(min_word)
			else:
				res_sent.append(w1)
				res_sent.append(w2)
		# res_list.append(res_sent)		
	return res_sent
print (negate("I am not good. You are no good"))

