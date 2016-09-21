temp_list=[]
temp=""
with open('twitter_text.txt',"rb") as f:
	temp_list=f.read().splitlines()
f_pos=open("pos_tweet_train","w")
f_neg=open("neg_tweet_train","w")
f_neutral=open("neutral_tweet","w")

f_pos_test=open("pos_tweet_test","w")
f_neg_test=open("neg_tweet_test","w")

# print temp_list[0:4]
# print(temp_list[0:2])
for t in temp_list[:3500]:	
	# t=str(t)	
	# print (type(t))
	temp=t.replace('\t',' ')
	# temp=bytes(temp)
	# temp=list(temp)
	temp=temp.split()	
	# print t
	# print (temp[1])
	if float(temp[1])>=0:
		temp_str=""
		# print "a"
		for t1 in temp[2:]:
			temp_str=temp_str+" "+t1
		f_pos.write(temp_str+'\n')
	elif float(temp[1])<0:
		temp_str=""
		for t1 in temp[2:]:
			temp_str=temp_str+" "+t1
		f_neg.write(temp_str+'\n')
for t in temp_list[3501:]:
	temp=t.replace('\t',' ')
	temp=temp.split()	
	# print temp[1]	
	if float(temp[1])>=0:
		temp_str=""
		# print "a"
		for t1 in temp[2:]:
			temp_str=temp_str+" "+t1
		f_pos_test.write(temp_str+'\n')
	elif float(temp[1])<0:
		temp_str=""
		for t1 in temp[2:]:
			temp_str=temp_str+" "+t1
		f_neg_test.write(temp_str+'\n')

	# else:
	# 	temp_str=""
	# 	for t1 in temp[2:]:
	# 		temp_str=temp_str+" "+t1
	# 	f_neutral.write(temp_str+'\n')
	# temp1=temp.split()
	# print (temp1[1])	
f_pos.close()

f_neg.close()

f_neutral.close()
f_pos_test.close()

f_neg_test.close()
