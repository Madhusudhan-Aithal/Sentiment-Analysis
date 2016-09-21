from nltk.corpus import nps_chat
import sentiment_mod as s
posts = nps_chat.xml_posts()
print(len(posts))
output = open("out.txt","a")

for sen in posts:
	print(sen.text )
	print(s.sentiment(sen.text) )
	print(" ")
	print ((s.sentiment(sen.text)))
	#sentiment_value = s.sentiment(sen.text)[1]
	output.write(str(s.sentiment(sen.text)[0]))
	output.write('\n')

output.close()	